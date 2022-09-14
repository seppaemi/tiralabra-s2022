# Viikkoraportti 2:
## Käytetty aika:
13 h

## Mitä tein:
Viimeviikosta oli jäänyt todella hyvä paikka jatkaa, joka helpotti tällä viikolla! Tein menulle graafisen käyttöliittymän ja loin luokan Play() multiplayeriin. Multiplayerin osalta ohjelma on jo valmis, koska käyttäjä pystyy nyt vaikka pelaamaan kaveria vastaan. Aloitin testaamaan menua (jonka kaikki testit passed) ja multiplayeria (josta osassa testeistä bound-metod ongelma. En aivan päässyt jyvälle mitä tein väärin, mutta palaan tähän ensi viikolla.) Tein pylintillä koodille laatutarkastuksia ja korjasin laadullisia ongelmia ja siistin yleisesti koodia. Kommentoin myös kaiken tähänastisen koodin modulesista, testsistä ja UI:sta. Kattavuusraportille ne ehtinyt vielä keksiä mitään, koitin codecovia mutten päässyt jyvälle sen toiminnasta. Tässä kuitenkin alla sitten tältä viikolta kattavuusraportti. Lueskelin loppuviikosta myöskin alfabeetasta ja minmax algoritmista jo valmiiksi jotta pääsee helposti alkuun ensiviikolla. 

## Ohjelman edistyminen:
Mielestäni ohjelma on erinomaisella mallilla ja on editynyt hyvin! Tosiaan multiplayer-toiminto on täydessä toiminnassa eikä siihen täydy enää tehdä muuta! Ohjelma aukeaa virtuaaliympäristössä komennolla **poetry run invoke start** ja käyttäjä pääsee sieltä menu-valikkoon. Valikosta toimii vasta pelaaminen kaveria vastaan, jossa pelaajat ovat vihreä ja punainen pelimerkki ja he voivat tiputella merkkejään ruudukkoon. Peli päättyy joko tasapeliin, vihreän voittoon tai punaisen voittoon. Sitten sen voi aloittaa alusta halutessaan.

## Mitä opin:
Oppiminen oli ehkä vähäisempää kuin edellisellä viikolla, koska pygamen käyttö ja poetry-ohjelmien kehittäminen on jo itselleni tuttua puuhaa. Kuitenkin opin jonkin verran multiplayer-pelimuotoa tehdessä vuorojen vaihtamisesta ja siitä, kuinka matriisista voidaan löytää voittaja mihinkin suuntaan! Opin myös vähän lisää minmax-algoritmista ja alfabeeta karsinnasta, vaikka ne jäivätkin vielä vähän epäselviksi.

## Epäselvyydet ja haasteet
Suurin haaste on ollut pienten ja turhien asioiden debugaaminen. Tekoälyn luominen on edelleen itselleni harmaata aluetta, mutta uskon että ensi viikolla kun pääsee tositoimiin sitä tehdessä, on helpompi ymmärtää oppimaani soveltamalla.

## Mitä seuraavaksi:
- Minmax-algoritmin luomista. Olen onneksi omaa aikatauluani hieman edellä joten sen tekemiselle olen varannut hyvin aikaa ja aion edetä aika varovaisesti.
- Testaamisen lisääminen ja testikattavuuden nostaminen. Aion korjata testit jotka eivät nyt mene läpi ja lisätä testejä luokille, joilla niitä ei ole. 
- Jos jää aikaa niin singleplayerin kehittely
- Testikattavuus esitettävään muotoon :)

## Testikattavuusraportti tältä viikolta:
![coverage](https://github.com/seppaemi/tiralabra-s2022/blob/main/Dokumentaatio/coverage_w2_tira.png)
