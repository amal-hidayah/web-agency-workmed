# Working Media - Website Portfolio

Website portfolio profesional untuk studio digital marketing Working Media, dibangun dengan Flask dan Tailwind CSS.

## Fitur Utama

- ✅ Single Page Application (SPA) dengan smooth scroll navigation
- ✅ Desain modern dan responsif menggunakan Tailwind CSS
- ✅ Tema warna dominan oranye sesuai branding
- ✅ Animasi hover pada kartu layanan
- ✅ 6 Section lengkap: Hero, About, Services, Pricing, Portfolio, Contact
- ✅ Integrasi WhatsApp dan email
- ✅ Foto profesional dari Unsplash
- ✅ Mobile-friendly design

## Teknologi yang Digunakan

- **Backend**: Python Flask
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Font**: Google Fonts (Poppins)
- **Icons**: SVG Icons

## Instalasi

1. Clone atau download project ini
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python app.py
```

4. Buka browser dan akses:
```
http://localhost:5000
```

## Struktur Folder

```
workingmedia/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── images/           # Folder untuk gambar
    └── css/              # Folder untuk CSS tambahan
```

## Konten Website

### 1. Hero Section
- Nama: Working Media
- Tagline: "Mitra Aktivasi Media Sosial dan Konten Visual Anda"
- Call-to-action buttons

### 2. About Us
- Deskripsi lengkap studio
- Statistik: 50+ Klien, 200+ Projects, 5+ Tahun

### 3. Services (6 Layanan)
- Aktivasi Sosial Media
- Perancangan Konten Visual
- Online Advertising Management
- Pembuatan Website & Aplikasi
- Professional Copywriting
- Video Production

### 4. Pricing
**Paket Bulanan:**
- Super Hemat: Rp 3.450.000
- Paket Premium: Rp 4.200.000
- Paket Business: Rp 6.600.000

**Harga Satuan:**
- Konten Visual: Rp 150.000
- Foto Produk: Rp 250.000
- Video Promosi: Rp 500.000
- Dan lainnya...

### 5. Portfolio Klien
**Food & Beverage:** Jawara Kerang, Foresthree Coffee, Bebek Bang Acim, Tiger Sweet, Momomilk, Kandang Susu, Yun Sin

**Lifestyle & Hospitality:** Arnava Bogor Hotel, Nikita Mirzani Skincare, Thmany Sinergi Utama, GEEZ

**Lainnya:** Tactical In Police (Bimbel Polri)

### 6. Contact
- Alamat: Jln. Pertanian PPMKP Bendungan Ciawi, Bogor
- WhatsApp: +62 896-1392-2360
- Email: workingmedia.art@gmail.com

## Kustomisasi

### Mengganti Warna
Edit di bagian `tailwind.config` dalam file `index.html`:
```javascript
colors: {
    'brand-orange': '#FF6B35',
    'brand-orange-dark': '#E55A2B',
}
```

### Menambah/Edit Konten
Edit langsung di file `templates/index.html` pada section yang diinginkan.

### Mengganti Foto
Saat ini website menggunakan foto dari Unsplash. Untuk menggunakan foto sendiri:
1. Simpan foto di folder `static/images/`
2. Ganti URL foto di HTML dengan: `/static/images/nama-foto.jpg`

## Deployment

### Deploy ke Heroku
1. Install Heroku CLI
2. Buat file `Procfile`:
```
web: python app.py
```
3. Deploy:
```bash
heroku create workingmedia
git push heroku main
```

### Deploy ke PythonAnywhere
1. Upload semua file ke PythonAnywhere
2. Configure web app untuk menggunakan Flask
3. Set working directory dan WSGI configuration

## Support

Untuk pertanyaan atau bantuan, hubungi:
- WhatsApp: +62 896-1392-2360
- Email: workingmedia.art@gmail.com

## License

© 2026 Working Media. All rights reserved.
