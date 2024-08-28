def speak_direct():
    print("meov direct")
def speak_imported():
    print("meov imported")

def testFunc():
    print("Test Fonksiyonudur")

if __name__ == "__main__":
    speak_direct() # yukardaki if i kullanarak şu an içinde oldugum python dosyası dışında başka bir dosyada çalıştırıldıgında speak importedi bu dopsyada çalıştırıldıgında da directi görecegim
else: # == main bu dosyada mı çalıştırılıyor diye sorgulamaya yarıyor
    speak_imported()  ######## başka bir python dosyasında import etsen ve hiçbir fonksiyonu kullanmasan bile mainden başka bir dosyada çalıoştırdıgın için else çalışıyor
# BU YAZDIĞIM KODLA FONKSİYON KENDİ İÇİNDEN ÇALIŞTIRILIRSA FARKLI ŞEY BAŞKA BİR PYTHON DOSYASINDAN ÇALIŞTIRIKLIYORSA FARKLI ŞEY YAZDIRIR7
# BAŞKA PYTHON DOSYASINDAN ÇALIŞTIRSAYDIM "meov imported" çalışıcaktı