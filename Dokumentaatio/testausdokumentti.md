# Testausdokumentti

### yksikkötestaus:

Luokille Menu, Play ja SinglePlayer sekä toiminnallisuuksille mm_ab ja gameplay on tehty yskikkötestausta. Ulkopuolelle olen jättänyt kaikki UI-luokat, niiden vastatessa pääosin vain pelin ulkomuodosta. Testien suorittamiseen ohjeet löytyvät alempaa tiedostosta. Sovellus on tehty Liuxilla ja sitä on myös testattu vain linux-ympäristössä. Toinen ympäristö saattaa vaikuttaa etenkin manuaalisen testauksen toimivuteen huomattavasti. Testit on tehty Unittest-työkalulla, jonka käyttö ohjeistettiin ohjelmistotekniikka-kurssilla. Jokainen testi testaa tiettyä toiminnallisuutta ja jokaista tarvittavaa ohjelman toiminnallisuutta on pyritty testaamaan. Mikäli testi näyttää virhettä, olen hyödyntänyt sen palautusta korjatessani huomattua ongelmaa. Tärkeimpänä testattavana olen pitänyt gameplayn ja minmaxin testaamista eriaisia testejä tekemällä, sekä palautusen toimivuutta manuaalisesti. testien suorittaminen vie aikaa noin 1,4 sekuntia.

### Lopullinen kattavuusraportti:
![coverage](https://github.com/seppaemi/tiralabra-s2022/blob/main/Dokumentaatio/kuvat/coverage_week_six.png)

Testikattavuus on ohjelman palautuksen kohdalla 77%. Kattavuus voisi olla korkeampi, mutten nähnyt tapeelliseksi testata esimerkiksi single- ja multiplayereissä samaa asiaa molemmista luokista tai funktioita jotka ovat tehty vain kutsuttaviksi. Myös frontpagen testaaminen on vajavaista koska pääasiassa se vain kutsuu tarvittavaa Play-luokkaa, eikä niinkään vastaa ohjelman toiminnasta. Kuitenkin tärkeimmät, kuten gameplay joka vastaa pelin toiminnasta ja mm_ab joka vastaa minmaxin toiminnasta on testattu tarkasti. Kaikki toimintalogiikan algoritmit toimivat testien perusteella oikein.
Jokaiselta viikolta on mahdollista löytää testikattavuusraportti, viikon raportin loppuosasta. Viikolla 5 sattui pikku kömmähdys, jolloin testikattavuus tippui 17%. Tämä oli kuitenkin nopeasti korjattavissa. 

### testien suorittaminen ja kattavuusraportti:
Yksikkötestit voi suorittaa komennolla **poetry run invoke test**
Testikattavuusraportin voi luoda komennolla **poetry run invoke coverage-report**
jonka jälkeen suorittaa **coverage html**
Tämä luo testikattavuusraportin juurihakemiston tmlcov kansioon. Kattavuusraportti löytyy index.html tiedostosta, jonka voi avata esimerkiksi komennolla **google-chrome index.html**

### Manuaalinen testaus:
Pelejä tehdessä on erittäin tärkeää manuaalisesti testata pelin toimintaa, joten olen pelannut tätä huomattavan plajon projektin edetessä sekä palautellut arvoja lähes jokaisen funktion kohdalla, eplin edetessä. Tärkein manuaalisen testauksen kohde on ollut graafisen käyttöliittymän toiminta, sekä minmaxin oikeanlainen suoritus. Olen itse pelannut peliä mahdollisimman hyvin, huonosti sekä vain räiskien vähän minne sattuu. Olen pakottanut ystäviäni ja vanhempiani pelaamaan, jotta voisin nähdä mahdollisimman hyvin tekoälyn toimintaa erilaisten vastusten kanssa. Peliä on siis testannut lapset, aikuiset, shakkimestari, ihminen joka ei koskaan pelaa mitään ja sekalainen joukko kaikkea siltä väliltä. Pelin toiminta on siis manuaalisesti ainakin tarkasti testattu ja olemme todenneet voittojen ja tappioiden avulla miten tekoäly toimii ja tein parannuksia sen mukaan ohjelman edetessä.

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

### Havainnot suorituskykytesteistä:
Käytin jokaiselle vaikeustasolle otoskokoa 7, mutta suhteet pysyivät aika samoina myös muilla arvoilla. Keskimäärin tietokone pohdiskeli siirtoa 7-sekunnin verran jokaisella tasolla. aikojen vaihtelu tasojen välillä oli kuitenkin suurta:
helppo: 0,00892
medium: 0,08751
vaikea: 0,61717
On helppo todeta että tason noustessa aika, jonka tekoäly käyttää pohdintaan kasvaa eksponentiaalisesti.
