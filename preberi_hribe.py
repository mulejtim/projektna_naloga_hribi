import json
import re
import csv
import orodja


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


    vzorec = (r' <span class="html-tag">&lt;tr <span class="html-attribute-name">bgcolor</span>'
    r'="<span class="html-attribute-value">#.*?'
    r'</span>"&gt;</span><span class="html-tag">&lt;td&gt;</span>'
    r'<span class="html-tag">&lt;a <span class="html-attribute-name">href</span>'
    r'="<a class="html-attribute-value html-external-link" target="_blank"'
    r' href='
    r'".*?  rel="noreferrer noopener">'
    r'.*?</a>"&gt;</span>&amp;nbsp;(?P<ime>.*?)' # ime gore
    r'<span class="html-tag">&lt;/a&gt;</span><span'
    r'class="html-tag">&lt;/td&gt;</span><span'
    r'class="html-tag">&lt;td&gt;</span>&amp;nbsp;&amp;nbsp;<span'
    r'class="html-tag">&lt;/td&gt;</span><span'
    r'class="html-tag">&lt;td&gt;</span><span class="html-tag">&lt;a'
    r'<span class="html-attribute-name">href</span>'
    r'="<a class="html-attribute-value html-external-link" target="_blank" href='
    r'.*? rel="noreferrer noopener">.*?'
    r'</a>"&gt;</span>(?P<visina>.*?)' # visina
    r'<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/td&gt;'
    r'</span><span class="html-tag">&lt;td'
    r'<span class="html-attribute-name">width</span>="'
    r'<span class="html-attribute-value">30'
    r'</span>"&gt;</span>&amp;nbsp;<span class="html-tag">&lt;/td&gt;</span>'
    r'<span class="html-tag">&lt;td&gt;</span><span class="html-tag">&lt;p '
    r'<span class="html-attribute-name">align</span>="<span class="html-attribute-value">center'
    r'</span>"&gt;</span><span class="html-tag">&lt;table <span class="html-attribute-name">'
    r'width</span>="<span class="html-attribute-value">100%</span>" '
    r' <span class="html-attribute-name">cellpadding</span>'
    r'="<span class="html-attribute-value">0</span>" <span class="html-attribute-name">'
    r'cellspacing</span>="<span class="html-attribute-value">0</span>'
    r'"&gt;</span><span class="html-tag">&lt;tr <span class="html-attribute-name">'
    r'height</span>="<span class="html-attribute-value">5</span>'
    r'"&gt;</span><span class="html-tag">&lt;td <span class="html-attribute-name">bgcolor</span>="<span class="html-attribute-value">#4FC5A0'
    r'</span>" <span class="html-attribute-name">width</span>="<span '
    r'class="html-attribute-value">(?P<priljublenost>.*?)' #priljublenost
    r'</span>"&gt;</span><span class="html-tag">&lt;/td&gt;</span><span class="html-tag">&lt;td <span class="html-attribute-name">width</span>="'
    r'<span class="html-attribute-value">(?P<obrat>.*?)' # obrat
    r'</span>" <span class="html-attribute-name">bgcolor</span>="<span class="html-attribute-value">#cccccc</span>"&gt;</span><span class="html-tag">&lt;/td&gt;</span><span '
    r'class="html-tag">&lt;/tr&gt;</span><span class="html-tag">&lt;/table&gt;'
    r'</span><span class="html-tag">&lt;/td&gt;</span><span class="html-tag">&lt;/tr&gt;'
    r'</span>'
    )

    vzorec1 = (r'</span>&amp;nbsp;(?P<ime>[^&<].+?)<span class="html-tag">'
    r'.*</a>"&gt;</span>(?P<visina>.*?)<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/td&gt;'
    r'.*<span class="html-attribute-value">(?P<obrat>.*?)</span>" <span class="html-attribute-name">bgcolor</span>="')

niz = [vsebina, vsebina1, vsebina2, vsebina3, vsebina4, vsebina5, vsebina6, vsebina7]
gore = []

for x in niz:
    for zadetek in re.finditer(vzorec1, x):
        gore.append(zadetek.groupdict())

print(gore)

orodja.zapisi_csv(gore, ['ime', 'visina', 'obrat'], 'gore.csv')