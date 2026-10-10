
def tong(ds):
    tong =0
    for so in ds:
        tong += so
    return tong
so = [1,2,3,4,5]
so2 = [3,6,9,12]
print(tong(so + so2))