# Give the different penalties
import numpy as np


def score_func_raw(algo, cluster_mean, key_reuse_factor):
    # algorithm: [0] = pk_size_bytes, [1] = sk_size_bytes, [2] = artifact_size_bytes, [3] = gen_cycles,
    # [4] = send_op_cycles, [5] = receive_op_cycles cluster: [0] = idle_cpu, [1] = peak_cpu, [2] = avg_TPS,
    # [3] = peak_TPS, [4] = packet_size, [5] = RAM_size

    # key_reuse_factor: How many times do the same keys get reused for a certain client? for example: In ATM systems,
    # every transaction is with a new client, therefore key_reuse_factor = 1. But, for middleware,
    # a single communication line can be held for many transactions, which would allow for a high key_reuse_factor

    idle, peak, tps, p_tps, ram = 0, 1, 2, 3, 4
    scores = {'s_penalty': 0, 'c_penalty': 0, 'm_penalty': 0, 'sec_penalty': 0}

    # prevent negative values:
    # Normalized [0,1]
    idle_cpu = cluster_mean[idle]
    peak_cpu = cluster_mean[peak]
    avg_tps = cluster_mean[tps]
    peak_tps = cluster_mean[p_tps]
    ram = cluster_mean[ram]

    pk = algo['pk_size_bytes']
    sk = algo['sk_size_bytes']
    art = algo['artifact_size_bytes']
    gen = algo['gen_cycles']
    snd = algo['send_op_cycles']
    rcv = algo['receive_op_cycles']
    sec = algo['nist_level']

    # Penalties
    # eps=epsilon, near zero value to prevent zero division
    eps = 1e-9
    # size: bandwidth - the cost of transferring
    scores['s_penalty'] = np.log1p((pk / (key_reuse_factor+eps)) + art) * (peak_tps + avg_tps + eps)
    # memory - the cost of storing
    scarcity = np.minimum(ram, 0.1)
    scores['m_penalty'] = np.log1p(pk + sk + art) / ((ram + eps) * scarcity)

    # compute - the cost of computation
    scores['c_penalty'] = np.log1p(gen + snd + rcv) * (peak_cpu / (1 - peak_cpu + eps)) * idle_cpu
    # security - reward high security with low penalty
    scores['sec_penalty'] = 1 / (np.log1p(sec) ** ((
            (1 - peak_tps) * (1 - peak_cpu) * ram)))

    return scores


# get the sum of scores
def score_func(algo, cluster_mean, key_reuse_factor,
               norm_func, args_s, args_m, args_c, args_sec,
               w_size, w_compute, w_memory, w_security):
    scores = score_func_raw(algo, cluster_mean, key_reuse_factor)
    sp = scores['s_penalty']
    mp = scores['m_penalty']
    cp = scores['c_penalty']
    sec_p = scores['sec_penalty']
    mod_sp = norm_func(sp, args_s) * w_size
    mod_mp = norm_func(mp, args_m) * w_memory
    mod_cp = norm_func(cp, args_c) * w_compute
    mod_sec_p = norm_func(sec_p, args_sec) * w_security
    return mod_sp + mod_mp + mod_cp + mod_sec_p
