import os
import shutil
import subprocess
import ctypes
import sys

def is_admin():
    """Yönetici yetkisi kontrolü."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def kill_updates():
    # Durdurulacak ve devre dışı bırakılacak kritik servisler
    # wuauserv: Ana Update servisi
    # bits: Arka plan indirme
    # waasmedicvc: Update onarım (en inatçısı)
    # UsoSvc: Güncelleme orkestrasyonu
    servisler = ["wuauserv", "bits", "waasmedicvc", "UsoSvc"]
    
    # Pencere açılmasını engelleyen flag (0x08000000 = CREATE_NO_WINDOW)
    NO_WINDOW = 0x08000000

    for servis in servisler:
        try:
            # Önce servisi durdur
            subprocess.run(f"sc stop {servis}", shell=True, capture_output=True, creationflags=NO_WINDOW)
            # Sonra başlangıç türünü 'Devre Dışı' yap
            subprocess.run(f"sc config {servis} start=disabled", shell=True, capture_output=True, creationflags=NO_WINDOW)
        except:
            pass

    # Update indirme klasörünü temizle (Sistem dosyalarına dokunmaz)
    update_path = r"C:\Windows\SoftwareDistribution\Download"
    if os.path.exists(update_path):
        try:
            # Klasörü tamamen sil ve boş bir tane oluştur
            shutil.rmtree(update_path)
            os.makedirs(update_path)
        except:
            pass

if __name__ == "__main__":
    # Eğer yöneticiyse işlemi yap, değilse sessizce kapan (uyarı vermez)
    if is_admin():
        kill_updates()
    sys.exit()