# ⚡ Quick Start Guide - Working Media Website

## 🚀 Start dalam 3 Langkah

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Jalankan Server
```bash
python app.py
```

### 3️⃣ Buka Browser
```
http://localhost:5000
```

**✅ Website sudah jalan!**

---

## 📋 Yang Perlu Anda Ketahui

### 🎯 URL Website
- **Local Development**: http://localhost:5000
- **Production**: (setelah deploy)

### 📁 File Penting
- `app.py` - Flask backend
- `templates/index.html` - Halaman website
- `static/` - CSS, JS, Images

### 🎨 Edit Konten
Edit file: `templates/index.html`
- Cari section yang ingin diubah (Hero, About, Services, dll)
- Edit teks langsung
- Save file
- Refresh browser (auto-reload jika debug mode ON)

### 🖼️ Ganti Foto
1. Taruh foto di: `static/images/`
2. Edit path di HTML:
   ```html
   <img src="/static/images/nama-foto.jpg">
   ```
3. Lihat detail: `IMAGES-GUIDE.md`

### 🎨 Ubah Warna
Edit di `templates/index.html` (line ~10):
```javascript
colors: {
    'brand-orange': '#FF6B35',  // Warna utama
}
```

### 💰 Edit Harga
Cari `id="pricing"` di `templates/index.html`
Edit angka dan teks sesuai kebutuhan

---

## 🌐 Deploy ke Internet

### Option 1: Heroku (Gratis)
```bash
heroku login
heroku create workingmedia
git push heroku main
```

### Option 2: Vercel (Gratis)
```bash
npm i -g vercel
vercel
```

**Detail lengkap: `DEPLOYMENT.md`**

---

## 📱 Fitur Website

✅ 6 Section Lengkap (Hero, About, Services, Pricing, Portfolio, Contact)
✅ Responsive (Desktop, Tablet, Mobile)
✅ Smooth Scroll Navigation
✅ Animasi Hover & Scroll
✅ Form Kontak dengan Validasi
✅ WhatsApp Integration
✅ SEO Optimized

---

## 📚 Dokumentasi Lengkap

| File | Deskripsi |
|------|-----------|
| `README.md` | Overview & instalasi |
| `DEPLOYMENT.md` | Panduan deploy |
| `IMAGES-GUIDE.md` | Cara ganti foto |
| `USER-GUIDE.md` | Panduan lengkap |
| `PROJECT-SUMMARY.md` | Ringkasan project |

---

## 🆘 Butuh Bantuan?

📧 **Email**: workingmedia.art@gmail.com
📱 **WhatsApp**: +62 896-1392-2360

---

## ⚠️ Troubleshooting Cepat

### Website tidak jalan?
```bash
python --version  # Pastikan Python 3.7+
pip install -r requirements.txt --force-reinstall
python app.py
```

### Foto tidak muncul?
- Check path: `/static/images/filename.jpg`
- Clear browser cache (Ctrl + F5)

### Error saat deploy?
- Check `DEPLOYMENT.md`
- Verify file `Procfile` dan `requirements.txt`

---

## 🎉 Selamat!

Website Working Media Anda sudah siap! 🚀

**Next Steps:**
1. ✅ Review website
2. 📸 Ganti foto (opsional)
3. 🌐 Deploy ke internet
4. 📊 Setup analytics

**Happy Coding! 💻**
