algorithms = [
    # ----------KEM----------
    {
        'algorithm': 'ML-KEM-512',
        'type': 'KEM',
        'math_problem': 'Lattice (MLWE)',
        'nist_level': 1,
        'pk_size_bytes': 800,
        'sk_size_bytes': 1632,
        'artifact_size_bytes': 768,
        'gen_cycles': 45457,
        'send_op_cycles': 63854,
        'receive_op_cycles': 87778
    },
    {
        'algorithm': 'ML-KEM-768',
        'type': 'KEM',
        'math_problem': 'Lattice (MLWE)',
        'nist_level': 3,
        'pk_size_bytes': 1184,
        'sk_size_bytes': 2400,
        'artifact_size_bytes': 1088,
        'gen_cycles': 77142,
        'send_op_cycles': 100496,
        'receive_op_cycles': 136444
    },
    {
        'algorithm': 'ML-KEM-1024',
        'type': 'KEM',
        'math_problem': 'Lattice (MLWE)',
        'nist_level': 5,
        'pk_size_bytes': 1568,
        'sk_size_bytes': 3168,
        'artifact_size_bytes': 1568,
        'gen_cycles': 126540,
        'send_op_cycles': 82172,
        'receive_op_cycles': 346755
    },

    {
        'algorithm': 'BIKE-128',
        'type': 'KEM',
        'nist_level': 1,
        'math_problem': 'Codes (QC-MDPC)',
        'pk_size_bytes': 1541,
        'sk_size_bytes': 881,
        'artifact_size_bytes': 1572,
        'gen_cycles': 4535574,
        'send_op_cycles': 382377,
        'receive_op_cycles': 6284216
    },
    {
        'algorithm': 'BIKE-192',
        'type': 'KEM',
        'nist_level': 3,
        'math_problem': 'Codes (QC-MDPC)',
        'pk_size_bytes': 3082,
        'sk_size_bytes': 1510,
        'artifact_size_bytes': 3114,
        'gen_cycles': 14267489,
        'send_op_cycles': 1104598,
        'receive_op_cycles': 19624344
    },
    # Missing
    # {
    #     'algorithm': 'BIKE-256',
    #     'type': 'KEM',
    #     'nist_level': 5,
    #     'math_problem': 'Codes (QC-MDPC)',
    #     'pk_size_bytes': 5122,
    #     'sk_size_bytes': 2325,
    #     'artifact_size_bytes': 5193,
    #     'gen_cycles': ,
    #     'send_op_cycles': ,
    #     'receive_op_cycles':
    # ,

    {
        'algorithm': 'Classic-McEliece-348864',
        'type': 'KEM',
        'nist_level': 1,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 261120,
        'sk_size_bytes': 6492,
        'artifact_size_bytes': 96,
        'gen_cycles': 101510739,
        'send_op_cycles': 43881,
        'receive_op_cycles': 285267
    },
    {
        'algorithm': 'Classic-McEliece-460896',
        'type': 'KEM',
        'nist_level': 3,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 524160,
        'sk_size_bytes': 13608,
        'artifact_size_bytes': 156,
        'gen_cycles': 328665299,
        'send_op_cycles': 89124,
        'receive_op_cycles': 720177
    },
    {
        'algorithm': 'Classic-McEliece-6688128',
        'type': 'KEM',
        'nist_level': 5,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 1044992,
        'sk_size_bytes': 13932,
        'artifact_size_bytes': 208,
        'gen_cycles': 931324896,
        'send_op_cycles': 172006,
        'receive_op_cycles': 839625
    },

    {
        'algorithm': 'Classic-McEliece-348864(f)',
        'type': 'KEM',
        'nist_level': 1,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 261120,
        'sk_size_bytes': 6492,
        'artifact_size_bytes': 96,
        'gen_cycles': 82407209,
        'send_op_cycles': 45743,
        'receive_op_cycles': 284778
    },
    {
        'algorithm': 'Classic-McEliece-460896(f)',
        'type': 'KEM',
        'nist_level': 3,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 524160,
        'sk_size_bytes': 13608,
        'artifact_size_bytes': 156,
        'gen_cycles': 269246744,
        'send_op_cycles': 87712,
        'receive_op_cycles': 720196
    },
    {
        'algorithm': 'Classic-McEliece-6688128(f)',
        'type': 'KEM',
        'nist_level': 5,
        'math_problem': 'Codes (Goppa)',
        'pk_size_bytes': 1044992,
        'sk_size_bytes': 13932,
        'artifact_size_bytes': 208,
        'gen_cycles': 459004376,
        'send_op_cycles': 158854,
        'receive_op_cycles': 840064
    },

    {
        'algorithm': 'HQC-128-1',
        'type': 'KEM',
        'nist_level': 1,
        'math_problem': 'Codes (QCSD)',
        'pk_size_bytes': 2249,
        'sk_size_bytes': 2305,
        'artifact_size_bytes': 4433,
        'gen_cycles': 753431,
        'send_op_cycles': 1294651,
        'receive_op_cycles': 2144421
    },
    {
        'algorithm': 'HQC-192-1',
        'type': 'KEM',
        'nist_level': 3,
        'math_problem': 'Codes (QCSD)',
        'pk_size_bytes': 4522,
        'sk_size_bytes': 4586,
        'artifact_size_bytes': 8978,
        'gen_cycles': 1480267,
        'send_op_cycles': 2844398,
        'receive_op_cycles': 4312051
    },
    {
        'algorithm': 'HQC-256-1',
        'type': 'KEM',
        'nist_level': 5,
        'math_problem': 'Codes (QCSD)',
        'pk_size_bytes': 7245,
        'sk_size_bytes': 7317,
        'artifact_size_bytes': 14421,
        'gen_cycles': 2639361,
        'send_op_cycles': 4749692,
        'receive_op_cycles': 7105993
    },

    {
        "algorithm": "NTRU-HPS-2048-509",
        "type": "KEM",
        "nist_level": 1,
        'math_problem': 'Lattice (NTRU)',
        "pk_size_bytes": 699,
        "sk_size_bytes": 935,
        "artifact_size_bytes": 699,
        'gen_cycles': 2626418,
        'send_op_cycles': 94514,
        'receive_op_cycles': 192931
    },
    {
        "algorithm": "NTRU-HPS-2048-677",
        "type": "KEM",
        "nist_level": 3,
        'math_problem': 'Lattice (NTRU)',
        "pk_size_bytes": 930,
        "sk_size_bytes": 1234,
        "artifact_size_bytes": 930,
        'gen_cycles': 4545605,
        'send_op_cycles': 146051,
        'receive_op_cycles': 309390
    },
    {
        "algorithm": "NTRU-HPS-2048-821",
        "type": "KEM",
        "nist_level": 5,
        'math_problem': 'Lattice (NTRU)',
        "pk_size_bytes": 1230,
        "sk_size_bytes": 1590,
        "artifact_size_bytes": 1230,
        'gen_cycles': 6611641,
        'send_op_cycles': 196684,
        'receive_op_cycles': 431365
    },

    # ----------DSA----------

    {
        'algorithm': 'ML-DSA-512',
        'type': 'DSA',
        'nist_level': 1,
        'math_problem': 'Lattice (MLWE,MSIS)',
        'pk_size_bytes': 1184,
        'sk_size_bytes': 2800,
        'artifact_size_bytes': 2044,
        'gen_cycles': 160000,
        'send_op_cycles': 777955,
        'receive_op_cycles': 672484
    },
    {
        'algorithm': 'ML-DSA-768',
        'type': 'DSA',
        'nist_level': 3,
        'math_problem': 'Lattice (MLWE,MSIS)',
        'pk_size_bytes': 1472,
        'sk_size_bytes': 3504,
        'artifact_size_bytes': 2701,
        'gen_cycles': 295683,
        'send_op_cycles': 1606091,
        'receive_op_cycles': 955701
    },
    {
        'algorithm': 'ML-DSA-1024',
        'type': 'DSA',
        'nist_level': 5,
        'math_problem': 'Lattice (MLWE,MSIS)',
        'pk_size_bytes': 1760,
        'sk_size_bytes': 4864,
        'artifact_size_bytes': 3366,
        'gen_cycles': 449411,
        'send_op_cycles': 1792269,
        'receive_op_cycles': 1419745
    },

    {
        'algorithm': 'SLH-DSA-128-Robust',
        'type': 'DSA',
        'nist_level': 1,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 32,
        'sk_size_bytes': 64,
        'artifact_size_bytes': 7586,
        'gen_cycles': 4046289,
        'send_op_cycles': 140483164,
        'receive_op_cycles': 8621895
    },
    {
        'algorithm': 'SLH-DSA-192-Robust',
        'type': 'DSA',
        'nist_level': 3,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 48,
        'sk_size_bytes': 96,
        'artifact_size_bytes': 16224,
        'gen_cycles': 11361911,
        'send_op_cycles': 226496038,
        'receive_op_cycles': 14586977
    },
    {
        'algorithm': 'SLH-DSA-256-Robust',
        'type': 'DSA',
        'nist_level': 5,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 64,
        'sk_size_bytes': 128,
        'artifact_size_bytes': 29792,
        'gen_cycles': 30008518,
        'send_op_cycles': 428700137,
        'receive_op_cycles': 30611613
    },

    {
        'algorithm': 'SLH-DSA-128-Simple',
        'type': 'DSA',
        'nist_level': 1,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 32,
        'sk_size_bytes': 64,
        'artifact_size_bytes': 7586,
        'gen_cycles': 2161363,
        'send_op_cycles': 38301068,
        'receive_op_cycles': 4308319
    },
    {
        'algorithm': 'SLH-DSA-192-Simple',
        'type': 'DSA',
        'nist_level': 3,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 48,
        'sk_size_bytes': 96,
        'artifact_size_bytes': 16224,
        'gen_cycles': 3145247,
        'send_op_cycles': 73131644,
        'receive_op_cycles': 7113137
    },
    {
        'algorithm': 'SLH-DSA-256-Simple',
        'type': 'DSA',
        'nist_level': 5,
        'math_problem': 'Stateless Hash',
        'pk_size_bytes': 64,
        'sk_size_bytes': 128,
        'artifact_size_bytes': 29792,
        'gen_cycles': 12096261,
        'send_op_cycles': 125984500,
        'receive_op_cycles': 12458602
    },

    {
        'algorithm': 'Falcon-512',
        'type': 'DSA',
        'nist_level': 1,
        'math_problem': 'Lattice (NTRU,SIS)',
        'pk_size_bytes': 897,
        'sk_size_bytes': 1281,
        'artifact_size_bytes': 618,
        'gen_cycles': 17579287,
        'send_op_cycles': 917699,
        'receive_op_cycles': 342801
    },
    {
        'algorithm': 'Falcon-1024',
        'type': 'DSA',
        'nist_level': 5,
        'math_problem': 'Lattice (NTRU,SIS)',
        'pk_size_bytes': 1793,
        'sk_size_bytes': 2305,
        'artifact_size_bytes': 1234,
        'gen_cycles': 46523261,
        'send_op_cycles': 1856561,
        'receive_op_cycles': 697558
    }
]
