import numpy as np
row = int(input())
data = []
for i in range(row):
    baris = list(map(int, input().split()))
    data.append(baris)
data = np.array(data)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == -1:
            kolom = i
            baris2 = j
            bawah = data[i+1:, j]
            if len(bawah) > 0:
                temp = np.max(bawah)
            else:
                temp = 0  # fallback kalau tidak ada elemen di bawah
            data[i][j] = temp
print(data)