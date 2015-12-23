import urllib.parse
import urllib.request
import json

def convert(fr, to, ur):
    """ this function returns the converted text """

    url = 'http://subjectrefresh.info/morpheus/api/convert'
    values = {'from' : fr,
              'to' : to,
              'url' : ur }

    data = urllib.parse.urlencode(values)
    full_url = url + '?' + data
    
    content = urllib.request.urlopen(full_url)
    output = content.read().decode('utf-8')
    
    ser = json.loads(output)
    return ser[to]

def output(into):
    print(into.encode(sys.stdout.encoding, errors='replace'))
