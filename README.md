# GitHub Pages için statik site

Bu klasör, GitHub Pages üzerinde yayınlamak için hazır bir statik site yapısı içerir.

## Adımlar

1. Bu dosyaları GitHub üzerindeki depoya yükleyin.
2. GitHub deposunda Settings > Pages bölümüne gidin.
3. Source olarak "GitHub Actions" seçin.
4. Değişiklikleri ana branche push ettiğinizde deployment otomatik başlayacaktır.

## Yerelde kontrol etmek için

```bash
python3 -m http.server 8000
```

Ardından tarayıcıda http://localhost:8000 adresini açın.
