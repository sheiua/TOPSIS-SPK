# Metode TOPSIS - Pemilihan Lokasi Coffee Shop

Dokumen ini berisi implementasi metode **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** menggunakan bahasa pemrograman Python untuk menentukan lokasi coffee shop terbaik.

---

# Studi Kasus

Sebuah perusahaan ingin menentukan lokasi terbaik untuk membuka coffee shop berdasarkan beberapa kriteria penilaian.

## Alternatif Lokasi

- A1 = Dekat Kampus
- A2 = Pusat Kota
- A3 = Perumahan

---

# Kriteria Penilaian

| Kriteria | Jenis |
|---|---|
| Harga Sewa | Cost |
| Kepadatan Penduduk | Benefit |
| Akses Jalan | Benefit |
| Tingkat Kemacetan | Cost |
| Potensi Pasar | Benefit |

---

# Bobot Kriteria

| Kriteria | Bobot |
|---|---|
| Harga Sewa | 0.25 |
| Kepadatan Penduduk | 0.20 |
| Akses Jalan | 0.20 |
| Tingkat Kemacetan | 0.15 |
| Potensi Pasar | 0.20 |

---

# Data Alternatif

| Alternatif | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A1 | 7 | 8 | 9 | 6 | 8 |
| A2 | 9 | 9 | 8 | 8 | 7 |
| A3 | 6 | 7 | 7 | 5 | 9 |

Keterangan:
- C1 = Harga Sewa
- C2 = Kepadatan Penduduk
- C3 = Akses Jalan
- C4 = Tingkat Kemacetan
- C5 = Potensi Pasar

---

# Tahapan Metode TOPSIS

## 1. Membentuk Matriks Keputusan

Matriks keputusan dibentuk dari nilai setiap alternatif terhadap seluruh kriteria.

```text
A1 = [7, 8, 9, 6, 8]
A2 = [9, 9, 8, 8, 7]
A3 = [6, 7, 7, 5, 9]
```

---

## 2. Normalisasi Matriks

Rumus normalisasi:

```math
r_{ij} = \frac{x_{ij}}{\sqrt{\sum x_{ij}^2}}
```

Tujuan normalisasi adalah agar seluruh data memiliki skala yang sama.

---

## 3. Matriks Normalisasi Terbobot

Rumus:

```math
y_{ij} = w_j \times r_{ij}
```

Nilai hasil normalisasi dikalikan dengan bobot masing-masing kriteria.

---

## 4. Menentukan Solusi Ideal Positif dan Negatif

### Solusi Ideal Positif (A+)

Merupakan nilai terbaik dari setiap kriteria.

### Solusi Ideal Negatif (A-)

Merupakan nilai terburuk dari setiap kriteria.

---

## 5. Menghitung Jarak Solusi Ideal

### Jarak terhadap Solusi Ideal Positif

```math
D_i^+ = \sqrt{\sum (y_{ij} - y_j^+)^2}
```

### Jarak terhadap Solusi Ideal Negatif

```math
D_i^- = \sqrt{\sum (y_{ij} - y_j^-)^2}
```

---

## 6. Menghitung Nilai Preferensi

Rumus:

```math
V_i = \frac{D_i^-}{D_i^- + D_i^+}
```

Alternatif dengan nilai preferensi terbesar menjadi pilihan terbaik.

---

# Coding Python Metode TOPSIS

```python
# TOPSIS - Pemilihan Lokasi Coffee Shop

import numpy as np
import pandas as pd

# ------------------------------------------
# Data alternatif
# ------------------------------------------

data = np.array([
    [7, 8, 9, 6, 8],  # A1
    [9, 9, 8, 8, 7],  # A2
    [6, 7, 7, 5, 9]   # A3
])

# ------------------------------------------
# Nama alternatif
# ------------------------------------------

alternatif = [
    "A1 - Dekat Kampus",
    "A2 - Pusat Kota",
    "A3 - Perumahan"
]

# ------------------------------------------
# Bobot kriteria
# ------------------------------------------

bobot = np.array([
    0.25,
    0.20,
    0.20,
    0.15,
    0.20
])

# ------------------------------------------
# Jenis kriteria
# 1 = Benefit
# 0 = Cost
# ------------------------------------------

kriteria = np.array([
    0,  # Harga Sewa
    1,  # Kepadatan Penduduk
    1,  # Akses Jalan
    0,  # Tingkat Kemacetan
    1   # Potensi Pasar
])

# ------------------------------------------
# Normalisasi Matriks
# ------------------------------------------

norm = data / np.sqrt((data**2).sum(axis=0))

print("=== Matriks Normalisasi ===")
print(norm)

# ------------------------------------------
# Matriks Ternormalisasi Terbobot
# ------------------------------------------

y = norm * bobot

print("\n=== Matriks Ternormalisasi Terbobot ===")
print(y)

# ------------------------------------------
# Solusi Ideal Positif dan Negatif
# ------------------------------------------

ideal_pos = np.where(
    kriteria == 1,
    y.max(axis=0),
    y.min(axis=0)
)

ideal_neg = np.where(
    kriteria == 1,
    y.min(axis=0),
    y.max(axis=0)
)

print("\n=== Solusi Ideal Positif ===")
print(ideal_pos)

print("\n=== Solusi Ideal Negatif ===")
print(ideal_neg)

# ------------------------------------------
# Menghitung Jarak
# ------------------------------------------

d_pos = np.sqrt(((y - ideal_pos)**2).sum(axis=1))

d_neg = np.sqrt(((y - ideal_neg)**2).sum(axis=1))

print("\n=== Jarak Positif ===")
print(d_pos)

print("\n=== Jarak Negatif ===")
print(d_neg)

# ------------------------------------------
# Menghitung Nilai Preferensi
# ------------------------------------------

v = d_neg / (d_pos + d_neg)

# ------------------------------------------
# Ranking
# ------------------------------------------

hasil = pd.DataFrame({
    "Alternatif": alternatif,
    "Nilai Preferensi": v
})

hasil = hasil.sort_values(
    by="Nilai Preferensi",
    ascending=False
)

print("\n=== Hasil Ranking ===")
print(hasil)

# ------------------------------------------
# Kesimpulan
# ------------------------------------------

terbaik = hasil.iloc[0]

print("\n=== Kesimpulan ===")
print(
    f"Lokasi terbaik adalah "
    f"{terbaik['Alternatif']} "
    f"dengan nilai preferensi "
    f"{terbaik['Nilai Preferensi']:.4f}"
)
```

---

# Hasil Ranking

| Ranking | Alternatif | Keterangan |
|---|---|---|
| 1 | A1 - Dekat Kampus | Lokasi terbaik |
| 2 | A3 - Perumahan | Alternatif kedua |
| 3 | A2 - Pusat Kota | Alternatif terakhir |

---

# Kesimpulan

Berdasarkan metode **TOPSIS**, lokasi terbaik untuk membuka coffee shop adalah:

> **A1 - Dekat Kampus**

Karena memiliki nilai preferensi tertinggi dibandingkan alternatif lainnya.
