a=11

def parent():
    
    def child():
        a=13
        return a
    return a

print(parent())