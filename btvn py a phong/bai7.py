def lon_nhat(ds):
    sln=0
    for i in ds:
        if i> sln:
            sln=i
    return sln
ds=[1,99,109,1999,88]
print(lon_nhat(ds))