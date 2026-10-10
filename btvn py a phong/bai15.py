def khop(nop,lop):
    da_nop=nop & lop 
    ch_nop=lop - nop
    return(da_nop , ch_nop)
nop = {1, 2, 3}
lop = {1, 2, 3, 4, 5}
print(khop(nop,lop))
    