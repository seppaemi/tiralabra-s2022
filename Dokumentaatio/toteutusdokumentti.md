# Toteutusdokumentti

## Ohjelman rakenne:
Connect four-ohjelmassa pelataan tietokonetta (tai kaveria) vastaan. Tietokoneen tekoäly on tehty minmax-algortimilla ja sitä on tehostettu alpha-beta karsinnalla. Peli alkaa pelaajan siirrolla, jossa hän valitsee haluamansa sarakkeen. Tekoäly laskelmoi voiton mahdollisuuden jokaisella siirrolla ja pyrkii tekemään parhaimman mahdollisen siirron, voittoa tavoittelevasti. Tekoäly olettaa että pelaaja pelaa myös optimaalisimmalla tavalla. 

Ohjelma koostuu pythonilla ohjelmoiduista käyttöliittymästä ja sovelluslogiikasta. Käyttöliittymä on toteutettu pygamella, joka on pythonin kirjasto etenkin pelien käyttöliittymän toteuttamiseen. Sovelluslogiikka löytyy pääasiassa src/modules, jossa on erillisiä tiedostoja. Tiedostoihin on toteutettu kutsuttavia luokkia tai/ja funktioita, joiden toimintaan ohjelma perustuu. Ohjelma käynnistyy index.py tiedostosta, joka kutsuu graafista käyttöliittymää.
Kuva graafisesta käyttöliitymästä:
![connectfour](https://github.com/seppaemi/tiralabra-s2022/blob/main/Dokumentaatio/kuvat/connectfour_friend.png)

### Aika ja tilavaativuudet:
Mikäli minmax-karsinta pystyy hyödyntämään alpha-beta karsintaa, on työn aikavaatimus O(sqrt(b^d)), jossa b on haarautuminen ja d haun syvyys. Pelissä on seitsemän vaihtoehtoista saraketta. jolloin b=7. Pelissä on kolme tasoa, joiden syvyydet ovat

helppo=2

medium=4

vaikea=6

jolloin jokin näistä valikoituu syvyydeksi, tasosta riippuen. Pahimmillaan siis minmaxia ja alpha betaa käyttämällä aikavaativuudeksi muodostuu O(sqrt(7⁶)) ja parhaimmillaan O(sqrt(7²)).
Mikäli koko puu tulee käydä läpi, eli alpha betaa ei voida hyödyntää, on aikavaatimus O(b^d), joka on siis pahimmillaan O(7⁶) ja parhaimmillaan O(7²).

Connect fourin algoritmi on rekursiivinen eli se varaa muistista tilaa rekursiohaaraa varten ja vapauttaa sitä aina päättymishaarassa. Rekursiiviset algoritmit eivät vaadi tietorakennetta joka ylläpitäisi suurta määrää niiden tallentamaa tietoa. Algoritmi ei siis tallenna tietoa kuin hetkittäin, ja silloinkin tallennetaan vain jokaiselle haarautumalle yksi arvo. Aikavaativuuden tavalla tilavaatimus on siis O(b*d) jossa b on haarautumien määrä ja d on haun syvyys.

### Puutteet ja parannusideat:
- Minmaxin toimintaa voisi nopeuttaa, esimerkiksi board_calc-funktiota tehostamalla. Tällöin ohjelma toimisi suuremmilla syvyyksillä nopeammin ja syvyyttä olisi mahdollista kasvattaa.
- Käyttäjää varten olisi ollut hauska tallentaa voittotiedot tietokantaan, jolloin pelituloksista olisi helppo pitää kirjaa.
- Mahdollinen vinkkaaja-algoritmi, joka toimisi samoin kuin tekoäly ja pelaaja voisi hyödyntää sitä vaikka kerran koko pelin aikana antamaan vinkin parhaaseen mahdolliseen siirtoon.

### Lähteet:
Wikipedia (FI), [Neljän suora](https://fi.wikipedia.org/wiki/Nelj%C3%A4n_suora)

Hussain Syed, Hameed Usman, [Minimax with alpha-beta pruning (Connect-4 game)](https://www.academia.edu/41561708/Minimax_with_alpha_beta_pruning_connect_4_game_)

GeeksForGeeks, [Minmax algorithm ni game theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)

Gilles Vandewiele, [Creatin the (nearly) perfect connect-four bot with limited move time and file size](https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0)

Johdatus tekoälyyn, [IntToAi](https://materiaalit.github.io/intro-to-ai/part2/)

Youtube video, [youtube video](https://www.youtube.com/watch?v=m1l3k_rcG0M)

Gamesolver.org, [gamesolver.org](http://blog.gamesolver.org/solving-connect-four/01-introduction/)

#### Kuvalähteet:
Kaikki peliin tehty grafiikka on itse piirrettyä picsart sovelluksella.