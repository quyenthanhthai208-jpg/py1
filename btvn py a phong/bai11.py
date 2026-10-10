def vi_tri(ds):
    kq = {}
    for i in range(len(ds)):
        so = ds[i]
        if so in kq:
            kq[so].append(i)
        else:
            kq[so] = [i]
    return kq
ds = [5, 3, 5, 7, 3, 5]
print(vi_tri(ds))   