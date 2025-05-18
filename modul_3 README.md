# Mengimpor library yang dibutuhkan
import numpy as np
from sympy import symbols, Eq, solve

# ---------------------------------------------
# Bagian 1: Menyelesaikan Sistem Persamaan 1 (2 variabel) dengan SymPy
# ---------------------------------------------

# Mendefinisikan variabel simbolik
x, y, z = symbols('x y z')

# Mendefinisikan persamaan
eq1 = Eq(2 * x + 3 * y, 1)
eq2 = Eq(4 * x - y, 7)

# Menyelesaikan sistem persamaan
solusi1 = solve((eq1, eq2), (x, y))
print("Judul: Solusi Sistem 1 (2 variabel):")
print(f"x = {solusi1[x]}, y = {solusi1[y]}")
print()

# ---------------------------------------------
# Bagian 2: Menyelesaikan Sistem Persamaan 2 (3 variabel) dengan SymPy
# ---------------------------------------------

# Mendefinisikan persamaan sistem 3 variabel
eq3 = Eq(x + 2 * y + z, 10)
eq4 = Eq(3 * x - y + 2 * z, 2)
eq5 = Eq(2 * x + 3 * y - z, 9)

# Menyelesaikan sistem
solusi2 = solve((eq3, eq4, eq5), (x, y, z), dict=True)

# Menampilkan hasil
print("Judul: Solusi Sistem 2 (3 variabel):")
if solusi2:
    for sol in solusi2:
        print(sol)
else:
    print("Sistem tidak memiliki solusi.")
print()

# ---------------------------------------------
# Bagian 3: Menyelesaikan Sistem Persamaan 1 (2 variabel) dengan NumPy
# ---------------------------------------------

# Matriks koefisien dan konstanta
A1 = np.array([[2, 3], [4, -1]])
B1 = np.array([1, 7])

# Menyelesaikan sistem
solusi_numpy1 = np.linalg.solve(A1, B1)
print("Judul: Solusi Sistem (2 variabel) dengan NumPy:")
print(f"x = {solusi_numpy1[0]}, y = {solusi_numpy1[1]}")
print()

# ---------------------------------------------
# Bagian 4: Menyelesaikan Sistem Persamaan 2 (3 variabel) dengan NumPy
# ---------------------------------------------

# Matriks koefisien dan konstanta
A2 = np.array([[1, 2, 1], [3, -1, 2], [2, 3, -1]])
B2 = np.array([10, 2, 9])

# Menyelesaikan sistem
solusi_numpy2 = np.linalg.solve(A2, B2)
print("Judul: Solusi Sistem (3 variabel) dengan NumPy:")
print(f"x = {solusi_numpy2[0]}, y = {solusi_numpy2[1]}, z = {solusi_numpy2[2]}")
