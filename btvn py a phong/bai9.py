def gop(dic1 , dic2) :
    kq= dic1.copy()
    for key,value in dic2.items():
        if key in kq:
            kq[key] = kq[key] + value
        else:
            kq[key] = value
    return kq
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
print(gop(dic1 , dic2))




