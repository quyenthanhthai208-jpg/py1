def dem_tan_suat(ds):
    tan_suat = {}
    for phan_tu in ds:
        if phan_tu in tan_suat:
            tan_suat[phan_tu] +=1
        else:
            tan_suat[phan_tu] = 1
    return tan_suat

ds = [1, 2, 2, 3, 3, 3]
print(dem_tan_suat(ds))   