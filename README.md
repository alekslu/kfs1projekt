# JSON konverter
Projekti mõte on luua JSON konverter, mis:
1) Võtab UI kaudu sisse JSON faili;
2) Kuvab JSONi kasutajaliidesel
3) Kuvatud JSONist on võimalik filtreerida välja ainult soovitud elemendid
   3.1) Seda saab teha nt kuvatud JSONi elemendil topeltklikiga või esialgu tehakse listi JSONis olevatest elementidest koos checkboxiga, mille abil vastavat rida valida saab
4) Filtreeritud ridadest ja seal olevatest väärtustest saab luua uue JSONi kus kuvatakse antud elementide väärtused listina
   4.1) Nt Kui JSONis on element "kordusteArv" (ja seda võib esineda ka mitmel korral), siis uude JSONisse kogutakse antud väärtused kõik ühe
   elemendi alla

Näide:
1) See on fail mis lisatakse läbi UI programmi (esialgu võib mockida suvalise JSONi). Peab arvestama, et JSONis võib olla palju erinevaid elemente ja alamelemente
{
  "element": {
     "mingiMuutuja": "Tekst",
     "kordusteArv": 1
  },
  "element": {
     "mingiMuutuja": "Tekst Siin ka",
     "kordusteArv": 17
  },
  "element": {
     "mingiMuutuja": "Tekst Siin ka",
     "kordusteArv": 094
  }
}

2) 3) Välja kuvatakse: (saab valida ühe või mitu)
- element 
- element.mingiMuutuja
- element.kordusteArv

Valin nt element.kordusteArv

4) Valin genereeri uus JSON

Uue JSONi sisu:

{
  "element.kordusteArv": [1, 17, 094]
}



NB! Kui selle ülesandega jääb meil väheseks, siis võtame kasutusele kas nt XML failitüübi konverteerimise või hakkame looma lisafunktsionaalsuseid
