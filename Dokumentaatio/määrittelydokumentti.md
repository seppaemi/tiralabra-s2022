## Määrittelydokumentti
**Opinto-ohjelma**: Tietojenkäsittelytieteen kandidaatti

**Ohjelmointikieli**: Python

**Dokumentaation kieli**: Suomi (vertaisarviointi sujuu myös englanniksi ja ruotsiksi)

### Aihe
Connect-four peli on kahden pelaajan peli 7x6 kokoisella pelilaudalla. Laudalle tiputetaan vuorotellen oma pelinappula, tavoitteena yhdistää ensin neljä nappulaa joko pystyyn, vaakaan tai viistoon. Tavoitteenani on luoda pygamella peli, jota voi pelata joko kaverin kanssa tai tekoälyä vastaan, mahdollisesti useammalla tasolla. 

### Käytettävät algoritmit
Tekoäly luodaan, jotta pelaaja voi pelata myös yksin. Sen tavoitteena on tehdä joka kerta mahdollisimman hyvä siirto itselleen. Tekoälyn luomiseen ajattelin käyttää minmax-algoritmia, jota tehostan alpha-beeta karsinnalla. Näin saan karsittua binääripuun haaroja, joka nopeuttaa tekoälyn toimintaa.

### Aika- ja tilavaativuusarvio:
Alpha-beta karsinnalla aika-arvion pitäisi olla O(sqrt(b^d)), missä d on minmaxin syvyys ja b lukuarvi, joka kuvaa kuinka moneen solmuun kukin puun solmu haarautuu. Tekoälyn siirtojen on tarkoitus olla mahdollisimman nopeita, vaikka ne tulevat hidastumana vaikeuden noustessa.

### Lähteet
Wikipedia (FI), [Neljän suora](https://fi.wikipedia.org/wiki/Nelj%C3%A4n_suora)

Hussain Syed, Hameed Usman, [Minimax with alpha-beta pruning (Connect-4 game)](https://www.academia.edu/41561708/Minimax_with_alpha_beta_pruning_connect_4_game_)

GeeksForGeeks, [Minmax algorithm ni game theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)

Gilles Vandewiele, [Creatin the (nearly) perfect connect-four bot with limited move time and file size](https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0)