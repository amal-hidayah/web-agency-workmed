# Panduan Pengguna Working Media Website

## Cara Menggunakan Website

### 1. Menjalankan Website Lokal

```bash
# Masuk ke folder project
cd workingmedia

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python app.py

# Buka browser
http://localhost:5000
```

### 2. Navigasi Website

Website ini adalah Single Page Application (SPA) dengan 6 section utama:

#### Home (Hero Section)
- Tampilan pertama pengunjung
- Menampilkan nama, keahlian, dan tagline
- 2 CTA button: "Lihat Layanan" dan "Konsultasi Gratis"

#### Tentang Kami
- Deskripsi lengkap Working Media
- Statistik: 50+ Klien, 200+ Projects, 5+ Tahun
- Menjelaskan layanan utama

#### Layanan
- 6 kartu layanan interaktif dengan hover effect
- Setiap kartu menjelaskan layanan spesifik
- Icon SVG untuk setiap layanan

#### Harga
- 3 paket bulanan dalam format kartu perbandingan
- Paket Premium highlighted sebagai pilihan populer
- Tabel harga satuan di bawah paket bulanan
- Link WhatsApp langsung untuk setiap paket

#### Portfolio
- Dibagi 3 kategori: F&B, Lifestyle & Hospitality, Lainnya
- Logo/nama klien dengan emoji icons
- 6 foto hasil karya (saat ini dari Unsplash)
- Hover effect pada setiap client card

#### Kontak
- Informasi lengkap: Alamat, WhatsApp, Email
- Form kontak untuk pengunjung
- Jam operasional
- Map location (bisa ditambahkan Google Maps)

### 3. Fitur Interaktif

#### Smooth Scroll
- Klik menu navigasi untuk scroll halus ke section
- Offset otomatis untuk navigation bar

#### Scroll to Top Button
- Muncul saat scroll > 300px
- Klik untuk kembali ke atas halus

#### Hover Effects
- Service cards: Naik 10px dengan shadow
- Pricing cards: Scale 1.05 dengan shadow oranye
- Client logos: Dari grayscale ke color

#### Form Validation
- Validasi nama, email, phone, message
- Format email dan nomor telepon Indonesia
- Alert jika ada field kosong atau format salah

### 4. Responsiveness

Website full responsive untuk semua device:

#### Desktop (>1024px)
- Layout multi-kolom penuh
- Sidebar navigation visible
- Hover effects aktif

#### Tablet (768px - 1024px)
- Layout 2 kolom
- Navigation tetap di atas
- Card size menyesuaikan

#### Mobile (<768px)
- Layout 1 kolom
- Navigation collapsed (hamburger - bisa ditambahkan)
- Touch-friendly buttons dan links
- Stack layout untuk semua section

### 5. Mengubah Konten

#### Edit Teks
File: `templates/index.html`

Cari section yang ingin diubah:
- `id="home"` - Hero section
- `id="about"` - About section
- `id="services"` - Services section
- `id="pricing"` - Pricing section
- `id="portfolio"` - Portfolio section
- `id="contact"` - Contact section

Edit teks di dalam tag HTML.

#### Edit Warna
File: `templates/index.html` (line ~10)

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'brand-orange': '#FF6B35',  // Ubah warna utama
                'brand-orange-dark': '#E55A2B',  // Ubah warna hover
                'brand-gray': '#2D3142',  // Ubah warna teks
            }
        }
    }
}
```

#### Edit Logo/Gambar
Lihat file: `IMAGES-GUIDE.md`

#### Edit Harga
Cari section `id="pricing"` di HTML dan ubah:
- Nama paket
- Harga (format: Rp X.XXX.XXX)
- Fitur paket (dalam list items)
- Link WhatsApp

#### Edit Klien
Cari section `id="portfolio"` dan:
- Tambah/kurangi klien
- Ganti nama
- Ganti emoji icon
- Upload logo (lihat IMAGES-GUIDE.md)

### 6. Menambah Section Baru

Template section baru:

```html
<section id="section-name" class="py-20 bg-white">
    <div class="container mx-auto px-6">
        <div class="text-center mb-16">
            <h2 class="text-4xl font-bold text-brand-gray section-title mb-4">
                Judul Section
            </h2>
            <p class="text-gray-600 mt-8">Deskripsi section</p>
        </div>
        <!-- Konten section -->
    </div>
</section>
```

Tambahkan link di navigation:
```html
<a href="#section-name" class="text-brand-gray hover:text-brand-orange transition">
    Section Name
</a>
```

### 7. Integrasi Form Contact

Saat ini form menggunakan action dummy. Untuk mengaktifkan:

#### Option 1: Formspree (Gratis)
1. Daftar di https://formspree.io/
2. Dapatkan form endpoint
3. Update form action:
```html
<form action="https://formspree.io/f/YOUR-FORM-ID" method="POST">
```

#### Option 2: EmailJS
1. Daftar di https://www.emailjs.com/
2. Setup service dan template
3. Tambah EmailJS SDK
4. Implement JavaScript

#### Option 3: Custom Backend
Update `app.py`:
```python
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    # Send email using smtplib
    return jsonify({'status': 'success'})
```

### 8. Analytics & Tracking

#### Google Analytics
Tambahkan di `<head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA-XXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA-XXXXXX');
</script>
```

#### Facebook Pixel
```html
<!-- Facebook Pixel -->
<script>
!function(f,b,e,v,n,t,s){...}
fbq('init', 'YOUR-PIXEL-ID');
fbq('track', 'PageView');
</script>
```

### 9. SEO Optimization

#### Update Meta Tags
Edit di `<head>`:
```html
<meta name="description" content="Deskripsi website">
<meta name="keywords" content="digital marketing, social media, bogor">
<meta property="og:title" content="Working Media">
<meta property="og:description" content="...">
<meta property="og:image" content="URL-to-image">
```

#### Submit ke Search Engines
- Google Search Console: https://search.google.com/search-console
- Bing Webmaster: https://www.bing.com/webmasters

### 10. Maintenance

#### Regular Updates
- [ ] Update konten portfolio setiap 3 bulan
- [ ] Cek dan update harga setiap 6 bulan
- [ ] Update client list setelah project baru
- [ ] Backup website setiap bulan
- [ ] Update dependencies: `pip list --outdated`

#### Performance Check
- PageSpeed Insights: https://pagespeed.web.dev/
- GTmetrix: https://gtmetrix.com/
- Mobile-Friendly Test: https://search.google.com/test/mobile-friendly

#### Security
- [ ] Update Flask dan dependencies rutin
- [ ] Enable HTTPS
- [ ] Backup database (jika ada)
- [ ] Monitor error logs

### 11. Troubleshooting

#### Website Tidak Jalan
```bash
# Check Python version
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check port
netstat -ano | findstr :5000
```

#### Foto Tidak Muncul
- Check path: `/static/images/filename.jpg`
- Verify file exists di folder
- Clear browser cache

#### Form Tidak Submit
- Check form action URL
- Verify form method="POST"
- Check JavaScript console for errors

#### Mobile Tidak Responsive
- Verify viewport meta tag
- Check Tailwind breakpoints
- Test di Chrome DevTools mobile emulator

### 12. Support & Bantuan

#### Dokumentasi
- README.md - Overview project
- DEPLOYMENT.md - Panduan deploy
- IMAGES-GUIDE.md - Panduan gambar
- CHANGELOG.md - History update

#### Kontak
- Email: workingmedia.art@gmail.com
- WhatsApp: +62 896-1392-2360

#### Resources
- Flask Docs: https://flask.palletsprojects.com/
- Tailwind CSS: https://tailwindcss.com/docs
- MDN Web Docs: https://developer.mozilla.org/

---

**Selamat menggunakan Working Media Website! 🚀**
