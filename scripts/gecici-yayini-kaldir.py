#!/usr/bin/env python3
"""Geçici "site yenileniyor" yayınını kaldırır.

Ne yapar:
  1. hakkimizda.html / hizmetler.html / iletisim.html içindeki
     "GEÇİCİ YÖNLENDİRME" bloklarını siler (sayfalar yeniden normal açılır).
  2. index.html için ne yapılması gerektiğini hatırlatır (otomatik değiştirmez).

Kullanım:
    python3 scripts/gecici-yayini-kaldir.py            # değişiklikleri uygular
    python3 scripts/gecici-yayini-kaldir.py --kontrol  # sadece ne yapacağını gösterir
"""
import io
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAYFALAR = ['hakkimizda.html', 'hizmetler.html', 'iletisim.html']
BLOK = re.compile(
    r'[ \t]*<!-- ==== GEÇİCİ YÖNLENDİRME.*?<!-- ==== /GEÇİCİ YÖNLENDİRME ==== -->\n',
    re.S)


def main():
    kontrol = '--kontrol' in sys.argv
    degisen = 0
    for ad in SAYFALAR:
        yol = os.path.join(KOK, ad)
        s = io.open(yol, encoding='utf-8').read()
        yeni, adet = BLOK.subn('', s)
        if not adet:
            print('  atlandı  %-16s (yönlendirme bloğu yok)' % ad)
            continue
        if kontrol:
            print('  silinecek %-16s (%d blok)' % (ad, adet))
        else:
            io.open(yol, 'w', encoding='utf-8').write(yeni)
            print('  temizlendi %-16s (%d blok)' % (ad, adet))
        degisen += 1

    print()
    print('index.html HÂLÂ geçici sayfadır. Seçenekler:')
    print('  - Yenilenen ana sayfa hazırsa onu index.html olarak koyun.')
    print('  - Yenileme öncesi ana sayfaya dönmek için:')
    print('      git checkout 2dea786 -- index.html')
    print()
    print('gecici-sayfa.html depoda kalır; ileride tekrar gerekirse:')
    print('      cp gecici-sayfa.html index.html   (sonra noindex satırını silin)')
    print()
    print('Son adım: CHANGELOG.txt -> "Yayın durumu" maddelerini [x] yapıp')
    print('tarihli bölüme taşıyın.')
    if kontrol:
        print('\n(--kontrol modu: hiçbir dosya değiştirilmedi)')
    return 0 if degisen or kontrol else 0


if __name__ == '__main__':
    sys.exit(main())
