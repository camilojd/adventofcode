from collections import defaultdict

def get_counts(ids):
    from collections import defaultdict

    ret = defaultdict(int)
    for c in ids:
        ret[c] += 1

    return {v:True for k, v in ret.items() if v in (2,3)}

amount_2 = 0
amount_3 = 0
fh = open('input.txt', 'r')

for line in fh:
    line = line.strip()
    counts = get_counts(line)
    amount_2 += 1 if 2 in counts else 0
    amount_3 += 1 if 3 in counts else 0
fh.close()

print (amount_2 * amount_3)
