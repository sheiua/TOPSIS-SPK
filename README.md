# Metode Profile Matching  
## Pemilihan Team Leader Terbaik

---

# Identitas

- Nama: Sheina Azima  
- NPM: 2255061020  
- Mata Kuliah: Sistem Penunjang Keputusan  

---

# Studi Kasus

Sebuah perusahaan ingin memilih karyawan terbaik untuk dipromosikan menjadi **Team Leader** menggunakan metode **Profile Matching**.

---

# Kriteria Penilaian

Kriteria yang digunakan:

- Komunikasi
- Kepemimpinan
- Disiplin
- Kerja Sama Tim

## Pembagian Faktor

### Core Factor (CF)
- Komunikasi
- Kepemimpinan

### Secondary Factor (SF)
- Disiplin
- Kerja Sama Tim

| Kriteria | Jenis | Target |
|---|---|---|
| Komunikasi | Core Factor | 5 |
| Kepemimpinan | Core Factor | 5 |
| Disiplin | Secondary Factor | 4 |
| Kerja Sama Tim | Secondary Factor | 4 |

---

# Data Kandidat

| Kandidat | Komunikasi | Kepemimpinan | Disiplin | Kerja Sama Tim |
|---|---|---|---|---|
| Andi | 4 | 5 | 4 | 3 |
| Budi | 5 | 4 | 5 | 4 |
| Citra | 3 | 5 | 4 | 5 |
| Dinda | 5 | 5 | 3 | 4 |

---

# Tahapan Metode Profile Matching

## 1. Identifikasi Masalah

Perusahaan ingin menentukan kandidat terbaik yang layak dipromosikan menjadi Team Leader.

---

## 2. Menentukan Kriteria dan Subkriteria

Kriteria:
- Komunikasi
- Kepemimpinan
- Disiplin
- Kerja Sama Tim

---

## 3. Menentukan Bobot

- Core Factor = 60%
- Secondary Factor = 40%

---

## 4. Penentuan Nilai Target

| Kriteria | Target |
|---|---|
| Komunikasi | 5 |
| Kepemimpinan | 5 |
| Disiplin | 4 |
| Kerja Sama Tim | 4 |

---

# Perhitungan GAP

Rumus:

```math
GAP = Nilai\ Kandidat - Nilai\ Target
```

## Tabel GAP

| Kandidat | Komunikasi | Kepemimpinan | Disiplin | Kerja Sama Tim |
|---|---|---|---|---|
| Andi | -1 | 0 | 0 | -1 |
| Budi | 0 | -1 | 1 | 0 |
| Citra | -2 | 0 | 0 | 1 |
| Dinda | 0 | 0 | -1 | 0 |

---

# Konversi GAP ke Bobot

## Tabel Bobot GAP

| Selisih GAP | Bobot |
|---|---|
| 0 | 5 |
| 1 | 4.5 |
| -1 | 4 |
| 2 | 3.5 |
| -2 | 3 |

---

## Hasil Konversi GAP

| Kandidat | Komunikasi | Kepemimpinan | Disiplin | Kerja Sama Tim |
|---|---|---|---|---|
| Andi | 4 | 5 | 5 | 4 |
| Budi | 5 | 4 | 4.5 | 5 |
| Citra | 3 | 5 | 5 | 4.5 |
| Dinda | 5 | 5 | 4 | 5 |

---

# Perhitungan NCF dan NSF

## Rumus Core Factor

```math
NCF = \frac{Jumlah\ Nilai\ Core\ Factor}{Jumlah\ Item\ Core\ Factor}
```

## Rumus Secondary Factor

```math
NSF = \frac{Jumlah\ Nilai\ Secondary\ Factor}{Jumlah\ Item\ Secondary\ Factor}
```

---

## Hasil Perhitungan

### Andi

```text
NCF = (4 + 5) / 2 = 4.5
NSF = (5 + 4) / 2 = 4.5
```

### Budi

```text
NCF = (5 + 4) / 2 = 4.5
NSF = (4.5 + 5) / 2 = 4.75
```

### Citra

```text
NCF = (3 + 5) / 2 = 4
NSF = (5 + 4.5) / 2 = 4.75
```

### Dinda

```text
NCF = (5 + 5) / 2 = 5
NSF = (4 + 5) / 2 = 4.5
```

---

# Perhitungan Nilai Akhir

Rumus:

```math
Nilai\ Akhir = (60\% \times NCF) + (40\% \times NSF)
```

## Hasil Nilai Akhir

| Kandidat | NCF | NSF | Nilai Akhir |
|---|---|---|---|
| Andi | 4.5 | 4.5 | 4.5 |
| Budi | 4.5 | 4.75 | 4.6 |
| Citra | 4 | 4.75 | 4.3 |
| Dinda | 5 | 4.5 | 4.8 |

---

# Perangkingan

| Ranking | Kandidat | Nilai |
|---|---|---|
| 1 | Dinda | 4.8 |
| 2 | Budi | 4.6 |
| 3 | Andi | 4.5 |
| 4 | Citra | 4.3 |

---

# Kesimpulan

Berdasarkan metode **Profile Matching**, kandidat terbaik untuk dipromosikan menjadi **Team Leader** adalah:

> **Dinda** dengan nilai akhir sebesar **4.8**

---

# Coding Python Metode Profile Matching

```python
import pandas as pd

# ==========================================
# METODE PROFILE MATCHING
# PEMILIHAN TEAM LEADER TERBAIK
# ==========================================

# ------------------------------------------
# 1. Data Kandidat
# ------------------------------------------

data = {
    'Kandidat': ['Andi', 'Budi', 'Citra', 'Dinda'],
    'Komunikasi': [4, 5, 3, 5],
    'Kepemimpinan': [5, 4, 5, 5],
    'Disiplin': [4, 5, 4, 3],
    'Kerja Sama Tim': [3, 4, 5, 4]
}

# Membuat DataFrame
df = pd.DataFrame(data)

print("================================")
print("DATA KANDIDAT")
print("================================")
print(df)

# ------------------------------------------
# 2. Nilai Target
# ------------------------------------------

target = {
    'Komunikasi': 5,
    'Kepemimpinan': 5,
    'Disiplin': 4,
    'Kerja Sama Tim': 4
}

print("\n================================")
print("NILAI TARGET")
print("================================")
print(target)

# ------------------------------------------
# 3. Menghitung GAP
# ------------------------------------------

gap_df = df.copy()

for kolom in target:
    gap_df[kolom] = df[kolom] - target[kolom]

print("\n================================")
print("TABEL GAP")
print("================================")
print(gap_df)

# ------------------------------------------
# 4. Konversi GAP ke Bobot
# ------------------------------------------

def bobot_gap(gap):

    konversi = {
        0: 5,
        1: 4.5,
        -1: 4,
        2: 3.5,
        -2: 3
    }

    return konversi.get(gap, 0)

bobot_df = gap_df.copy()

for kolom in target:
    bobot_df[kolom] = gap_df[kolom].apply(bobot_gap)

print("\n================================")
print("HASIL KONVERSI GAP")
print("================================")
print(bobot_df)

# ------------------------------------------
# 5. Menentukan Core dan Secondary Factor
# ------------------------------------------

core_factor = ['Komunikasi', 'Kepemimpinan']

secondary_factor = ['Disiplin', 'Kerja Sama Tim']

# ------------------------------------------
# 6. Menghitung NCF dan NSF
# ------------------------------------------

# NCF = rata-rata Core Factor
bobot_df['NCF'] = bobot_df[core_factor].mean(axis=1)

# NSF = rata-rata Secondary Factor
bobot_df['NSF'] = bobot_df[secondary_factor].mean(axis=1)

print("\n================================")
print("NILAI NCF DAN NSF")
print("================================")
print(bobot_df[['Kandidat', 'NCF', 'NSF']])

# ------------------------------------------
# 7. Menghitung Nilai Akhir
# ------------------------------------------

# Rumus:
# Nilai Akhir = (60% × NCF) + (40% × NSF)

bobot_df['Nilai Akhir'] = (
    (0.6 * bobot_df['NCF']) +
    (0.4 * bobot_df['NSF'])
)

print("\n================================")
print("NILAI AKHIR")
print("================================")
print(bobot_df[['Kandidat', 'Nilai Akhir']])

# ------------------------------------------
# 8. Melakukan Ranking
# ------------------------------------------

ranking = bobot_df[['Kandidat', 'Nilai Akhir']]

ranking = ranking.sort_values(
    by='Nilai Akhir',
    ascending=False
)

ranking['Ranking'] = range(1, len(ranking) + 1)

print("\n================================")
print("HASIL RANKING")
print("================================")
print(ranking)

# ------------------------------------------
# 9. Menentukan Kandidat Terbaik
# ------------------------------------------

terbaik = ranking.iloc[0]

print("\n================================")
print("KESIMPULAN")
print("================================")

print(
    f"Kandidat terbaik untuk menjadi "
    f"Team Leader adalah "
    f"{terbaik['Kandidat']} "
    f"dengan nilai akhir "
    f"{terbaik['Nilai Akhir']:.1f}"
)
```
