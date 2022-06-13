my_list=['a','b','c','d','b','n','d','n']

duplicates={char for char in my_list if my_list.count(char)>1}

print(duplicates)