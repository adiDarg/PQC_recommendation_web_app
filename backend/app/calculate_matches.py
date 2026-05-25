import joblib

from app.scoring_function import score_func_raw, score_func
from app.PQC_algorithm_data import algorithms
from app.helper_functions import maxAbsScaling
import numpy as np

cluster_means_minmax = joblib.load("./joblib_files/cluster_means_minmax.joblib")


def calculate_penalties_coefficients(key_reuse_factor):
    # Find total penalties
    scores = {'s_penalties': [], 'c_penalties': [], 'm_penalties': [], 'sec_penalties': []}
    for cluster_idx in range(0, len(cluster_means_minmax)):
        for a in algorithms:
            centroid = cluster_means_minmax[cluster_idx]
            raw = score_func_raw(a, centroid, key_reuse_factor)

            scores['s_penalties'].append({'score': raw['s_penalty'], 'cluster': cluster_idx})
            scores['m_penalties'].append({'score': raw['m_penalty'], 'cluster': cluster_idx})
            scores['c_penalties'].append({'score': raw['c_penalty'], 'cluster': cluster_idx})
            scores['sec_penalties'].append({'score': raw['sec_penalty'], 'cluster': cluster_idx})

    s_pts = scores['s_penalties']  # size penalties
    m_pts = scores['m_penalties']  # memory penalties
    c_pts = scores['c_penalties']  # compute penalties
    sec_pts = scores['sec_penalties']  # security penalties
    return [s_pts, m_pts, c_pts, sec_pts]


def calculate_matches(s_pts, m_pts, c_pts, sec_pts, security_level, key_reuse_factor, allowed_problems,
                      w_size, w_compute, w_memory, w_security):
    func = maxAbsScaling

    results = {}
    args_s = [np.mean([x['score'] for x in s_pts])]
    args_m = [np.mean([x['score'] for x in m_pts])]
    args_c = [np.mean([x['score'] for x in c_pts])]
    args_sec = [np.mean([x['score'] for x in sec_pts])]
    for cluster_idx in range(len(cluster_means_minmax)):
        # Cluster dependent arguments
        # args_s = [x['score'] for x in s_pts if x['cluster'] == cluster_idx]
        # args_m = [x['score'] for x in m_pts if x['cluster'] == cluster_idx]
        # args_c = [x['score'] for x in c_pts if x['cluster'] == cluster_idx]

        cluster_results = {}
        for algo_type in ['KEM', 'DSA']:
            # Filter by type and security level
            candidates = [
                a for a in algorithms if
                a['type'] == algo_type and
                (a['nist_level'] >= security_level)
                and
                any([problem in a['math_problem'] for problem in allowed_problems])
            ]
            if len(candidates) == 0:
                cluster_results[algo_type] = 'None'
                continue

            # find algorithm with minimum penalty
            best_algo = min(
                candidates,
                key=lambda a: score_func(
                    a, cluster_means_minmax[cluster_idx], key_reuse_factor,
                    func, args_s, args_m, args_c, args_sec,
                    w_size, w_compute, w_memory, w_security
                )
            )
            cluster_results[algo_type] = best_algo['algorithm']

        results[cluster_idx] = cluster_results
    return results
