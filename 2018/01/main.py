from collections import defaultdict
from itertools import cycle

freqs = defaultdict(int)
freqs[0] += 1

def extract_sign_and_number(line):
    sign, number = line[0:1], line[1:]
    return sign, int(number)

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

    sign, number = extract_sign_and_number(v)
    if sign == '+':
        current += number
    else:
        current -= number

    freqs[current] += 1
    if freqs[current] == 2 and not first_repeated_found:
        first_repeated_found = True
        print ('first repeated : ' + str(current))

    iters += 1

    if iters == len(values):
        print ('entire cycle : ' + str(current))

