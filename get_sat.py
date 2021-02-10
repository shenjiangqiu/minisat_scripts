#!/bin/python3
# %%
import re
folders = ["16_line_all_hit", "16_line_real", "one_lane_real"]
cnfs = [
    "b1904P1-8x8c6h5SAT.cnf",
    "b1904P3-8x8c11h0SAT.cnf",
    "eqsparcl10bpwtrc10.cnf",
    "eqspdtlf14bpwtrc14.cnf",
    "eqspwtrc16bparrc16.cnf",
    "Grain_no_init_ver1_out200_known_last104_0.cnf",
    "Haystacks-ext-12_c18.cnf",
    "hcp_bij16_16.cnf",
    "hcp_CP20_20.cnf",
    "hcp_CP24_24.cnf",
    "knight_20.cnf",
    "Mickey_out250_known_last146_0.cnf",
    "MM-23-2-2-2-2-3.cnf",
    "QuasiGroup-4-12_c18.cnf",
    "sha1r17m145ABCD.cnf",
    "sha1r17m72a.cnf",
    "size_4_4_4_i0418_r8.cnf",
    "size_5_5_5_i003_r12.cnf",
    "toughsat_28bits_0.cnf",
    "toughsat_30bits_0.cnf",
    "Trivium_no_init_out350_known_last142_1.cnf"
]

# %%
sat= re.compile(".*SATIS.*")


# %%

for cnf in cnfs:
    print(cnf)
    f = "."
    txt = open("{}/{}/result_{}.txt".format(f, cnf, cnf)).read()
    print("{}".format(sat.findall(txt)))
