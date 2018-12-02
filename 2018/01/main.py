from collections import defaultdict
from itertools import cycle

freqs = defaultdict(int)
freqs[0] += 1

fh = open('input.txt', 'r')
values = []
for line in fh:
    line = line.strip()
    values.append(line)
fh.close()

first_repeated_found = False
current = 0
iters = 0
for v in cycle(values):
    if iters >= len(values) and first_repeated_found:
        # no need to continue
        break

    number = int(v)
    current += number

    freqs[current] += 1
    if freqs[current] == 2 and not first_repeated_found:
        first_repeated_found = True
        print ('first repeated : ' + str(current))

    iters += 1

    if iters == len(values):
        print ('entire cycle : ' + str(current))

