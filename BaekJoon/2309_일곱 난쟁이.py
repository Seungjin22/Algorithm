import sys
sys.stdin = open('2309_input.txt')


def Comb(d, rst):
    if len(rst) == 7 and sum(rst) == 100:
        rst.sort()
        fin.append(rst)
        return
    for i in range(d, len(dwarfs)):
        Comb(i + 1, rst + [dwarfs[i]])


dwarfs = []
fin = []
for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()
dwarfs.reverse()
Comb(0, [])

for f in fin[0]:
    print(f)

