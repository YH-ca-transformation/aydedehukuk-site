# GitHub Pages için statik site

Bu klasör, GitHub Pages üzerinde yayınlamak için hazır bir statik site yapısı içerir.

## Adımlar

1. Bu dosyaları GitHub üzerindeki depoya yükleyin.
2. GitHub deposunda Settings > Pages bölümüne gidin.
3. Source olarak "GitHub Actions" seçin.
4. Custom domain olarak "aydedehukuk.com" yazın.
5. Değişiklikleri ana branche push ettiğinizde deployment otomatik başlayacaktır.

## GoDaddy DNS ayarları

GitHub Pages için alan adınızı kullanmak üzere GoDaddy panelinizde şu kayıtları ekleyin:

- Tip: A
  - Değer: 185.199.108.153
- Tip: A
  - Değer: 185.199.109.153
- Tip: A
  - Değer: 185.199.110.153
- Tip: A
  - Değer: 185.199.111.153

- Tip: CNAME
  - Ad: www
  - Değer: <kullanici>.github.io

Örnek olarak:
- Ana alan adı: aydedehukuk.com
- www alt alanı: www.aydedehukuk.com

DNS kayıtları yayıldıktan sonra GitHub Pages panelinde "Check DNS" işlemini bekleyin.

## Yerelde kontrol etmek için

```bash
python3 -m http.server 8000
```

Ardından tarayıcıda http://localhost:8000 adresini açın.
