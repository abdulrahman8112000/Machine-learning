some_list=['a','b','c','d','b','e','n','n']


duplicates=[]
for item in some_list:
    if some_list.count(item)>1:
        duplicates.append(item)


for item in duplicates:
    if duplicates.count(item)>1:
        duplicates.remove(item)
print(duplicates)
