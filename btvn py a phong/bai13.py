def gop(ds):
    kq= {}
    for id,value in ds:
        if id in kq:
            kq[id].append(value)
        else:
            kq[id] = [value]
    return kq
ds = [(1, 'a'), (2, 'b'), (1, 'c')]
print(gop(ds))



