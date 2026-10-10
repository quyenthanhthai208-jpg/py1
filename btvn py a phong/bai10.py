def tra(ds) :
    kq=[]
    for i in ds:
        if i % 2==0 or i >10:
            kq.append(i)
    return kq
ds=[1,2 ,4,6,19,8,10,99,11,12]
print(tra(ds))