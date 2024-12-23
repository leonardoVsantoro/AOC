filename = 'input_22.txt'
# filename = 'test_22.txt'
def evolve(num, epocs):
    num = ((num * 64)^ num)  % 16777216
    num = ((num // 32) ^ num) % 16777216
    num  = ((num * 2048) ^ num ) % 16777216
    if epocs ==1:
        return num
    else:
        return evolve(num, epocs-1)

data = list(map(int, open(filename).read().splitlines()))

p1 = sum([evolve(x,2000) for x in data])
print(f'Part 1 : {p1}')

from collections import defaultdict
seq_to_gain = defaultdict(int)
for bp in data:
    seen = set()
    prices = [bp % 10]
    newprice = bp
    for i in range(1, 2000):
        newprice = evolve(newprice, 1)
        prices.append(newprice % 10)
        if len(prices) == 5:
            a,b,c,d,e = prices
            prices.pop(0)                    
            seq = (b-a,c-b,d-c,e-d)
            if seq in seen: continue
            seen.add(seq)
            seq_to_gain[seq] += e

p2 = max(seq_to_gain.values())
print(f'Part 2 : {p2}')
