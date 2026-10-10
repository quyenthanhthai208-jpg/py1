def xh(ds , x) :
    for i in ds:
        if i == x:
          return True
    return False
ds= [1,2,3,4,5,6,7,8,9,9,9,9]
x=int(input('nhap so can check: '))
print(xh(ds , x))
   

    