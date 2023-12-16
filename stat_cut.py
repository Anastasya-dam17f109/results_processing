mass = [ [93.43,	69.26,	63.11,	40.53,	72.04,	52.31,	94.82,	75.58,	70.0,	14.35,	90.41,	70.09],
[95.88,	83.30	,68.86,	44.16,	61.09,	66.51,	95.93,	93.91,	93.33,	23.59,	90.53,	86.54],
[93.15,	80.88	,61.93,	49.68,	70.26,	50.15,	94.48,	91.36,	81.79,	38.72,	89.88,	82.74]

]
charact = 6
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

rec = []

for i in range(charact-1):

    rec.append(difs[i])


rec =  sum(rec, [])
rec.sort()

rec_ful.sort()
print(rec_ful)



print(max(rec), min(rec), rec[len(rec)//2], sum(rec)/len(rec))
print(max(rec_ful), min(rec_ful), rec_ful[len(rec_ful)//2], sum(rec_ful)/len(rec_ful))
