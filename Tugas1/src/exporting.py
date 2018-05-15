from extraction import titles,prices,sellers,ranks
import json 
import io

try:
    to_unicode = unicode #konfigurasi awal
except NameError:
    to_unicode = str

#untuk keperluan pembuatan file json
data = {'Judul': titles, 
        'Harga': prices,
        'Pelapak': sellers,
        'Rank': ranks}

#membuat file json
with io.open('data.json', 'w', encoding='utf8') as outfile: 
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

