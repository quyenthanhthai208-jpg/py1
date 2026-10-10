def dtb(ds):
    tong=0
    for i in ds:
        tong += i
    return tong / len(ds)
def xep_loai(diem):
    if diem >= 8:
        return 'Gioi'
    elif diem >= 6.5:
        return 'Kha'
    elif diem >= 5:
        return 'Trung Binh'
    else:
        return 'Yeu'
def phan_tich(sv):
    kq={}
    for ten, ds_diem in sv.items():
        tb=dtb(ds_diem)
        kq[ten] = xep_loai(tb)
    return kq
sinh_vien = {
    'An': [8, 9, 7],
    'Binh': [5, 6, 4],
    'Chi': [9, 10, 9]
}
print(phan_tich(sinh_vien))

    
    