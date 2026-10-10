def xoa_trung(ds):
    kq=[]
    for a in ds:
        if a not in kq:
            kq.append(a)
    return kq
ds=[1,2,3,4,5,6,7,8,8,8,8,9]
print(xoa_trung(ds))