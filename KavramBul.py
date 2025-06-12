import json
from zemberek.morphology import TurkishMorphology
import time
import os
source_folder = "Kaynaklar" # Kaynaklar klasöründe ders olmalı
ders = "Biyoloji" # Dersde veriseti olarak kullanacağımız json dictionary dosyası olmalı kavramlar bundan alınacak örnek json dosyasını dosyalardan ulaşabilirsiniz.
#Arama inp isimli değişkeninize kavramları bulmak istediğiniz metni yapıştırın örnek aşşağıdadır.
#aramainp = "Biyolojide bazı temel kavramlar vardır ki bunları bilmeden canlıların nasıl yaşadığını, çevreyle nasıl etkileşimde bulunduğunu anlamak zordur. Mesela adezyon ve kohezyon... Su molekülleri sadece birbirlerine değil, başka yüzeylere de tutunabilir. İşte başka yüzeylere tutunma durumu adezyondur. Cam yüzeyinde suyun yayılması gibi örnekler akla gelebilir. Öte yandan, su molekülleri birbirine de sıkı sıkıya bağlı kalmak ister. Bu da kohezyondur. Bir damla suyun dağılmadan kalması ya da tüp ağzında bombelenmesi hep bu kohezyon kuvvetinin işidir. Bitkilerde suyun kökten yapraklara kadar çıkmasında da bu iki özellik birlikte çalışır; su, damar çeperlerine yapışarak yukarı çıkar (adezyon), ama aynı zamanda su molekülleri birbirini çekerek kopmadan taşınır (kohezyon). Şimdi biraz da canlıların çevreye uyumundan söz edelim. Adaptasyon, bir canlının yaşadığı çevreye uyum sağlayacak şekilde zamanla geliştirdiği kalıtsal özelliklerdir. Örneğin, kutup ayısının kalın kürkü ya da bukalemunun renk değiştirme yeteneği adaptasyona örnektir. Bu özellikler canlıların hem hayatta kalmasını hem de üremesini kolaylaştırır. Canlıların yaşaması için madde alışverişi çok önemli. Hücreler bazen bu işi enerji harcayarak yapar. İşte buna aktif taşıma diyoruz. Bu mekanizma sayesinde hücre, ihtiyaç duyduğu maddeleri yoğunluk farkına rağmen içeri alabilir. Amfibiler dediğimiz canlılar hem suda hem karada yaşayabiliyor. Kurbağalar buna güzel bir örnek. Hayatlarına suda başlıyorlar, solungaç solunumu yapıyorlar; sonra kara yaşamına geçince akciğer ve deri solunumu yapıyorlar. Ayrıca başkalaşım geçiriyorlar yani ergin hale gelene kadar önemli yapısal değişiklikler yaşıyorlar. Sürüngenlerde, kuşlarda ve memelilerde embriyonun geliştiği özel bir yapı var: amniyon kesesi. Bu kese sıvı dolu ve embriyoyu dış etkilere karşı koruyor. Embriyo bu sayede daha güvenli bir ortamda gelişimini sürdürebiliyor. Bilimsel çalışmalarda verileri toplamak işin sadece ilk adımıdır. Bu verileri yorumlayarak sonuca ulaşma süreci, yani analiz yapıp çıkarımda bulunma kısmı, bilimsel düşüncenin temel taşlarından biridir. Eğer veriler hipotezi desteklemiyorsa hipotezi revize etmek gerekir. Tam tersine destekliyorsa sonuçlar paylaşılır, raporlanır. Bazı canlılar var ki biz onlara 'aşırı koşullarda yaşayanlar' diyoruz. Bunlar arkeler. Çok sıcak, çok tuzlu, çok asidik ya da oksijensiz ortamlarda rahatlıkla yaşayabilirler. Bu yönleriyle diğer prokaryotlardan ayrılırlar. Hatta bu özellikleri sayesinde endüstride ve biyoteknolojide bile kullanılıyorlar. Laboratuvarda bazı testler yapılırken maddelerin varlığını göstermek için ayıraçlar kullanırız. Bunlar belirli maddelerle tepkimeye girip renk değiştirir. Örneğin, nişasta için iyot çözeltisi kullanılır ve ortamda nişasta varsa mavi-mor bir renk oluşur. Bazal metabolizma diye bir kavram var, bu da dinlenme halindeyken bile vücudumuzun çalışması için gereken minimum enerji miktarı. Kalp atışımız, nefes almamız, vücut ısımızın korunması gibi işlevler için bu enerji gerekir. Gazların hücre zarından geçişi bazen çok basit bir şekilde olur. Enerji harcanmaz. Bu olaya basit difüzyon denir. Örneğin oksijenin hücreye girişinde böyle bir geçiş söz konusudur. Bakteriler, prokaryot hücre yapısına sahip canlılardır. Zarla çevrili çekirdekleri yoktur. Ama bu basit yapılı olmaları onları önemsiz yapmaz. Bazıları hastalıklara neden olurken bazıları da doğada organik maddelerin ayrışmasında görev alır."
aramainp = "BURAYA"
kaynak = {}
for filename in os.listdir(source_folder+"/"+ders):
    file_path = os.path.join(source_folder,ders, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        kaynak[filename] = data
print(kaynak)
morphology = TurkishMorphology.create_with_defaults()

def tokenize(cumle):
    tokens = cumle.split()
    return tokens

def kavramkokal(kelime):
    results = morphology.analyze(kelime)
    kok = kelime
    for result in results:
        kok = result.get_stem()
        break
    return kok
def kelimekokal(kelime):
    results = morphology.analyze(kelime)
    kok = ""
    for result in results:
        kok = result.get_stem()
        break
    return kok if kok else ""

tanitilantanimlar = []
baski = 1
kavramlar = {}
#aramainpfiltre

for konu,bilgi in kaynak.items():
    for kavram, veri in bilgi.items():
        time.sleep(0.001)
        for kelime in tokenize(aramainp):
            time.sleep(0.001)
            if tanitilantanimlar.__contains__(kavram):
                continue
            gec = False
            gecc = False
            if len(tokenize(kavram)) > 1:
                if str.lower(kavram) == str.lower(kelime) or str.lower(kelimekokal(kelime)) == str.lower(kavram):
                    gec = True
            else:
                if str.lower(kavramkokal(kavram)) == str.lower(kelime) or str.lower(kelimekokal(kelime)) == str.lower(kavramkokal(kavram)):
                    gec = True
            if gec == True:
                if kavram not in kavramlar:
                    kavramlar[kavram] = 1
                else:
                    kavramlar[kavram] += 1
                if kavramlar[kavram] >= baski:
                    gecc = True
            if gecc == True:
                tanitilantanimlar.append(kavram)
                if "tanım" in veri:
                    print("||||||||||||||||||||||")
                    print(f'Tanım: {veri["tanım"]}')
                    print("||||||||||||||||||||||")
                    aramainp = aramainp + " " + veri["tanım"]
                if "ek_bilgi" in veri:
                    for ekbilgi in veri["ek_bilgi"]:
                        print(f'Ek Bilgi: {ekbilgi}')
                        aramainp = aramainp + " "+ ekbilgi
### Sıralama
