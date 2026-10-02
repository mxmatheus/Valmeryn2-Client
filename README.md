# Valmeryn2 Client

Valmeryn2 istemcisinin çalışma dosyaları, arayüz betikleri, locale verileri ve paketlenecek oyun asset'leri.

## Bileşenler

- `assets/`: Python UI dosyaları, locale/proto dosyaları ve paketlenecek grafik/ses içerikleri.
- `Metin2.exe`: mevcut temel istemci çalıştırılabilir dosyası. Yeni client source derlemesiyle uyumlu sürümü kullanılmalıdır.
- `config.exe`: istemci görüntü ve başlatma ayarları.

İlgili kaynak: `Valmeryn2-Client-Src`.

## İlk istemci kurulumu

1. Client source deposunu Windows'ta CMake ve Visual Studio C++ araçlarıyla derleyin.
2. Sunucu deposundaki güncel `item_proto` ve `mob_proto` dosyalarını, istemcinin `assets/locale` ağacındaki ilgili locale dizinlerine dağıtın.
3. Yerel geliştirme için `assets/root/serverinfo.py` şu portları kullanır: auth `127.0.0.1:24000`, CH1 `24011`, CH2 `24021`.
4. Yalnızca sunucu listesini değiştirdiyseniz `assets` altında `python pack.py root` çalıştırıp `pack/root.pck` paketini yenileyin. Diğer asset'ler de değiştiyse `python pack.py --all` kullanın.
5. Aynı revizyondan üretilmiş client executable ve paketlerle giriş akışını doğrulayın.

Veritabanı portu `3309` istemci bağlantı portlarından ayrıdır; client `serverinfo.py` içine yazılmaz.

## Giriş ve karakter seçimi görselleri

- Giriş: `assets/ETC/ymir work/ui/intro/login/login.jpg`
- Karakter seçimi: `assets/ETC/ymir work/ui/intro/select/select.jpg`

İki dosya da 1024×1024 JPEG'tir. Eşlik eden `.sub` tanımları 1024×768 alanı örnekler. Kaynak dosyalarındaki yeni Valmeryn görselleri bu hedeflere yerleştirilmiştir; oyundaki kadrajı paketleme sonrası kontrol edin.

## Özellik geliştirme durumu

`YENI_PROJE_DEVIR_RAPORU.md` önceki çalışmadan gelen sistem kataloğu ve doğrulama notlarıdır. Bu çalışma kopyaları temiz M2Dev ana dalından başlıyor; katalogdaki sistemler burada henüz entegre kabul edilmemelidir. Her sistem kaynak, paket ve oyun içi kontrol tamamlandıkça bu README güncellenecektir.
