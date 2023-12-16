
mass = [[73.58,	42.43	,61.16,	86.58	,87.47,	68.12	,38.18,	37.61	,69.73,	58.11]
[62.41,	52.56	,63.96,	86.19	,87.55,	82.36	,34.04,	22.65	,65.65,	63.55]
[64.52,	37.64,	65.97,	79.08	,83.17,	74.94,	34.47,	63.82	,65.67,	60.55 ]
]
charact = 5
rows=3
difs = []
for i in range(charact):
    difs.append([])
    for j in range(rows):
        buf = mass[j][ i*2] - mass[j][ i*2+1]
        if buf >=0:
            difs[i].append(buf)


print(difs)
rec_ful = difs[charact-1]
pr = []
rec = []

for i in range(charact-1):
    if i %2 ==0:
        rec.append(difs[i])
    else:
        pr.append(difs[i])

rec =  sum(rec, [])
rec.sort()
pr =  sum(pr, [])
pr.sort()
rec_ful.sort()
print(rec_ful)
cr2 = difs[1]
print(cr2)
cr2.sort()

print(max(pr), min(pr), pr[len(pr)//2], sum(pr)/len(pr))
print(max(rec), min(rec), rec[len(rec)//2], sum(rec)/len(rec))
print(max(rec_ful), min(rec_ful), rec_ful[len(rec_ful)//2], sum(rec_ful)/len(rec_ful))
print(max(cr2), min(cr2), cr2[len(cr2)//2], sum(cr2)/len(cr2))