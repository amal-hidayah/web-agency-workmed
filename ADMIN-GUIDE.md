# 🔐 Panduan Admin Panel - Working Media

## 📋 Fitur Admin Panel

Panel admin yang telah ditambahkan memungkinkan Anda untuk:

✅ **Upload Logo Klien** - Kelola portfolio klien dengan logo/emoji
✅ **Upload Portfolio** - Tambah hasil karya dengan gambar
✅ **Edit & Hapus Konten** - Kelola semua konten dengan mudah
✅ **Status Aktif/Nonaktif** - Kontrol konten yang tampil di website
✅ **Urutan Tampilan** - Atur urutan tampilan konten
✅ **Kategori** - Organisir konten berdasarkan kategori

---

## 🚀 Cara Akses Admin Panel

### 1. Akses Halaman Login

Buka browser dan kunjungi:
```
http://localhost:5000/admin/login
```

### 2. Login dengan Kredensial Default

**Username:** `admin`  
**Password:** `admin123`

⚠️ **PENTING:** Ganti password setelah login pertama kali!

### 3. Setelah Login

Anda akan diarahkan ke Dashboard Admin dengan akses ke:
- Dashboard (statistik)
- Kelola Klien
- Kelola Portfolio
- Logout

---

## 📁 Kelola Klien Portfolio

### Menambah Klien Baru

1. Klik **"Klien"** di menu navigasi
2. Klik tombol **"➕ Tambah Klien"**
3. Isi form:
   - **Nama Klien** (wajib): Contoh: "Jawara Kerang"
   - **Kategori** (wajib): Pilih dari dropdown
     - Food & Beverage
     - Lifestyle & Hospitality
     - Lainnya
   - **Emoji** (opsional): Contoh: 🦪 ☕ 🏨
   - **Logo** (opsional): Upload file JPG/PNG/GIF/SVG
   - **Urutan**: 0 = tampil paling awal
   - **Aktif**: Centang untuk menampilkan di website

4. Klik **"💾 Simpan"**

### Upload Logo Klien

**Format yang Didukung:**
- JPG, JPEG
- PNG (dengan transparansi)
- GIF
- SVG

**Ukuran Maksimal:** 16MB per file

**Tips:**
- Gunakan PNG dengan background transparan untuk hasil terbaik
- Ukuran ideal: 200x200px hingga 400x400px
- Compress gambar sebelum upload untuk loading lebih cepat

### Edit Klien

1. Klik tombol **"Edit"** pada klien yang ingin diubah
2. Ubah data yang diperlukan
3. Klik **"💾 Simpan"**

### Hapus Klien

1. Klik tombol **"Hapus"** pada klien yang ingin dihapus
2. Konfirmasi penghapusan
3. Data akan terhapus permanen

---

## 🖼️ Kelola Portfolio / Hasil Karya

### Menambah Portfolio Baru

1. Klik **"Portfolio"** di menu navigasi
2. Klik tombol **"➕ Tambah Portfolio"**
3. Isi form:
   - **Judul** (wajib): Nama project/hasil karya
   - **Deskripsi** (opsional): Penjelasan singkat
   - **Kategori**: Pilih dari dropdown
     - Social Media
     - Design
     - Photography
     - Video
     - Web Development
     - Lainnya
   - **Gambar** (WAJIB): Upload hasil karya
   - **Urutan**: 0 = tampil paling awal
   - **Aktif**: Centang untuk menampilkan di website

4. Klik **"💾 Simpan"**

### Upload Gambar Portfolio

**Format yang Didukung:**
- JPG, JPEG
- PNG
- GIF

**Ukuran Maksimal:** 16MB per file

**Tips:**
- Gunakan resolusi tinggi (minimal 800x800px)
- Aspect ratio 1:1 atau 4:3 untuk tampilan optimal
- Compress gambar untuk loading lebih cepat
- Gunakan watermark jika perlu

### Edit Portfolio

1. Klik tombol **"Edit"** pada portfolio yang ingin diubah
2. Ubah data yang diperlukan
3. Upload gambar baru jika ingin mengganti
4. Klik **"💾 Simpan"**

### Hapus Portfolio

1. Klik tombol **"Hapus"** pada portfolio yang ingin dihapus
2. Konfirmasi penghapusan
3. Data akan terhapus permanen

---

## 📊 Dashboard

Dashboard menampilkan:
- **Total Klien**: Jumlah klien yang terdaftar
- **Total Portfolio**: Jumlah hasil karya
- **Views Hari Ini**: (Coming soon)
- **Status**: Status website

**Quick Actions:**
- Tambah Klien Baru
- Lihat Semua Klien
- Tambah Portfolio Baru
- Lihat Semua Portfolio

---

## 🗂️ Struktur File Upload

File yang diupload akan tersimpan di:

```
static/
└── uploads/
    ├── clients/        # Logo klien
    │   ├── logo1_20260120_123456.png
    │   └── logo2_20260120_123457.jpg
    └── portfolio/      # Gambar portfolio
        ├── project1_20260120_123458.jpg
        └── project2_20260120_123459.png
```

**File naming:** `nama_timestamp.ext`

---

## 💾 Database

Website menggunakan SQLite database: `workingmedia.db`

**Tables:**
- **User** - Admin users
- **Client** - Klien portfolio
- **Portfolio** - Hasil karya

**Backup Database:**
Backup file `workingmedia.db` secara berkala!

```bash
# Windows
copy workingmedia.db backup_workingmedia.db

# Linux/Mac
cp workingmedia.db backup_workingmedia.db
```

---

## 🎨 Tampilan di Website Utama

### Klien Portfolio
- Ditampilkan per kategori
- Diurutkan berdasarkan field "order"
- Jika ada logo: tampilkan logo
- Jika tidak ada logo: tampilkan emoji
- Hover effect: grayscale → color

### Portfolio/Hasil Karya
- Grid 3 kolom (responsive)
- Hover untuk lihat judul & deskripsi
- Ukuran gambar: 400x400px (auto-crop)
- Smooth scale-up animation

---

## ⚙️ Settings & Konfigurasi

### Ganti Password Admin

**Cara Manual (via database):**
1. Stop server
2. Edit `app.py`, ubah kode untuk create admin:
```python
admin.set_password('password_baru_anda')
```
3. Hapus file `workingmedia.db`
4. Restart server (database akan dibuat ulang)

### Tambah Admin Baru

**Via Python Shell:**
```python
from app import app, db
from models import User

with app.app_context():
    new_admin = User(username='nama_admin', email='admin@email.com')
    new_admin.set_password('password_kuat')
    db.session.add(new_admin)
    db.session.commit()
```

### Ubah Ukuran Upload

Edit `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

---

## 🔒 Keamanan

### Tips Keamanan:
1. ✅ **Ganti password default** segera
2. ✅ Gunakan password kuat (min 12 karakter)
3. ✅ Jangan share kredensial login
4. ✅ Backup database secara berkala
5. ✅ Update dependencies rutin
6. ✅ Gunakan HTTPS di production

### Logout
Selalu klik **"Logout"** setelah selesai menggunakan admin panel.

---

## 🐛 Troubleshooting

### Error: "Upload Failed"
**Solusi:**
- Check format file (JPG, PNG, GIF saja)
- Check ukuran file (max 16MB)
- Check permission folder `static/uploads/`

### Error: "Database Locked"
**Solusi:**
- Stop semua instance Flask yang berjalan
- Restart server

### Gambar Tidak Muncul di Website
**Solusi:**
- Check path gambar di database
- Verify file ada di folder `static/uploads/`
- Clear browser cache (Ctrl + F5)
- Check status "Aktif" pada konten

### Tidak Bisa Login
**Solusi:**
- Verify username & password
- Check database `workingmedia.db` ada
- Restart server
- Reset password (lihat section Ganti Password)

---

## 📝 Best Practices

### Penamaan File:
- Gunakan nama deskriptif
- Hindari spasi (gunakan underscore)
- Format: `nama_klien.png` atau `nama_project.jpg`

### Organisasi Konten:
- Set urutan (order) untuk control tampilan
- Gunakan kategori yang konsisten
- Update status "Aktif/Nonaktif" untuk kontrol visibility

### Maintenance Rutin:
- Backup database weekly
- Review & update konten monthly
- Clean unused images
- Monitor disk space

---

## 📱 Mobile Access

Admin panel **responsive** dan bisa diakses via mobile:
- Login via smartphone
- Upload foto langsung dari kamera
- Edit konten on-the-go

---

## 🆘 Support

Jika ada pertanyaan atau masalah:

📧 **Email:** workingmedia.art@gmail.com  
📱 **WhatsApp:** +62 896-1392-2360

---

## 🎯 Next Steps

Setelah mengatur admin panel:

1. ✅ Login dan ganti password
2. ✅ Upload logo semua klien
3. ✅ Upload portfolio/hasil karya
4. ✅ Test tampilan di website utama
5. ✅ Backup database
6. ✅ Deploy ke production

---

**Happy Managing! 🚀**

*Panel admin dibuat dengan ❤️ untuk Working Media*
