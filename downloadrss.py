# DownloadRss.py
#
# Downloads all of the attachments from an RSS, feed. Designed for podcasts but could work on any type of RSS feed
#
import sys
import xmltodict
import requests
import os

# Downloads a file from an RSS 
#
def GetDocumentList(url):
    #if os.path.isfile(filename):
    #    print(f"{filename} already exists, skipping...")

    print(f'Downloading {url}')

    filename = 'tempcache.db'
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.text.encode('utf-8'))

    with open(filename) as fd:
        xml = xmltodict.parse(fd.read())
    os.remove(filename)

    Documents = xml['rss']['channel']['item']

    print(f'{len(Documents)} documents found in the feed')

    return Documents

# Downloads an individual document
#
def DownloadDocument(Document):
    url = Document['enclosure']['@url']
    i = url.find('?')
    if i != -1:
        url = url[0:i]
    i = url.rfind('/')
    fname = url[i+1:]
    
    if os.path.isfile(fname):
        print(f'{fname} already exists, skipping...')
        return
    
    print(f'Downloading {url} into {fname}')
    r = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(r.content)

# Main code for the script
#
DocumentList = GetDocumentList(sys.argv[1])
for Document in DocumentList:
    DownloadDocument(Document)
