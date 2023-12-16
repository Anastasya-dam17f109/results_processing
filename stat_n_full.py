
mass = [
[0.723,	0.70,	0.61,	0.56,	0.950,	0.920,	0.81,	0.77,	0.326,	0.273,	0.66,	0.63,	0.697,	0.663],
[0.742,	0.72,	0.69,	0.69,	0.982,	0.980,	0.84,	0.80,	0.483,	0.482,	0.78,	0.76,	0.766,	0.759],
[0.726,	0.75,	0.71,	0.68,	0.972,	0.958,	0.87,	0.86,	0.559,	0.546,	0.77,	0.77,	0.782,	0.777],
[0.604,	0.58,	0.78,	0.76,	0.964,	0.938,	0.89,	0.86,	0.719,	0.669,	0.72,	0.69,	0.8,	0.767],
[0.795,	0.78,	0.63,	0.61,	0.988,	0.984,	0.82,	0.83,	0.351,	0.356,	0.79,	0.78,	0.739,	0.735],
[0.829,	0.78,	0.72,	0.75,	0.999,	0.993,	0.86,	0.82,	0.54,	0.531,	0.85,	0.83,	0.809,	0.795],
[0.804,	0.82,	0.74,	0.73,	0.989,	0.988,	0.89,	0.88,	0.627,	0.613,	0.84,	0.86,	0.829,	0.829],
[0.65	,0.64,	0.85,	0.87,	0.976,	0.978,	0.91,	0.86,	0.794,	0.746,	0.76,	0.78,	0.84,	0.826]


]

diffs_em = []
diffs_qtr = []
difs_full = []
models = 4
charact = 7
for i in range(charact):
    diffs_em.append([])
    diffs_qtr.append([])
    difs_full.append([])
    for j in range(models):
        if -mass[j][2*i+1] + mass[j][2*i] >=0:
            diffs_em[i].append(-mass[j][2*i+1] + mass[j][2*i])
        if -mass[j][2*i+1] + mass[ models+ j][2*i+1] >= 0:
            diffs_qtr[i].append(-mass[j][2*i+1] + mass[ models+j][2*i+1])
        if -mass[j][2*i+1] + mass[models+ j][2*i] >= 0:
            difs_full[i].append(-mass[j][2*i+1] + mass[ models+ j][2*i])



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
