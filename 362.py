from functools import reduce


my_list=[3,4,56]

def accumulator(acc,item):
    return acc+item

print(reduce(accumulator,my_list,4))
