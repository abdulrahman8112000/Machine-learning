my_list=[1,2,3,4,5]


def only_odd(item):
    return item%2!=0

print(list(filter(only_odd,my_list)))
