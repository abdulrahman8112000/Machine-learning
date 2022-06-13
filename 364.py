simple_dict={
    'a':1,
    'b':2
}


my_dict={k:v for k,v in simple_dict.items()}
print(my_dict)


my_dict2={number:number*2 for number in [1,2,3]}
print(my_dict2)