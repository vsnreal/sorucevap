import json
import random
#kütüphaneler bunlar

with open('sorular.json', 'r', encoding='utf-8') as f:
    sorular = json.load(f)
#jsonları oku, sonradan utf-8 ekledim. türkçe karakter sorunu cozuldu.
    
def rastgele_soru_sec():
    if not sorular:
        print("Soru listesi boş! Soru eklemek için 'ye' yazabilirsin.")
        return
#ye: yeni ekle

    soru_index = random.randint(0, len(sorular) - 1)
    soru = sorular[soru_index]
    print(soru["soru"])
    cevap = input("Cevabınız: ")

    if cevap.lower() == soru["cevap"].lower():
        print("Tebrikler! Doğru cevap!")
    else:
        print("Yanlış cevap.")
        print(f"Doğru cevap: {soru['cevap']}")

#rastgele secme fonk.
    
def yeni_soru_ekle():
    yeni_soru = input("Yeni soruyu girin: ")
    yeni_cevap = input("Doğru cevabı girin: ")
    sorular.append({"soru": yeni_soru, "cevap": yeni_cevap})
    with open('sorular.json', 'w') as f:
        json.dump(sorular, f)
    print("Soru eklendi!")

    devam_etmek = input("Ana menüye dönmek ister misiniz? (evet/hayır): ")
    if devam_etmek.lower() == "evet":
        return  # Ana menüye döner
    else:
        yeni_soru_ekle()  # Yeni soru eklemeye devam eder

#yeni soru fonksiuonu
    
while True:
    rastgele_soru_sec()

    devam_etmek = input("Devam etmek istiyor musunuz? (e/h/ye): ")

    if devam_etmek.lower() == "e":
        continue 
    elif devam_etmek.lower() == "h":
        break  
    elif devam_etmek.lower() == "ye":
        yeni_soru_ekle()
    else:
        print("Geçersiz giriş!")


