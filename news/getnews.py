import urllib3
from xml.dom.minidom import parseString
http = urllib3.PoolManager()

def get_google_new_results( term, count ):
    results = []
    obj = parseString(http.request('GET','https://news.google.com/news?q=%s&output=rss' % term).data)

    elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc    
    links = obj.getElementsByTagName('link')[2:]

    for i in range(count if len(elements) > count else len(elements)):
      headline = elements[i].childNodes[0].data
      url = links[i].childNodes[0].data.split('=')[-1]
      newssearch = headline + ' -> ' + url
      results.append( newssearch )
    return results


items = get_google_new_results( 'marketing+ai', 5 )
for i,e in enumerate(items):
    print('%d: %s' % (i+1,e,))