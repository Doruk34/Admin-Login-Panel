import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Tk, Label, PhotoImage
class Login_Panel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Paneli")
        self.root.geometry("900x600")
        self.root.resizable(width=True,height=True)
        self.root.iconbitmap("admin.ico")
        self.kullanicilar = {}  # Kullanıcı bilgilerini saklamak için bir sözlük tanımladım.

        self.arkaplan_resmi = PhotoImage(file="bg.png")
        labelarkaplan = Label(self.root, image=self.arkaplan_resmi)
        labelarkaplan.place(x=0, y=0)

        cursor_dosya = "cursor.ico"
        root.config(cursor=f"@{cursor_dosya}")

        label = tk.Label(root)
        label.pack(padx=20, pady=20)

        tk.Label(self.root, text="Kayıt Sistemi", font="Verdana 12 bold", bg="lightgray", fg="black", padx=35, pady=5).pack()

        self.giris_frame = tk.Frame(root)
        self.giris_frame.pack(pady=20)

        self.admin_label = tk.Label(self.giris_frame, text="ID:")
        self.admin_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_entry = tk.Entry(self.giris_frame)
        self.admin_entry.grid(row=0, column=1, padx=10, pady=10)

        self.sifre_label = tk.Label(self.giris_frame, text="Şifre:")
        self.sifre_label.grid(row=1, column=0, padx=10, pady=10)
        self.sifre_entry = tk.Entry(self.giris_frame, show="*")
        self.sifre_entry.grid(row=1, column=1, padx=10, pady=10)

        self.gorsel2 = ImageTk.PhotoImage(Image.open("C:/Users/Doruk Akgün/OneDrive - metu.edu.tr/Masaüstü/VS Code Python/login.png").resize((50, 50)))
        self.gorsel_label2 = tk.Label(self.giris_frame, image=self.gorsel2)
        self.gorsel_label2.grid(row=1, column=2, padx=10, pady=10)

        self.gorsel1 = ImageTk.PhotoImage(Image.open("C:/Users/Doruk Akgün/OneDrive - metu.edu.tr/Masaüstü/VS Code Python/id.png").resize((50, 50)))
        self.gorsel_label1 = tk.Label(self.giris_frame, image=self.gorsel1)
        self.gorsel_label1.grid(row=0, column=2, padx=10, pady=10)

        self.giris_button = tk.Button(self.giris_frame, text="Giriş", command=self.admin_giris, height=2, width=15)
        self.giris_button.grid(row=2, column=0, columnspan=3, pady=10)
 
    def admin_giris(self):
            admin_id = self.admin_entry.get()
            şifre = self.sifre_entry.get()

            if admin_id == "admin" and şifre == "1234":
                self.giris_frame.destroy()
                self.kisi_bilgi_penceresi_goster()
            else:
                messagebox.showerror("Hata","Hatalı ID veya Şifre Girdiniz!")

    def turkce_karakter_kontrol(self, deger):
        if any(karakter in 'ğüşıöçĞŞİÖÇ' for karakter in deger):  # any: En az bir öğenin doğru olup olmadığını kontrol ediyor.
            messagebox.showerror("Hata","Geçersiz Karakter. Lütfen Türkçe Karakter Kullanmayınız! ")
            return False
        return True
    
    def ad_soyad_kontrol(self, ad_soyad):
        if not ad_soyad or not ad_soyad.replace(" ", "") or not self.turkce_karakter_kontrol(ad_soyad):  # if not ad_soyad: Değişkenin boş(None) veya boş bir dize olup olmadığını kontrol eder.
            messagebox.showerror("Geçersiz Kullanıcı Adı veya Soyadı. Lütfen Türkçe Karakter Kullanmayınız!")
            return False
        return True     

    def tc_kimlik_no_kontrol(self, deger):
        if len(deger) != 11 or not deger.isdigit():
            messagebox.showerror("Hata", "Geçersiz TC Kimlik Numarası. Lütfen 11 Haneden Oluşan Bir Numara Giriniz!")
            return False
        return True
    
    def telefon_no_kontrol(self, deger):
        if len(deger) != 12 or not deger.isdigit():
            messagebox.showerror("Hata", "Geçersiz Telefon Numarası. Lütfen 12 Haneden Oluşan Bir Numara Giriniz!")
            return False
        return True
    
    def email_kontrol(self, email):
        if email in self.kullanicilar:
            messagebox.showerror("Hata","Bu Email Zaten Mevcut!")
            return False
        return True

    def dogum_tarihi_kontrol(self, deger):
        if ' ' in deger:
            messagebox.showerror("Hata","Doğum Tarihi İçinde Boşluk Olmamalıdır!")
            return False
        if not deger.isnumeric():
            messagebox.showerror("Hata","Doğum Tarihi Sadece Rakamlardan Oluşmalıdır!")
            return False
        if len(deger) != 8:
            messagebox.showerror("Hata","Doğum Tarihi 8 Haneden Oluşmalıdır")
            return False
        return True

    def kisi_bilgi_penceresi_goster(self):

        self.kisi_bilgi_frame = tk.Frame(root)
        self.kisi_bilgi_frame.pack(pady=20)

        self.ad_soyad_label = tk.Label(self.kisi_bilgi_frame, text="Ad Soyad:")
        self.ad_soyad_label.grid(row=0, column=0, padx= 10, pady=10)
        self.ad_soyad_entry = tk.Entry(self.kisi_bilgi_frame)
        self.ad_soyad_entry.grid(row=0, column=1, padx=10, pady=10)

        self.tc_kimlik_label = tk.Label(self.kisi_bilgi_frame, text="TC Kimlik No:")
        self.tc_kimlik_label.grid(row=1, column=0, padx=10, pady=10)
        self.tc_kimlik_entry = tk.Entry(self.kisi_bilgi_frame)
        self.tc_kimlik_entry.grid(row=1, column=1, padx=10, pady=10)

        self.telefon_label = tk.Label(self.kisi_bilgi_frame, text="Telefon No:")
        self.telefon_label.grid(row=2, column=0, padx=10, pady=10)
        self.telefon_entry = tk.Entry(self.kisi_bilgi_frame)
        self.telefon_entry.grid(row=2, column=1, padx=10, pady=10)

        self.cinsiyet_label = tk.Label(self.kisi_bilgi_frame, text="Cinsiyet:")
        self.cinsiyet_label.grid(row=3, column=0, padx=10, pady=10)
        self.cinsiyet_combobox = tk.StringVar()
        self.cinsiyet_combobox.set("Seçiniz")
        self.cinsiyet_dropdown = tk.OptionMenu(self.kisi_bilgi_frame, self.cinsiyet_combobox, "Erkek", "Kadin", "Diğer")
        self.cinsiyet_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.email_label = tk.Label(self.kisi_bilgi_frame, text="E-mail:")
        self.email_label.grid(row=4, column=0, padx=10,pady=10)
        self.email_entry = tk.Entry(self.kisi_bilgi_frame)
        self.email_entry.grid(row=4, column=1, padx=10, pady=10)

        self.dogum_tarihi_label = tk.Label(self.kisi_bilgi_frame, text="Doğum Tarihi:")
        self.dogum_tarihi_label.grid(row=5, column=0, padx=10, pady=10)
        self.dogum_tarihi_entry = tk.Entry(self.kisi_bilgi_frame)
        self.dogum_tarihi_entry.grid(row=5, column=1, padx=10, pady=10)
        
        self.ekle_button = tk.Button(self.kisi_bilgi_frame, text="Ekle", command=self.ekle_button_click)
        self.ekle_button.grid(row=20, column=0, padx=10, pady=10)

        self.temizle_button = tk.Button(self.kisi_bilgi_frame, text="Temizle", command=self.temizle)
        self.temizle_button.grid(row=20, column=1, padx=10, pady=10)

        self.kaydet_button = tk.Button(self.kisi_bilgi_frame, text="Kaydet", command=self.kisi_bilgi_kaydet)
        self.kaydet_button.grid(row=20, column=2, padx=10, pady=10)

        self.cikis_button = tk.Button(self.root, text="Çıkış", command=self.root.destroy)
        self.cikis_button.pack(pady=10)

        # Treeview sonuçları görmek için
        self.sonuc_frame = tk.Frame(self.root)
        self.sonuc_frame.pack(pady=20)
        self.tree = ttk.Treeview(self.sonuc_frame, columns=("Ad Soyad", "TC Kimlik No", "Telefon No", "Cinsiyet", "E-mail", "Doğum Tarihi"), show="headings")
        self.tree.column("Ad Soyad", width=150)
        self.tree.column("TC Kimlik No", width=150)
        self.tree.column("Telefon No", width=150)
        self.tree.column("Cinsiyet", width=150)
        self.tree.column("E-mail", width=150)
        self.tree.column("Doğum Tarihi", width=150)
        self.tree.heading("Ad Soyad", text="Ad Soyad")
        self.tree.heading("TC Kimlik No", text="TC Kimlik No")
        self.tree.heading("Telefon No", text="Telefon No")
        self.tree.heading("Cinsiyet", text="Cinsiyet")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Doğum Tarihi", text="Doğum Tarihi")
        self.tree.pack()

        self.kisiler = []

    def ekle_button_click(self):
        kisi_bilgisi = {
            "Ad Soyad": self.ad_soyad_entry.get(),
            "TC Kimlik No": self.tc_kimlik_entry.get(),
            "Telefon No": self.telefon_entry.get(),
            "Cinsiyet": self.cinsiyet_combobox.get(),
            "E-mail": self.email_entry.get(),
            "Doğum Tarihi": self.dogum_tarihi_entry.get()
        }
        if not self.ad_soyad_kontrol(kisi_bilgisi["Ad Soyad"]):
            messagebox.showerror("Hata","Türkçe Karakter Girdiniz!")
            return

        if not self.tc_kimlik_no_kontrol(kisi_bilgisi["TC Kimlik No"]):
            messagebox.showerror("Hata", "Hatalı TC Kimlik Numarası Girdiniz!")
            return

        if not self.telefon_no_kontrol(kisi_bilgisi["Telefon No"]):
            messagebox.showerror("Hata", "Hatalı Telefon Numarası Girdiniz!")
            return
        
        if not self.email_kontrol(kisi_bilgisi["E-mail"]):
            messagebox.showerror("Hata","Bu Email Zaten Mevcut!")
            return
        
        if not self.dogum_tarihi_kontrol(kisi_bilgisi["Doğum Tarihi"]):
            messagebox.showerror("Hata","Hatalı Doğum Tarihi. Lütfen Özel Karakter, Boşluk ve Fazla Hane Girişine Dikkat Ediniz!")
            return

        else:
            messagebox.showinfo("Bilgi", "Ekleme İşlemi Başarılı Bir Şekilde Gerçekleşmiştir!")

    
        self.kisiler.append(kisi_bilgisi)

        self.update_treeview()

    def kisi_bilgi_kaydet(self):
        
        with open("kisi_bilgisi.txt", "a") as dosya:
            for kişi in self.kisiler:
                dosya.write(
                    f"Ad Soyad: {kişi['Ad Soyad']}, TC Kimlik No: {kişi['TC Kimlik No']}, Telefon No: {kişi['Telefon No']}, Cinsiyet: {kişi['Cinsiyet']}, E-mail: {kişi['E-mail']}, Dogum Tarihi: {kişi['Doğum Tarihi']}\n")
    

        messagebox.showinfo("Bilgi", "Kişi Başarılı Bir Şekilde Kaydedilmiştir!")
    
        self.kisiler = []

        self.temizle()

        self.guncel_verileri_goster()  # Treeview'i kaydedilen veriler ile günceller

    def temizle(self):
        self.ad_soyad_entry.delete(0, tk.END)
        self.tc_kimlik_entry.delete(0, tk.END)
        self.telefon_entry.delete(0, tk.END)
        self.cinsiyet_combobox.set("Seçiniz")
        self.email_entry.delete(0, tk.END)
        self.dogum_tarihi_entry.delete(0, tk.END)

    def guncel_verileri_goster(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)

        with open("kisi_bilgisi.txt", "r") as dosya:  # Dosyadaki verileri okur ve Treeview'i doldurur. Treeview (Tablo görünümü sağlayan ağaç yapısı).
            for satir in dosya:
                veri = satir.strip().split(", ")
                self.tree.insert("", "end", values=(
                veri[0].split(":")[1], veri[1].split(":")[1], veri[2].split(":")[1], veri[3].split(":")[1], veri[4].split(":")[1], veri[5].split(":")[1]))

    def update_treeview(self):
        
        for item in self.tree.get_children():   # Treeview daki mevcut dataları temizler.
            self.tree.delete(item)

        for indeks, kişi in enumerate(self.kisiler, start=1):   # Treeview' a yeni data ekler.
            self.tree.insert("", "end", iid=indeks, values=(    # iid Öğe tanımlayıcı kısaltması, öğelerin benzersiz bir şekilde tanımlanması için kullanılır.
            kişi["Ad Soyad"], kişi["TC Kimlik No"], kişi["Telefon No"], kişi["Cinsiyet"], kişi["E-mail"], kişi["Doğum Tarihi"]))

class kullanici_yonetimi:
    def yeni_kullanici_ekle(self, email, sifre):
        if self.email_kontrol(email):
           self.kullanicilar[email] = sifre
           messagebox.showinfo("Başarılı","E-mail Başarılı Bir Şekilde Kaydedilmiştir!")

           kullanici_yonetimi = kullanici_yonetimi()
           kullanici_yonetimi.yeni_kullanici_ekle("doruk@gmail.com","sifre123")
           kullanici_yonetimi.yeni_kullanici_ekle("ornek@gmail.com","yenisifre")

if __name__ == "__main__":
    root = tk.Tk()
    Login_Panel = Login_Panel(root)
    root.mainloop()