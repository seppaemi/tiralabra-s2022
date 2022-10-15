# Testausdokumentti

### Mitä olen testannut:

Luokille Menu, Play ja SinglePlayer sekä toiminnallisuuksille mm_ab ja gameplay on tehty yskikkötestausta. Ulkopuolelle olen jättänyt kaikki UI-luokat, niiden vastatessa pääosin vain pelin ulkomuodosta.

### Kattavuusraportti viikolla kuusi
![coverage](https://github.com/seppaemi/tiralabra-s2022/blob/main/Dokumentaatio/kuvat/coverage_week_six.png)

Testikattavuus on tällä hetkellä puutteellinne, koska en ole testannut pygamea kutsuvia komentoja tai käyttöliittymän metodia kutsuvia funktioita.

### testien suorittaminen ja kattavuusraportti:
Yksikkötestit voi suorittaa komennolla **poetry run invoke test**
Testikattavuusraportin voi luoda komennolla **poetry run invoke coverage-report**
jonka jälkeen suorittaa **coverage html**
Tämä luo testikattavuusraportin juurihakemiston tmlcov kansioon. Kattavuusraportti löytyy index.html tiedostosta, jonka voi avata esimerkiksi komennolla **google-chrome index.html**

## Suorituskykyestaus:
Tekoälyn siirron keskinopeutta voi testata komentorivillä komennolla **poetry run invoke prformance**
### Suorituskykytestien toiminta:
- Komentoriviltä annetaan komento joka kertoo millä tasolla ohjelmaa testataan
**h** on helppo
**m** on medium
**v** vaikea
- Sen jälkeen komentoriville annetaan otoskoko, joka annetaan kokonaislukuarvona.
- Ohjelma tulostaa vastauksessa keskiarvon ja varianssin
- Ohjelma sammuu antamalla komento **q**
