# Viikkoraportti 3
## Käytetty aika:
14,5h

## Mitä tein: 
Selkeää oli itselle heti alussa, että nyt alan tekemään minmax-algoritmia ja sitä parantelen alpha-beta karsinnalla. Tein tiedoston mm_ab.py. Olin jo viime viikolla alkanut lukemaan miten tätä tedään ja iloinen yllätys oli, että samaan aikaan käymälläni Introduction To Ai kurssilla käytiin näitä myös läpi. Lopulta sain omasta mielestäni aika toimivaa algoritmia tehtyä. Tähän apuna käytin IntToAI kurssilla tekemääni TikTakToe tehtävää, johon piti myös käyttää samanlaisia toimia, [samaisen kurssin materiaaleja](https://materiaalit.github.io/intro-to-ai/part2/), [youtube videota](https://www.youtube.com/watch?v=m1l3k_rcG0M) sekä [gamesolver.org ohjeita](http://blog.gamesolver.org/solving-connect-four/01-introduction/). Eniten aikaa meni juuri perehtymiseen, jonka jälkeen algoritmin tekeminen ei ollutkaan kovin haastavaa! Kirjoittelin vielä kaikkeen kommentit ja korjailin pylint-virheitä. Koitin parhaani mukaan taas codecovin käyttöönottoa, mutten onnistunut siinä millään; ehkä ensi viikolla sitten parempi tuuri. Coverage on sitten taas tämän tiedoston pohjalla :) Tein myöskin kaksi testiä juuri tehdylle algoritmille.

## Ohjelman edistyminen
Ohjelman kannalta ollaan hyvällä saralla. Mitään tämän viikon uutuuksia ei ole vielä näkyvillä ohjelmaa suorittaessa, mutta taustalla tapahtui kuitenkin paljon ja ohjelma laajeni suuresti. Multiplayer osio toimii edelleen hyvin, enkä siihen keksi enää muuta lisättävää. 

## Mitä opin:
Minmax algoritmi oli jo aiemmin selkeää, mutta alpha-betan yhdistäminen siihen taas ei. Tällä viikolla sain selkeytettyä tätä itselleni todella hyvin!

## Epäselvyydet ja haasteet:
Testaaminen on selkeästi itselleni haasteellista ja tuntuu jäävän hieman taka-alalle. Kiva oli kuitenkin huomata että vielä viime viikolla epäselvä tekoäly on alkanut kirkastua! Haastavaa on ehkä itselleni juuri ajan käyttö. Aikaa menee joka viikko paljon kun innostun tutkimaan uusia lähteitä ja tapoja tehdä. Olen kuitenkin edistynyt mielestäni aika hyvin, joten saattaa olla että lopuilla viikoista aikaa tulee käytettyä vähemmän tutkimiseen, jolloin myös viikkoajat ovat pienempiä.

## Mitä seuraavaksi:
- Testaamista paljon lisää!! Saattaa olla että käytän pääosin siihen koko ensi viikon jotta saan testit jokaisesta nykyisestä luokasta ajantasalle.
- Tekoälyn liittäminen graafiseen käyttöliittymään. Haluan että vertaisarvioinnissa voisi pelata tekoälyä vastaan edes helpolla tasolla, joten jos aikaa riittää, haluan sen valmiiksi!
- Ehkä testikattavuus esitettävään muotoon.

## Testikattavuusraportti tältä viikolta:
![coverage](https://github.com/seppaemi/tiralabra-s2022/blob/main/Dokumentaatio/kuvat/cov_report_vko3.png)
