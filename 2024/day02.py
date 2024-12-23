# filename = 'test_02.txt'
filename = 'input_02.txt'

data = [line.split() for line in open(filename).read().strip().split("\n")]
data = [[int(num) for num in row] for row in data]


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def is_safe(remaining_report, last = None,  order = None, can_remove = False):
    if len(remaining_report) == 1:
        return True
    else:
        increment = remaining_report[1] - remaining_report[0]
        if (sign(increment) == order or order == None) and (abs(increment)) <=3:
            return is_safe(remaining_report[1:], last =remaining_report[0], order = sign(increment), can_remove = can_remove)
        else:
            if can_remove:
                if last is None:
                    return is_safe(remaining_report[1:], order, can_remove = False)
                else:
                    return is_safe([last] + remaining_report[1:], order) or is_safe([last, remaining_report[0]] + remaining_report[2:], order)
            else:
                return False

part_1 = 0; part_2 = 0
for line in data:
    part_1 += is_safe(line, can_remove = False)
    part_2 += is_safe(line, can_remove = True)
print(f'part 1: {part_1}')
print(f'part 2: {part_2}')
