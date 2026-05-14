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
