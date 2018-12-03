def get_common_chars(s1, s2):
    common = ''
    for i, c in enumerate(s1):
        if c == s2[i]:
            common += c
    return common

fh = open('input.txt', 'r')

values = []
for line in fh:
    line = line.strip()
    values.append(line)
fh.close()

max_common = ''
for j in values:
    for k in values:
        if j == k:
            continue
        common = get_common_chars(j, k)
        if len(common) > len(max_common):
            max_common = common

print(max_common)
