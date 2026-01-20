# Panduan Deployment Working Media Website

## 1. Deploy ke Heroku

### Persiapan
```bash
# Install Heroku CLI dari https://devcenter.heroku.com/articles/heroku-cli

# Login ke Heroku
heroku login
```

### Buat Procfile
File `Procfile` sudah dibuat dengan konten:
```
web: gunicorn app:app
```

### Update requirements.txt
Tambahkan gunicorn:
```
Flask==3.0.0
gunicorn==21.2.0
```

### Deploy
```bash
# Inisialisasi Git (jika belum)
git init
git add .
git commit -m "Initial commit"

# Buat aplikasi Heroku
heroku create workingmedia

# Deploy
git push heroku main

# Buka aplikasi
heroku open
```

## 2. Deploy ke PythonAnywhere

### Langkah-langkah:
1. Daftar akun di [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload semua file via File Manager atau Git
3. Buka Web tab
4. Klik "Add a new web app"
5. Pilih Flask
6. Atur path ke app.py
7. Reload web app

### WSGI Configuration
Edit file WSGI untuk menambahkan:
```python
import sys
path = '/home/username/workingmedia'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

## 3. Deploy ke Railway

### Langkah-langkah:
1. Daftar di [Railway](https://railway.app)
2. Connect repository GitHub
3. Railway akan auto-detect Flask
4. Deploy otomatis

## 4. Deploy ke Vercel

### Persiapan
Buat file `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Deploy
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

## 5. Deploy ke Google Cloud Platform (GCP)

### Buat app.yaml
```yaml
runtime: python39

handlers:
- url: /static
  static_dir: static

- url: /.*
  script: auto
```

### Deploy
```bash
gcloud app deploy
```

## 6. Deploy ke AWS Elastic Beanstalk

### Persiapan
Buat file `.ebextensions/python.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
```

### Deploy
```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init

# Create environment
eb create workingmedia-env

# Deploy
eb deploy
```

## Domain Custom

### Setelah deploy, tambahkan domain custom:

1. **Heroku**: 
```bash
heroku domains:add www.workingmedia.com
```

2. **PythonAnywhere**: Upgrade ke paid plan untuk custom domain

3. **Vercel**: Add domain di dashboard

### Setup DNS
Arahkan domain ke server:
- A Record: IP address server
- CNAME Record: subdomain ke server

## SSL Certificate

Semua platform modern (Heroku, Vercel, Railway) menyediakan SSL gratis via Let's Encrypt.

## Environment Variables

Untuk production, set environment variables:
```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

## Monitoring & Logging

- Heroku: `heroku logs --tail`
- PythonAnywhere: Check error log di web tab
- Railway: Built-in logging dashboard

## Backup & Recovery

Selalu backup:
1. Database (jika ada)
2. Static files
3. Configuration files

## Performance Optimization

1. Enable CDN untuk static files
2. Use caching headers
3. Compress images
4. Minify CSS/JS (optional)
5. Use production WSGI server (gunicorn)

## Security Checklist

- ✅ HTTPS enabled
- ✅ Debug mode off in production
- ✅ Secure secret keys
- ✅ CSRF protection
- ✅ Rate limiting
- ✅ Regular updates

## Troubleshooting

### Error: "Application Error"
- Check logs
- Verify Procfile
- Check requirements.txt

### Static files not loading
- Check static folder path
- Verify Flask configuration
- Check server configuration

### 502 Bad Gateway
- Check application is running
- Verify port binding
- Check worker timeout

## Support

Untuk bantuan deployment, hubungi:
- Email: workingmedia.art@gmail.com
- WhatsApp: +62 896-1392-2360
