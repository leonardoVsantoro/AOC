data = [eval(_) for _ in open('input_20.txt').read().split('\n')]

def solve(inp, repeat):
    nums = list(enumerate(inp))
    new = nums[:]
    for _ in range(repeat):
        for p in nums:
            i = new.index(p)
            new.remove(p)
            target = (i + p[1]) % len(new)
            new.insert(target, p)
    zero = [n for _, n in new].index(0)
    return sum(new[(zero + i) % len(new)][1] for i in (1000, 2000, 3000))


print("Part 1:", solve(data, 1))
print("Part 2:", solve(map(lambda x: x * 811589153, data), 10))