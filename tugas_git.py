# Data panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Tampilkan seluruh data
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"  {hasil}: {jumlah}")
    print()

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2: {jumlah_jagung_lokasi2}\n")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")

# 4. Masukkan jumlah hasil panen padi dan kedelai ke variabelgit
padi_total = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
kedelai_total = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("Jumlah hasil panen dari padi per lokasi:", padi_total)
print("Jumlah hasil panen dari kedelai per lokasi:", kedelai_total, "\n")


# 5. Percabangan untuk perhatian khusus
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        status = "memerlukan perhatian khusus"
    else:
        
        status = "dalam kondisi baik"
    print(f"Lokasi {data['nama_lokasi']} {status}.")
