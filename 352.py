def highest_even(li):
    heven=li[0]
    for item in li:
        if (item%2==0)and(item>=heven):
            heven=item
    return heven

print(highest_even([423,143,534,67,5768,679,6,8567,563,3]))