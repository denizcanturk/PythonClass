import random

# Global değişkenler
para = 0
istikrar = 0
nüfus = 1000
tur_geliri = 0
istikrar_geliri = 1  # Her tur için temel istikrar geliri
researches_in_progress = []

#-------------------------------------------
# Sınıfların düzenlenme ve yazılma şekilleri
# gayet güzel olmuş. Eline sağlık.
#-------------------------------------------

# Olay sınıfı
class Event:
    #-------------------------------------------
    #Constructorlara hangi tipte veri verdiğini belirtmen kullanıcı için daha kolaylık sağlar, aynı zamanda ileride
    # kodda iyileştirme yapmak istediğinde senin için de işleri kolaylaştırır
    #-------------------------------------------
    def __init__(self, name:str, effect:tuple):
        self.name = name
        self.effect = effect

    def trigger(self):
        global para, istikrar, nüfus
        print(f"Olay: {self.name} gerçekleşti!")
        for key, value in self.effect.items():
            if key == "para":
                para += value
            elif key == "istikrar":
                istikrar += value
            elif key == "nüfus":
                nüfus += value
            print(f"{key.capitalize()}: {value}")

# İnşaat sınıfı
class Construction:
    def __init__(self, name, cost, income_increase):
        self.name = name
        self.cost = cost
        self.income_increase = income_increase
        self.level = 0
    
    def build(self):
        global para, tur_geliri
        if para >= self.cost:
            para -= self.cost
            self.level += 1
            tur_geliri += self.income_increase
            print(f"{self.name} inşa edildi! Tur başı gelir +{self.income_increase} para arttı.")
        else:
            print(f"Yeterli para yok. {self.name} inşa edilemedi.")

# Görev sınıfı
class Mission:
    def __init__(self, name, description, cost, reward):
        self.name = name
        self.description = description
        self.cost = cost
        self.reward = reward
        self.completed = False
    
    def complete(self):
        global para, tur_geliri, istikrar_geliri
        if not self.completed:
            if para >= self.cost:
                para -= self.cost
                print(f"Görev '{self.name}' tamamlandı! Para kaybı: {self.cost}")
                self.completed = True
                for key, value in self.reward.items():
                    if key == "tur_geliri_yüzde":
                        tur_geliri += int(tur_geliri * (value / 100))
                        print(f"Tur başı gelir % {value} arttı.")
                    elif key == "inşa_hızı":
                        print(f"Inşa hızı % {value} arttı!")
                    elif key == "istikrar":
                        istikrar += int(istikrar * (value / 100))
                        print(f"İstikrar % {value} arttı.")
                    elif key == "istikrar_geliri":
                        istikrar_geliri += value
                        print(f"Tur başına istikrar +{value} arttı.")
            else:
                print(f"Yeterli para yok. Görev '{self.name}' tamamlanamadı.")
        else:
            print(f"Görev '{self.name}' zaten tamamlanmış.")

# Kronik sorun sınıfı
class ChronicIssue:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity
    
    def worsen(self):
        self.severity += 1
        print(f"{self.name} sorunu kötüleşti! Şiddet: {self.severity}")

    def improve(self):
        global istikrar_geliri
        if self.severity > 0:
            self.severity -= 1
            print(f"{self.name} sorunu iyileşti. Şiddet: {self.severity}")
            istikrar_geliri += 1
            print(f"Tur başına istikrar +1 arttı.")
        else:
            print(f"{self.name} sorunu zaten çözülmüş durumda.")

# Araştırma sınıfı
class Research:
    def __init__(self, name, cost, duration, effect):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.effect = effect
        self.level = 0
        self.progress = 0
    
    def start(self):
        global para
        if para >= self.cost:
            para -= self.cost
            self.progress = self.duration
            print(f"Araştırma '{self.name}' başlatıldı! Bekleme süresi: {self.duration} tur.")
            researches_in_progress.append(self)
        else:
            print(f"Yeterli para yok. Araştırma '{self.name}' başlatılamadı.")
    
    def update(self):
        if self.progress > 0:
            self.progress -= 1
            if self.progress == 0:
                self.level += 1
                print(f"Araştırma '{self.name}' tamamlandı! Seviye: {self.level}")
                for key, value in self.effect.items():
                    if key == "inşa_hızı":
                        print(f"Inşa hızı % {value} arttı!")
                    elif key == "istikrar_geliri":
                        global istikrar_geliri
                        istikrar_geliri += value
                        print(f"Tur başına istikrar +{value} arttı.")
                researches_in_progress.remove(self)
            else:
                print(f"Araştırma '{self.name}' devam ediyor. Kalan süre: {self.progress} tur.")
        else:
            print(f"Araştırma '{self.name}' zaten tamamlandı.")

#-------------------------------------------
#HANDLE_EVENT HAKKINDA 
# Bu fonksiyonu her çağırdığında bu sınıflar için nesneleri her seferinde üretiyor ve 
# içlerinden bir tanesini rastgele kullanıyor. Memory yönetimi açısından uygun bir kullanım 
# şekli değil, o nedenle main loop daki gibi bir event listesi içinde bu değerleri tutabilir
# ve içinden rastgele seçim yapabilirsin. 
# Hali hazırda kod : Her seferinde bu nesneleri yaratıyor, sonra işi bittiği için memory den siliyor
# ve her çağırışında bunu gerçekleştiriyor. 
#-------------------------------------------

# Olayları yönetme
def handle_event():
    events = [
        Event("terör saldırısı", {"para": -500, "istikrar": -40}),
        Event("dış ülkelerden yatırım", {"para": +200}),
        Event("doğal afet", {"para": -250, "nüfus": -50}),
        Event("iç karışıklık", {"istikrar": -40}),
        Event("yeni kaynak keşfi", {"para": +800}),
        Event("büyük göç", {"nüfus": +50, "istikrar": -25}),
        Event("büyük proje tamamlandı", {"para": +150, "istikrar": +10}),
        Event("ekonomik kriz", {"para": -800, "istikrar": -30}),
        Event("savaş tehdidi", {"istikrar": -20}),
        Event("geçit töreni", {"istikrar": +25}),
        Event("büyük tören", {"para": -250, "istikrar": +45}),
        Event("dışardan gelen büyük yatırım", {"para": +800, "istikrar": +15}),     
    ]
    event = random.choice(events)
    event.trigger()

# Geliri hesaplama
def calculate_income():
    global para, istikrar, nüfus, tur_geliri, istikrar_geliri
    # İstikrar 50'nin altındaysa tur başı gelir %35 azalır
    if istikrar < 50:
        tur_geliri = int(tur_geliri * 0.65)
        print("İstikrar 50'nin altında, tur başı gelir %35 azaldı.")
    
    total_income = tur_geliri + (nüfus // 10) + (istikrar // 10)
    para += total_income
    istikrar += istikrar_geliri  # Tur başına istikrar kazancı
    print(f"Bu tur toplam gelir: {total_income} para, Toplam istikrar kazancı: {istikrar_geliri}")

# Ana oyun döngüsü
def game_loop():
    global para, istikrar, nüfus

    civil_factory = Construction("Sivil Fabrika", 250, 100)
    military_factory = Construction("Askeri Fabrika", 300, 150)
    
    # Görev listesi (2 katına çıkarıldı)
    missions = [
        Mission("Ekonomi Büyütme", "Ekonomiyi büyütmek için yatırımlar yapın.", 250, {"tur_geliri_yüzde": 20}),
        Mission("Nüfus Artışı", "Nüfus artışı için sosyal projeler yapın.", 450, {"tur_geliri_yüzde": 15}),
        Mission("İstikrarı Sağla", "İstikrarı sağlamak için reformlar yapın.", 200, {"tur_geliri_yüzde": 25, "istikrar_geliri": 2}),
        Mission("Sosyal Projeler", "Toplum için sosyal projeler yaparak istikrarı artırın.", 100, {"inşa_hızı": 10}),
        Mission("Yatırım Çekme", "Yatırımcıları çekmek için projeler yapın.", 400, {"tur_geliri_yüzde": 30}),
        Mission("Sanayi Gelişimi", "Sanayi alanında yatırımlar yaparak ekonomiyi büyütün.", 800, {"tur_geliri_yüzde": 10}),
        Mission("Eğitim Reformu", "Eğitim sisteminde reformlar yaparak verimliliği artırın.", 500, {"inşa_hızı": 15}),
        Mission("Sağlık Yatırımları", "Sağlık sektörüne yatırım yaparak yaşam kalitesini artırın.", 600, {"tur_geliri_yüzde": 20}),
        Mission("Tarım Destekleme", "Tarım sektörüne destek vererek gıda güvenliğini artırın.", 450, {"tur_geliri_yüzde": 12}),
        Mission("İş Gücü Artışı", "İş gücünü artırmak için çeşitli projeler yapın.", 500, {"inşa_hızı": 20}),
        Mission("propoganda çalışmaları","istikrarı arttırmak için hükümet yanlısı propoganda yapın.", 260,{"istikrar": 25}),
    ]

    # Kronik sorunlar listesi (2 katına çıkarıldı)
    chronic_issues = [
        ChronicIssue("Yolsuzluk", 3),
        ChronicIssue("Eğitim Sorunu", 2),
        ChronicIssue("Sağlık Sorunu", 1),
        ChronicIssue("İşsizlik", 4),
        ChronicIssue("Altyapı Sorunu", 3),
        ChronicIssue("Çevre Kirliliği", 2),
        ChronicIssue("Güvenlik Sorunu", 1),
        ChronicIssue("Enerji Krizi", 2),
    ]

    # Araştırma listesi
    researches = [
        Research("İnşaat Hızı Arttırma", 240, 5, {"inşa_hızı": 20, "istikrar_geliri": 1}),
        Research("Ekonomi Araştırmaları", 300, 6, {"tur_geliri_yüzde": 15}),
        Research("Teknoloji Geliştirme", 250, 4, {"inşa_hızı": 15, "istikrar_geliri": 1}),
        Research("Eğitim Yatırımları", 200, 7, {"inşa_hızı": 10}),
        Research("Sağlık Araştırmaları", 270, 5, {"inşa_hızı": 25}),
        Research("Tarım Teknolojileri", 220, 6, {"tur_geliri_yüzde": 20}),
    ]

    while True:
        print("\nMevcut Durum:")
        print(f"Para: {para}, İstikrar: {istikrar}, Nüfus: {nüfus}, Tur başı gelir: {tur_geliri}")
        print("1. Olayları ele al")
        print("2. İnşa")
        print("3. Görevleri tamamla")
        print("4. Kronik sorunları yönet")
        print("5. Araştırma yap")
        print("6. Oyundan çık")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            handle_event()
        elif choice == "2":
            print("1. Sivil Fabrika")
            print("2. Askeri Fabrika")
            build_choice = input("İnşa edilecek yapıyı seçin: ")
            if build_choice == "1":
                civil_factory.build()
            elif build_choice == "2":
                military_factory.build()
            else:
                print("Geçersiz seçim.")
        elif choice == "3":
            print("Görevler:")
            for idx, mission in enumerate(missions, start=1):
                print(f"{idx}. {mission.name} - {mission.description} (Maliyet: {mission.cost})")
            mission_choice = input("Tamamlanacak görevi seçin: ")
            try:
                mission_choice = int(mission_choice) - 1
                if 0 <= mission_choice < len(missions):
                    missions[mission_choice].complete()
                else:
                    print("Geçersiz seçim.")
            except ValueError:
                print("Geçersiz seçim.")
        elif choice == "4":
            print("Kronik Sorunlar:")
            for idx, issue in enumerate(chronic_issues, start=1):
                print(f"{idx}. {issue.name} - Şiddet: {issue.severity}")
            issue_choice = input("Çözmek istediğiniz kronik sorunu seçin: ")
            try:
                issue_choice = int(issue_choice) - 1
                if 0 <= issue_choice < len(chronic_issues):
                    action = input(f"{chronic_issues[issue_choice].name} sorununun şiddetini azaltmak için (1: İyileştir, 2: Kötüleşsin) seçin: ")
                    if action == "1":
                        chronic_issues[issue_choice].improve()
                    elif action == "2":
                        chronic_issues[issue_choice].worsen()
                    else:
                        print("Geçersiz seçim.")
                else:
                    print("Geçersiz seçim.")
            except ValueError:
                print("Geçersiz seçim.")
        elif choice == "5":
            print("Araştırmalar:")
            for idx, research in enumerate(researches, start=1):
                print(f"{idx}. {research.name} - Maliyet: {research.cost}, Bekleme süresi: {research.duration} tur")
            research_choice = input("Başlatmak istediğiniz araştırmayı seçin: ")
            try:
                research_choice = int(research_choice) - 1
                if 0 <= research_choice < len(researches):
                    researches[research_choice].start()
                else:
                    print("Geçersiz seçim.")
            except ValueError:
                print("Geçersiz seçim.")
        elif choice == "6":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim")

        # Araştırma ilerlemesini güncelle
        for research in researches_in_progress:
            research.update()

        calculate_income()

game_loop()
#-------------------------------------------
# Game loop da income hesabı sadece ben bir secimde bulunursam gerçekleşiyor. 
# Bunu her 10 dk da bir parayı artıracak şekilde düzenlemen daha hoş olur.
# Arka arkada 10 kere basarsam, hiç bir şey yapmadan para artırmış olabilirim :)

# Mevcut durumu görüntüleyecek bir seçenek güzel olur
#   - Tur başı kazancım ne kadar
#   - Giderim ne kadar
#   - Mevcut sorunlarım neler
#   - Gelişmişlik durumum ne kadar vs vs ...
# Evet var farkındayım, listenin başında var, ancak ekra sürekli arka arkaya yazdığı
# için takibi zorlaştırıyoru. Ekranı temizleyip seçenekleri yazdırmayı deneyebilirsin.

# class kullanılarak (Nesne Yonelimli Programlama) yapılan yazılım geliştirme süreci
# Aynı zamanda nesnelerin birbileri ile de etkileşimleri nedeni ile diğer programlama
# türlerinden üstündür. Bu konuda da ilavelerde bulunabilirsin

# Ben oyunu kapatıp açtığımda, her şeye yeniden başlıyorum :(
# Oyunda bir level yönetimi, daha önce gelinmiş seviyenin ve para miktarının oyunun 
# yeniden açılması ile birlikte kaldığım yerden devam etmemi sağlayacak şekilde düzenlenmesi
# daha keyif verici olur. Bunun için bir config dosyası kullanabilirsin... json olur, düze text dosyası olur, xml olur... 
#hangisini denemek istersen... 

# Ellerine sağlık. Kolay gelsin.
#-------------------------------------------