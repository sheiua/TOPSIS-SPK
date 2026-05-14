import numpy as np
import pandas as pd

# =========================
# METODE TOPSIS
# PEMILIHAN LOKASI COFFEE SHOP
# =========================

# =========================
# 1. Data Awal
# =========================

data = np.array([
    [7, 8, 9, 6, 8],  # A1
    [9, 9, 8, 8, 7],  # A2
    [6, 7, 7, 5, 9]   # A3
])

alternatif = [
    "A1 - Dekat Kampus",
    "A2 - Pusat Kota",
    "A3 - Perumahan"
]

kriteria = ["C1", "C2", "C3", "C4", "C5"]

# =========================
# 2. Bobot Kriteria
# =========================

bobot = np.array([
    0.25,  # C1
    0.20,  # C2
    0.20,  # C3
    0.15,  # C4
    0.20   # C5
])

# =========================
# 3. Jenis Kriteria
# 1 = Benefit
# 0 = Cost
# =========================

jenis = np.array([
    0,  # C1 = Cost
    1,  # C2 = Benefit
    1,  # C3 = Benefit
    0,  # C4 = Cost
    1   # C5 = Benefit
])

# =========================
# 4. Menampilkan Data Awal
# =========================

df_awal = pd.DataFrame(
    data,
    index=alternatif,
    columns=kriteria
)

print("\n==============================")
print("DATA AWAL")
print("==============================")
print(df_awal)

# =========================
# 5. Normalisasi Matriks (R)
# =========================

pembagi = np.sqrt((data ** 2).sum(axis=0))

R = data / pembagi

df_R = pd.DataFrame(
    R,
    index=alternatif,
    columns=kriteria
)

print("\n==============================")
print("MATRIKS NORMALISASI (R)")
print("==============================")
print(df_R.round(3))

# =========================
# 6. Normalisasi Terbobot (Y)
# =========================

Y = R * bobot

df_Y = pd.DataFrame(
    Y,
    index=alternatif,
    columns=kriteria
)

print("\n==============================")
print("MATRIKS NORMALISASI TERBOBOT (Y)")
print("==============================")
print(df_Y.round(3))

# =========================
# 7. Solusi Ideal Positif
# dan Negatif
# =========================

A_plus = np.where(
    jenis == 1,
    Y.max(axis=0),
    Y.min(axis=0)
)

A_min = np.where(
    jenis == 1,
    Y.min(axis=0),
    Y.max(axis=0)
)

print("\n==============================")
print("SOLUSI IDEAL POSITIF (A+)")
print("==============================")
print(pd.Series(A_plus, index=kriteria).round(3))

print("\n==============================")
print("SOLUSI IDEAL NEGATIF (A-)")
print("==============================")
print(pd.Series(A_min, index=kriteria).round(3))

# =========================
# 8. Menghitung Jarak
# =========================

D_plus = np.sqrt(
    ((Y - A_plus) ** 2).sum(axis=1)
)

D_min = np.sqrt(
    ((Y - A_min) ** 2).sum(axis=1)
)

df_D = pd.DataFrame({
    "D+": D_plus,
    "D-": D_min
}, index=alternatif)

print("\n==============================")
print("JARAK KE SOLUSI IDEAL")
print("==============================")
print(df_D.round(3))

# =========================
# 9. Menghitung
# Nilai Preferensi (Vi)
# =========================

V = D_min / (D_plus + D_min)

df_V = pd.DataFrame({
    "Nilai Preferensi": V
}, index=alternatif)

# =========================
# 10. Ranking
# =========================

df_V["Ranking"] = df_V[
    "Nilai Preferensi"
].rank(ascending=False)

hasil = df_V.sort_values(
    by="Nilai Preferensi",
    ascending=False
)

print("\n==============================")
print("HASIL RANKING")
print("==============================")
print(hasil.round(3))

# =========================
# 11. Kesimpulan
# =========================

terbaik = hasil.iloc[0]

print("\n==============================")
print("KESIMPULAN")
print("==============================")

print(
    f"Alternatif terbaik adalah "
    f"{terbaik.name} "
    f"dengan nilai preferensi "
    f"{terbaik['Nilai Preferensi']:.3f}"
)
