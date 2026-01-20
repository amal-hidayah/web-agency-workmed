"""
Script untuk menghapus semua data dummy (klien dan portfolio)
Jalankan: python reset_data.py
"""

from app import app, db
from models import Client, Portfolio
import os

def reset_data():
    with app.app_context():
        # Hapus semua klien
        clients = Client.query.all()
        for client in clients:
            db.session.delete(client)
        
        # Hapus semua portfolio
        portfolios = Portfolio.query.all()
        for portfolio in portfolios:
            db.session.delete(portfolio)
        
        # Commit perubahan
        db.session.commit()
        
        print(f"✅ Berhasil menghapus {len(clients)} klien")
        print(f"✅ Berhasil menghapus {len(portfolios)} portfolio")
        print("\n🎉 Database sudah bersih! Silakan isi dengan data asli Anda.")

if __name__ == '__main__':
    print("⚠️  Menghapus semua data klien dan portfolio...")
    print("⚠️  User admin TIDAK akan dihapus.\n")
    
    confirm = input("Lanjutkan? (ketik 'ya' untuk konfirmasi): ")
    
    if confirm.lower() == 'ya':
        reset_data()
    else:
        print("❌ Dibatalkan.")
