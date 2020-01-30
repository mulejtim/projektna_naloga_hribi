import json
import re
import csv
import orodja
import requests


gorovja = ["gorisko_notranjsko_in_sneznisko_hribovje.html", "juliske_alpe.html"]
stevec = 0

with open("gorisko_notranjsko_in_sneznisko_hribovje.html", encoding="utf-8") as f:
    vsebina = f.read()
    print(stevec)
    # vsebina.encoding = "UTF-8"

with open("juliske_alpe.html", encoding="utf-8") as f:
    vsebina1 = f.read()
    print(stevec)

with open("kamnisko_savinjske_alpe.html", encoding="utf-8") as f:
    vsebina2 = f.read()
    print(stevec)

with open("karavanke.html", encoding="utf-8") as f:
    vsebina3 = f.read()
    print(stevec)

with open("pohorje_in_ostala_severovzhodna_slovenija.html", encoding="utf-8") as f:
    vsebina4 = f.read()
    print(stevec)

with open("polhograjsko_hribovje_in_ljubljana.html", encoding="utf-8") as f:
    vsebina5 = f.read()
    print(stevec)

with open("skofjelosko_cerkljansko_hribovje_in_jelovica.html", encoding="utf-8") as f:
    vsebina6 = f.read()
    print(stevec)

with open("zasavsko_-_posavsko_hribovje_in_dolenjska.html", encoding="utf-8") as f:
    vsebina7 = f.read()
    print(stevec)


    vzorec2 = (r'rel="noreferrer noopener">(?P<naslov>.+?)</a>"&gt;</span>&amp;nbsp;(?P<ime>[^&<].+?)<span class="html-tag">'
    r'.*</a>"&gt;</span>(?P<visina>.*?)<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/td&gt;'
    r'.*<span class="html-attribute-value">(?P<obrat>.*?)</span>" <span class="html-attribute-name">bgcolor</span>="')

    
vzorec4 = (r'<td class="naslov1"><b>&nbsp;&nbsp;<h1>(?P<ime>.*?)</h1></b></td>(.|\n)*'
    r'<tr><td><b>Gorovje:</b> <a class="moder" href=.*?>(?P<gorovje>.*?)</a></td></tr>(.|\n)*'
    r'<tr><td><b>Višina:</b>(?P<visina>.*?)&nbsp;m</td></tr>(.|\n)*'
    r'Širina/Dolžina:</b>&nbsp;<span id="kf0">(.|\n)*'
    r'<a class="moder" href="/zemljevid.asp\?goraid=\d+">(?P<geografska_sirina>.*?)&nbsp;/&nbsp;(?P<geografska_dolzina>.*?)</a>(.|\n)*'
    r'<tr><td><b>Vrsta:</b>(?P<vrsta>.*?)</td></tr>(.|\n)*'
    r'<tr><td><b>Ogledov:</b>(?P<st_ogledov>.*?)</td></tr>(.|\n)*'
    r'Priljubljenost:</b>(?P<priljubljenost>.*?)\((?P<mesto>.*?)\)</td></tr>(.|\n)*'
    r'<tr><td><b>Število poti:</b> <a class="moder" href="#poti">(?P<st_poti>.*?)</a></td></tr>(.|\n)*'
    r'<tr><td><b>Število GPS sledi:</b> <a class="moder" href="/gps.asp">(?P<st_gsp_sledi>.*?)</a></td></tr>(.|\n)*'
    r'<tr><td colspan="2"><p align="justify">(?P<opis>.*?)</p></td></tr>'
)

niz = [vsebina, vsebina1, vsebina2, vsebina3, vsebina4, vsebina5, vsebina6, vsebina7]
gore2 = []

for x in niz:
    for zadetek in re.finditer(vzorec2, x):
        url = "http://hribi.net{naslov}".format(naslov=str(zadetek.groups()[0]))
        print(f"Gledam na URL: {url}")
        r = requests.get(url)
        vseb = r.text
        for zad in re.finditer(vzorec4, vseb):
            stevec += 1
            gore2.append(zad.groupdict())
        
            

print(stevec)
print(gore2)

orodja.zapisi_csv(gore2, ['ime', 'gorovje', 'visina', 'geografska_sirina', 'geografska_dolzina', 'vrsta', 'st_ogledov', 'priljubljenost', 'mesto', 'st_poti', 'st_gsp_sledi', 'opis'], 'gore2.csv')