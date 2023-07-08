if not(os.path.isfile(fname)):
    print 'fetching'
    r = requests.get(url)
    f = open(fname, 'wb')
    f.write(r.text.encode('utf-8'))
    f.close()

with open(fname) as fd:
    xml = xmltodict.parse(fd.read())

episodes = xml['rss']['channel']['item']

print(len(episodes))

for episode in episodes:
    url = episode['enclosure']['@url']
    i = url.find('?')
    if i != -1:
        url = url[0:i]
    i = url.rfind('/')
    fname = destination_directory + '/' + url[i+1:]
    if not(os.path.isfile(fname)):
        r = requests.get(url)
        f = open(fname, 'wb')
        f.write(r.content)
        f.close()
