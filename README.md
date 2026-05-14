# Sistem Penunjang Keputusan  
## Metode TOPSIS – Pemilihan Lokasi Usaha Coffee Shop

---

# Identitas

- **Nama:** Sheina Azima  
- **NPM:** 2255061020  
- **Mata Kuliah:** Sistem Penunjang Keputusan  

---

# Pendahuluan

Penelitian ini bertujuan untuk menentukan lokasi terbaik dalam membuka usaha coffee shop menggunakan metode **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**.

Metode TOPSIS digunakan karena mampu memberikan solusi terbaik berdasarkan kedekatan terhadap solusi ideal positif dan jarak terhadap solusi ideal negatif.

---

# Tahap 1 – Identifikasi Masalah

## Tujuan

Menentukan lokasi terbaik dari beberapa alternatif lokasi usaha coffee shop.

---

# Tahap 2 – Kriteria

| Kode | Kriteria | Jenis |
|---|---|---|
| C1 | Biaya Sewa | Cost |
| C2 | Kepadatan Penduduk | Benefit |
| C3 | Aksesibilitas | Benefit |
| C4 | Kompetitor | Cost |
| C5 | Keamanan | Benefit |

---

# Tahap 3 – Bobot

| Kriteria | Bobot |
|---|---|
| C1 | 0.25 |
| C2 | 0.20 |
| C3 | 0.20 |
| C4 | 0.15 |
| C5 | 0.20 |

---

# Tahap 4 – Normalisasi Bobot

Total bobot:

```text
0.25 + 0.20 + 0.20 + 0.15 + 0.20 = 1
```

Karena total bobot sudah bernilai 1, maka bobot tidak perlu dinormalisasi kembali.

---

# Tahap 5 – Alternatif

| Kode | Alternatif |
|---|---|
| A1 | Dekat Kampus |
| A2 | Pusat Kota |
| A3 | Perumahan |

---

# Tahap 6 – Matriks Keputusan

| Alternatif | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A1 | 7 | 8 | 9 | 6 | 8 |
| A2 | 9 | 9 | 8 | 8 | 7 |
| A3 | 6 | 7 | 7 | 5 | 9 |

---

# Tahap 7 – Normalisasi Matriks

Rumus normalisasi:

```math
r_{ij} = \frac{x_{ij}}{\sqrt{\sum x_{ij}^2}}
```

---

# Tahap 8 – Matriks Normalisasi (R)

| Alternatif | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A1 | 0.543 | 0.574 | 0.646 | 0.537 | 0.574 |
| A2 | 0.699 | 0.646 | 0.574 | 0.716 | 0.503 |
| A3 | 0.466 | 0.503 | 0.503 | 0.447 | 0.646 |

---

# Tahap 9 – Matriks Normalisasi Terbobot (Y)

Rumus:

```math
y_{ij} = w_j \times r_{ij}
```

| Alternatif | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A1 | 0.136 | 0.115 | 0.129 | 0.081 | 0.115 |
| A2 | 0.175 | 0.129 | 0.115 | 0.107 | 0.101 |
| A3 | 0.117 | 0.101 | 0.101 | 0.067 | 0.129 |

---

# Tahap 10 – Solusi Ideal

## Solusi Ideal Positif (A+)

| Kriteria | Nilai |
|---|---|
| C1 (Cost) | 0.117 |
| C2 (Benefit) | 0.129 |
| C3 (Benefit) | 0.129 |
| C4 (Cost) | 0.067 |
| C5 (Benefit) | 0.129 |

---

## Solusi Ideal Negatif (A-)

| Kriteria | Nilai |
|---|---|
| C1 (Cost) | 0.175 |
| C2 (Benefit) | 0.101 |
| C3 (Benefit) | 0.101 |
| C4 (Cost) | 0.107 |
| C5 (Benefit) | 0.101 |

---

# Tahap 11 – Menghitung Jarak Solusi Ideal

## Jarak ke Solusi Ideal Positif (D+)

Rumus:

```math
D_i^+ = \sqrt{\sum (Y_i - A^+)^2}
```

| Alternatif | D⁺ |
|---|---|
| A1 | 0.027 |
| A2 | 0.072 |
| A3 | 0.036 |

---

## Jarak ke Solusi Ideal Negatif (D-)

Rumus:

```math
D_i^- = \sqrt{\sum (Y_i - A^-)^2}
```

| Alternatif | D⁻ |
|---|---|
| A1 | 0.051 |
| A2 | 0.026 |
| A3 | 0.054 |

---

# Tahap 12 – Menghitung Nilai Preferensi

Rumus:

```math
V_i = \frac{D^-}{D^+ + D^-}
```

## Perhitungan

### A1 – Dekat Kampus

```math
V_1 = \frac{0.051}{0.027 + 0.051} = 0.654
```

### A2 – Pusat Kota

```math
V_2 = \frac{0.026}{0.072 + 0.026} = 0.265
```

### A3 – Perumahan

```math
V_3 = \frac{0.054}{0.036 + 0.054} = 0.600
```

---

# Hasil Ranking

| Alternatif | Nilai Preferensi (Vi) | Ranking |
|---|---|---|
| A1 | 0.654 | 1 |
| A3 | 0.600 | 2 |
| A2 | 0.265 | 3 |

---

# Kode Python

```python
import numpy as np
import pandas as pd

# =========================
# 1. Data Awal
# =========================
data = np.array([
    [7, 8, 9, 6, 8],  # A1
    [9, 9, 8, 8, 7],  # A2
    [6, 7, 7, 5, 9]   # A3
])

alternatif = ["A1 - Dekat Kampus", "A2 - Pusat Kota", "A3 - Perumahan"]
kriteria = ["C1", "C2", "C3", "C4", "C5"]

# Bobot
bobot = np.array([0.25, 0.20, 0.20, 0.15, 0.20])

# Jenis kriteria: 1 = Benefit, 0 = Cost
jenis = np.array([0, 1, 1, 0, 1])

# =========================
# 2. Normalisasi (R)
# =========================
pembagi = np.sqrt((data**2).sum(axis=0))
R = data / pembagi

df_R = pd.DataFrame(R, index=alternatif, columns=kriteria)

print("\n=== Matriks Normalisasi (R) ===")
print(df_R.round(3))

# =========================
# 3. Normalisasi Terbobot (Y)
# =========================
Y = R * bobot

df_Y = pd.DataFrame(Y, index=alternatif, columns=kriteria)

print("\n=== Matriks Normalisasi Terbobot (Y) ===")
print(df_Y.round(3))

# =========================
# 4. Solusi Ideal
# =========================
A_plus = np.where(jenis == 1, Y.max(axis=0), Y.min(axis=0))
A_min = np.where(jenis == 1, Y.min(axis=0), Y.max(axis=0))

print("\n=== Solusi Ideal Positif (A+) ===")
print(pd.Series(A_plus, index=kriteria).round(3))

print("\n=== Solusi Ideal Negatif (A-) ===")
print(pd.Series(A_min, index=kriteria).round(3))

# =========================
# 5. Jarak ke Solusi Ideal
# =========================
D_plus = np.sqrt(((Y - A_plus)**2).sum(axis=1))
D_min = np.sqrt(((Y - A_min)**2).sum(axis=1))

df_D = pd.DataFrame({
    "D+": D_plus,
    "D-": D_min
}, index=alternatif)

print("\n=== Jarak ke Solusi Ideal ===")
print(df_D.round(3))

# =========================
# 6. Nilai Preferensi (Vi)
# =========================
V = D_min / (D_plus + D_min)

df_V = pd.DataFrame({
    "Nilai Preferensi": V
}, index=alternatif)

# Ranking
df_V["Ranking"] = df_V["Nilai Preferensi"].rank(ascending=False)

print("\n=== Nilai Preferensi & Ranking ===")
print(df_V.sort_values(by="Nilai Preferensi", ascending=False).round(3))
```

---

# Kesimpulan

## Pembahasan Hasil (Analisis Kenapa A1 Unggul)

Berdasarkan hasil perhitungan metode TOPSIS, alternatif **A1 (Dekat Kampus)** memperoleh nilai preferensi tertinggi sehingga menjadi pilihan terbaik.

Hal ini dapat dijelaskan sebagai berikut:

### 1. Keseimbangan Antar Kriteria

A1 memiliki nilai cukup tinggi pada hampir semua kriteria benefit seperti:

- Kepadatan penduduk (C2)
- Aksesibilitas (C3)
- Keamanan (C5)

Hal ini menunjukkan bahwa lokasi dekat kampus memiliki potensi pasar besar dan mudah dijangkau pelanggan.

---

### 2. Nilai Unggul pada Aksesibilitas (C3)

A1 memiliki nilai tertinggi pada kriteria aksesibilitas.

Faktor ini sangat penting dalam bisnis coffee shop karena mempengaruhi kemudahan pelanggan untuk datang ke lokasi usaha.

---

### 3. Kompetitor Tidak Terlalu Tinggi

Pada kriteria cost yaitu kompetitor (C4), nilai A1 tidak terlalu besar dibandingkan A2.

Hal ini menunjukkan tingkat persaingan masih relatif terkendali.

---

### 4. Biaya Masih Kompetitif

Walaupun bukan yang paling rendah, biaya sewa (C1) pada A1 masih lebih baik dibandingkan A2 sehingga lebih efisien dari sisi pengeluaran usaha.

---

### 5. Perbandingan dengan Alternatif Lain

#### A2 – Pusat Kota
- Unggul di beberapa aspek
- Namun memiliki biaya sewa dan tingkat kompetitor yang tinggi

#### A3 – Perumahan
- Memiliki biaya lebih rendah dan keamanan tinggi
- Tetapi kalah pada kepadatan penduduk dan aksesibilitas

---

# Hasil Akhir

Berdasarkan metode TOPSIS, lokasi terbaik untuk membuka usaha coffee shop adalah:

> **A1 – Dekat Kampus**

Karena memiliki nilai preferensi tertinggi yaitu:

```text
0.654
```
