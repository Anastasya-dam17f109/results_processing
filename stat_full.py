mass = [
[79.35,	78.87,	95.86,	97.39,	25.87,	24.96,	80.16],
[82.24,	80.64,	97.70,	97.02,	28.44,	31.33,	82.54],
[91.21,	82.32,	94.53,	98.70,	37.73,	47.56,	86.01],
[92.73,	83.44,	96.12,	98.54,	39.06,	54.38,	87.54],
[72.44,	94.97,	94.82,	97.68,	83.59,	44.11,	84.05],
[75.49,	97.29,	96.47,	97.43,	87.64,	49.17,	86.58],
[87.06,	91.11,	94.49,	98.35,	68.04,	52.73,	88.06],
[88.32,	96.11,	95.92,	98.24,	83.71,	61.74,	91.21],
[81.52,	94.07,	74.19,	99.07,	82.85,	35.16,	78.35],
[85.59,	96.47,	78.78,	99.22,	89.12,	41.97,	82.93],
[81.31,	94.69,	89.44,	97.87,	82.09,	46.03,	85.12],
[87.28,	95.85,	95.75,	97.69,	82.99,	60.58,	90.60]



]

diffs_em = []
diffs_qtr = []
difs_full = []
models = 3
charact = 7
for i in range(charact):
    diffs_em.append([])
    diffs_qtr.append([])
    difs_full.append([])
    for j in range(models):
        if -mass[2*j][i] + mass[2*models + 2*j][i] >=0:
            diffs_em[i].append(-mass[2*j][i] + mass[2*models + 2*j][i])
        if -mass[2 * j][i] + mass[2 * models + 2 * j+1][i] >= 0:
            difs_full[i].append(-mass[2 * j][i] + mass[2 * models + 2 * j+1][i])
        if -mass[2 * j][i] + mass[2 * j+1][i] >= 0:
            diffs_qtr[i].append(-mass[2 * j][i] + mass[ 2 * j+1][i])



all_difs = [diffs_em,
diffs_qtr,
difs_full]

all_difs_names = ["diffs_em",
"diffs_qtr",
"difs_full"]

for j in range(3):
    rec_ful = all_difs[j][charact - 1]
    pr = []
    rec = []
    print(all_difs_names[j])

    for i in range(charact - 1):
        if i % 2 == 0:
            rec.append(all_difs[j][i])
        else:
            pr.append(all_difs[j][i])
    rec = sum(rec, [])
    rec.sort()
    pr = sum(pr, [])
    pr.sort()
    rec_ful.sort()



    print(max(pr), min(pr), pr[len(pr) // 2], sum(pr) / len(pr))
    print(max(rec), min(rec), rec[len(rec) // 2], sum(rec) / len(rec))
    print(max(rec_ful), min(rec_ful), rec_ful[len(rec_ful) // 2], sum(rec_ful) / len(rec_ful))
