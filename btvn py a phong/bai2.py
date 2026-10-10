
def sl(tuple1 , x):
    dem = 0
    for s in tuple1:
        if s == x:
           dem += 1
    return dem
tuple1 =(1,2,3,4,5,1)
print(sl(tuple1 , 1))