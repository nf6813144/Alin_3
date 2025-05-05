# Import pustaka
import matplotlib.pyplot as plt
import numpy as np

# Nilai x dari -5 sampai 5
x = np.linspace(-5, 5, 400)

# Persamaan 1: 2x + 3y = 7 → y = (7 - 2x)/3
y_persamaan1 = (7 - 2 * x) / 3

# Persamaan 2: x - y = 1 → y = x - 1
y_persamaan2 = x - 1

# Buat grafik
plt.figure(figsize=(8, 6))
plt.plot(x, y_persamaan1, label='2x + 3y = 7', color='blue')
plt.plot(x, y_persamaan2, label='x - y = 1', color='green')

# Titik potong (solusi)
plt.plot(2, 1, 'ro')  # Titik merah di (2, 1)
plt.text(2.1, 1.1, 'Solusi (2, 1)', color='red')

# Hiasan grafik
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik Sistem Persamaan Linear (2 Variabel)')
plt.legend()
plt.axis('equal')

# Tampilkan grafik
plt.tight_layout()
plt.show()

# Import pustaka
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Buat grid nilai x dan y
x_nilai = np.linspace(-10, 10, 20)
y_nilai = np.linspace(-10, 10, 20)
x, y = np.meshgrid(x_nilai, y_nilai)

# Persamaan bidang:
# 1) 2x + 2y + z = 10   → z = 10 - 2x - 2y
# 2) 3x - y + 2z = 5    → z = (5 - 3x + y) / 2
# 3) -2x + 3y - z = 9   → z = -2x + 3y - 9

z_bidang1 = 10 - 2 * x - 2 * y
z_bidang2 = (5 - 3 * x + y) / 2
z_bidang3 = -2 * x + 3 * y - 9

# Buat grafik 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot bidang
ax.plot_surface(x, y, z_bidang1, alpha=0.5, color='blue')
ax.plot_surface(x, y, z_bidang2, alpha=0.5, color='green')
ax.plot_surface(x, y, z_bidang3, alpha=0.5, color='red')

# Hitung titik potong (solusi)
koefisien = np.array([[2, 2, 1], [3, -1, 2], [-2, 3, -1]])
hasil = np.array([10, 5, 9])
solusi = np.linalg.solve(koefisien, hasil)
x_solusi, y_solusi, z_solusi = solusi

# Tampilkan titik solusi
ax.scatter(x_solusi, y_solusi, z_solusi, color='black', s=50)
ax.text(x_solusi, y_solusi, z_solusi + 1,
        f'Solusi ({x_solusi:.2f}, {y_solusi:.2f}, {z_solusi:.2f})', color='black')

# Label sumbu
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Grafik 3D Sistem Persamaan Linear (3 Variabel)')

plt.tight_layout()
plt.show()

import sympy as sp
import matplotlib.pyplot as plt

# Mendefinisikan variabel simbolik
x, y = sp.symbols('x y')

# Menyusun sistem persamaan:
# Persamaan 1: 2x + 3y = 7
# Persamaan 2: x - y = 1
# Ditulis dalam bentuk aljabar biasa
persamaan1 = 2*x + 3*y - 7
persamaan2 = x - y - 1

# Menyelesaikan sistem persamaan
solusi = sp.solve((persamaan1, persamaan2), (x, y))

# Menampilkan hasil solusia
print("Solusi sistem persamaan:")
print(f"x = {solusi[x]}")
print(f"y = {solusi[y]}")

# Mengonversi solusi ke float untuk grafik
x_sol = float(solusi[x])
y_sol = float(solusi[y])

# Membuat data sumbu x secara manual dari -5 sampai 5
daftar_x = [i * 0.1 for i in range(-50, 51)]

# Menghitung y dari masing-masing persamaan
y1_data = [(7 - 2*nilai_x) / 3 for nilai_x in daftar_x]  # dari persamaan 1: y = (7 - 2x)/3
y2_data = [nilai_x - 1 for nilai_x in daftar_x]          # dari persamaan 2: y = x - 1

# Membuat grafik
plt.figure(figsize=(8, 6))
plt.plot(daftar_x, y1_data, label='2x + 3y = 7', color='blue')
plt.plot(daftar_x, y2_data, label='x - y = 1', color='green')

# Menampilkan titik solusi
plt.plot(x_sol, y_sol, 'ro')
plt.text(x_sol + 0.1, y_sol + 0.1, f'Solusi ({x_sol}, {y_sol})', color='red')

# Menambahkan garis sumbu, grid, dan label
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik Sistem Persamaan Linear 2 Variabel')
plt.legend()
plt.axis('equal')
plt.tight_layout()
plt.show()

import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Mendefinisikan variabel simbolik
x, y, z = sp.symbols('x y z')

# Menyusun sistem persamaan:
# Persamaan 1: 2x + 2y + z = 10
# Persamaan 2: 3x - y + 2z = 5
# Persamaan 3: -2x + 3y - z = 9

# Ditulis sebagai bentuk aljabar tanpa Eq
persamaan1 = 2*x + 2*y + z - 10
persamaan2 = 3*x - y + 2*z - 5
persamaan3 = -2*x + 3*y - z - 9

# Menyelesaikan sistem persamaan
solusi = sp.solve((persamaan1, persamaan2, persamaan3), (x, y, z))

# Menampilkan hasil solusi
print("Solusi sistem persamaan:")
print(f"x = {solusi[x]}")
print(f"y = {solusi[y]}")
print(f"z = {solusi[z]}")

# Mengonversi solusi ke float untuk grafik
x_sol = float(solusi[x])
y_sol = float(solusi[y])
z_sol = float(solusi[z])

# Membuat daftar nilai x dan y secara manual
daftar_x = [i for i in range(-10, 11)]
daftar_y = [i for i in range(-10, 11)]

# Menyiapkan data untuk ketiga bidang
x_data = []
y_data = []
z1_data = []
z2_data = []
z3_data = []

# Mengisi data untuk setiap kombinasi x dan y
for nilai_x in daftar_x:
    for nilai_y in daftar_y:
        x_data.append(nilai_x)
        y_data.append(nilai_y)
        z1_data.append(10 - 2*nilai_x - 2*nilai_y)         # dari persamaan 1
        z2_data.append((5 - 3*nilai_x + nilai_y) / 2)      # dari persamaan 2
        z3_data.append(-2*nilai_x + 3*nilai_y - 9)         # dari persamaan 3

# Membuat grafik 3D
fig = plt.figure(figsize=(10, 8))
sumbu = fig.add_subplot(111, projection='3d')

# Menampilkan ketiga bidang
sumbu.plot_trisurf(x_data, y_data, z1_data, alpha=0.5, color='blue', label='Bidang 1')
sumbu.plot_trisurf(x_data, y_data, z2_data, alpha=0.5, color='green', label='Bidang 2')
sumbu.plot_trisurf(x_data, y_data, z3_data, alpha=0.5, color='red', label='Bidang 3')

# Menampilkan titik solusi
sumbu.scatter(x_sol, y_sol, z_sol, color='black', s=50)
sumbu.text(x_sol, y_sol, z_sol + 1,
           f'Solusi ({x_sol:.2f}, {y_sol:.2f}, {z_sol:.2f})', color='black')

# Menambahkan label dan judul
sumbu.set_xlabel('X')
sumbu.set_ylabel('Y')
sumbu.set_zlabel('Z')
sumbu.set_title('Grafik 3D Sistem Persamaan Linear 3 Variabel')

plt.tight_layout()
plt.show()
