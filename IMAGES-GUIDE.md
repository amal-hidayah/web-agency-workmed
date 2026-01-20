# Panduan Menambahkan Foto Profesional

## 1. Foto yang Dibutuhkan

### Hero Section
- **File**: `hero-team.jpg`
- **Ukuran**: 600x600px
- **Deskripsi**: Foto tim atau workspace profesional
- **Lokasi**: `static/images/hero-team.jpg`

### About Section
- **File**: `about-team.jpg`
- **Ukuran**: 600x400px
- **Deskripsi**: Foto tim bekerja atau meeting
- **Lokasi**: `static/images/about-team.jpg`

### Portfolio Section (6 foto)
- `portfolio-1.jpg` - Social Media Content (400x400px)
- `portfolio-2.jpg` - Food Photography (400x400px)
- `portfolio-3.jpg` - Digital Marketing (400x400px)
- `portfolio-4.jpg` - Web Design (400x400px)
- `portfolio-5.jpg` - Team Collaboration (400x400px)
- `portfolio-6.jpg` - Creative Work (400x400px)

## 2. Logo Klien

Buat folder: `static/images/clients/`

Format file: PNG dengan background transparan
Ukuran: 200x200px

Nama file:
- `jawara-kerang.png`
- `foresthree-coffee.png`
- `bebek-bang-acim.png`
- `tiger-sweet.png`
- `momomilk.png`
- `kandang-susu.png`
- `yun-sin.png`
- `arnava-hotel.png`
- `nikita-mirzani-skincare.png`
- `thmany.png`
- `geez.png`
- `tactical-in-police.png`

## 3. Favicon

Buat favicon di: https://favicon.io/

Download dan extract ke `static/`:
- `favicon.ico`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `apple-touch-icon.png`

## 4. Cara Mengganti Foto di HTML

### Saat ini menggunakan Unsplash (temporary):
```html
<img src="https://images.unsplash.com/photo-xxxxx" alt="Description">
```

### Ganti dengan foto lokal:
```html
<img src="{{ url_for('static', filename='images/hero-team.jpg') }}" alt="Description">
```

atau

```html
<img src="/static/images/hero-team.jpg" alt="Description">
```

## 5. Optimasi Foto

### Sebelum Upload:
1. **Resize** ke ukuran yang sesuai
2. **Compress** menggunakan:
   - TinyPNG: https://tinypng.com/
   - Squoosh: https://squoosh.app/
3. **Format**:
   - JPEG untuk foto (quality 80-85%)
   - PNG untuk logo dengan transparansi
   - WebP untuk ukuran lebih kecil (modern browsers)

### Tools Rekomendasi:
- **Bulk Resize**: https://bulkresizephotos.com/
- **Remove Background**: https://remove.bg/
- **Image Optimizer**: https://imageoptim.com/

## 6. Template Update HTML

Edit file `templates/index.html`:

### Hero Section (Line ~100):
```html
<img src="{{ url_for('static', filename='images/hero-team.jpg') }}" 
     alt="Working Media Team" 
     class="rounded-2xl shadow-2xl w-full max-w-md">
```

### About Section (Line ~145):
```html
<img src="{{ url_for('static', filename='images/about-team.jpg') }}" 
     alt="About Working Media" 
     class="rounded-2xl shadow-xl">
```

### Portfolio Images (Line ~700):
```html
<img src="{{ url_for('static', filename='images/portfolio-1.jpg') }}" 
     alt="Social Media Content" 
     class="rounded-xl shadow-lg hover:scale-105 transition">
```

### Client Logos Example:
```html
<div class="bg-white rounded-xl p-6 shadow hover:shadow-xl transition">
    <img src="{{ url_for('static', filename='images/clients/jawara-kerang.png') }}" 
         alt="Jawara Kerang" 
         class="client-logo w-full h-auto">
</div>
```

## 7. Foto Profesional - Sumber Gratis

Jika belum punya foto sendiri, download dari:

### Stock Photos:
- **Unsplash**: https://unsplash.com/
- **Pexels**: https://pexels.com/
- **Pixabay**: https://pixabay.com/

### Keyword untuk search:
- "team meeting"
- "digital marketing workspace"
- "creative agency"
- "social media marketing"
- "graphic design workspace"
- "professional office"

## 8. Foto Profesional - Best Practices

### Konsistensi:
- Gunakan filter/tone yang sama untuk semua foto
- Perhatikan color grading (sesuaikan dengan brand orange)
- Ukuran dan rasio yang konsisten

### Quality:
- Resolusi minimal: 1920px untuk foto besar
- Hindari foto blur atau pixelated
- Gunakan foto dengan pencahayaan baik

### Brand Identity:
- Foto yang mencerminkan Working Media
- Tampilkan hasil kerja nyata jika memungkinkan
- Include team photos untuk personal touch

## 9. Checklist Upload Foto

- [ ] Download/prepare semua foto
- [ ] Resize ke ukuran yang sesuai
- [ ] Compress untuk web
- [ ] Upload ke folder `static/images/`
- [ ] Update path di HTML
- [ ] Test tampilan di browser
- [ ] Verify mobile responsiveness
- [ ] Check loading speed

## 10. Script Auto-Replace (Advanced)

Buat script Python untuk batch replace:

```python
# replace_images.py
import os
from PIL import Image

def optimize_image(input_path, output_path, quality=85):
    img = Image.open(input_path)
    img.save(output_path, optimize=True, quality=quality)

# Usage
optimize_image('original/hero.jpg', 'static/images/hero-team.jpg', 85)
```

## Contact untuk Bantuan

Jika perlu bantuan menambahkan foto:
- Email: workingmedia.art@gmail.com
- WhatsApp: +62 896-1392-2360
