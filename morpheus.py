import urllib.parse
import urllib.request
import json

def morpheus(fr, to, ur):
    url = 'http://subjectrefresh.info/morpheus/api/convert'
    values = {'from' : fr,
              'to' : to,
              'url' : ur }

    data = urllib.parse.urlencode(values)
    print(data)
    full_url = url + '?' + data
    print(full_url)
    
    content = urllib.request.urlopen(full_url)
    output = content.read().decode('utf-8')
    ser = json.loads(output)
    for item in ser:
        if ser[item] != ("url" or "from" or "to"):
            return ser[item]
        

f = open('workfile', 'w')
f.write(morpheus("pdf", "html", "http://www.indire.it/wp-content/uploads/2015/08/pdf-sample.pdf"))
f.close()
















