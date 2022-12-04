In [23]: with open('input.txt') as f:
    ...:     input = f.read().strip()
    ...:
    ...:

In [24]: chunks = input.split('\n\n')

In [25]: splitchunks = [chunk.split('\n') for chunk in chunks]

In [26]: sums = [sum(int(x) for x in splitchunk) for splitchunk in splitchunks]

In [27]: maxcals = max(sums)

In [28]: maxelf = sums.index(maxcals)

In [29]: maxelf
Out[29]: 28

In [30]: sums[28]
Out[30]: 71300

In [31]: sorted(sums, reverse=True)[:3]
Out[31]: [71300, 69249, 69142]

In [32]: sum(sorted(sums, reverse=True)[:3])
Out[32]: 209691
