'''
Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows:
for each number n that appears in l, there should be exactly one pair (n,r) in the list returned by the function, where r is is the number of repetitions of n in l.

the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

For instance:
>>> histogram([13,12,11,13,14,13,7,7,13,14,12])
[(11, 1), (7, 2), (12, 2), (14, 2), (13, 4)]

>>> histogram([7,12,11,13,7,11,13,14,12])
[(14, 1), (7, 2), (11, 2), (12, 2), (13, 2)]

>>> histogram([13,7,12,7,11,13,14,13,7,11,13,14,12,14,14,7])
[(11, 2), (12, 2), (7, 4), (13, 4), (14, 4)]
'''

valid_nums = []
rep_list = []
temp_list = []
final_list = []


def set_reps(l):
    for x in range(len(valid_nums)):
        reps = 0
        for y in range(len(l)):
            if valid_nums[x] == l[y]:
                reps = reps + 1
        rep_list[x] = reps


def histogram(l):
    [valid_nums.append(l[x]) for x in range(len(l)) if l[x] not in l[:x]]
    [rep_list.append(0) for x in range(len(valid_nums))]
    set_reps(l)
    [temp_list.append((rep_list[y], valid_nums[x])) for x in range(len(valid_nums)) for y in range(len(rep_list)) if x == y]
    [final_list.append((x[1], x[0])) for x in sorted(temp_list)]
    return final_list


l = [13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]
print(histogram(l))
