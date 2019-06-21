import urllib3
import pprint
from xml.dom.minidom import parseString
http = urllib3.PoolManager()

def get_google_new_results( term, count ):
    """
    This function queries and returns google search results in an easy to program format.
    :param term: Search term to query
    :param count: Max results to show
    :type term: string
    :type count: int
    :return: Two lists with the results, first one contains the headlines and second one the links to the articles.
    :rtype: (list, list)
    """
    headlines = []
    urls = []
    obj = parseString(http.request('GET','https://news.google.com/news?q=%s&output=rss' % term).data)

    elements = obj.getElementsByTagName('title')[2:] # To get rid of unwanted title elements in XML doc    
    links = obj.getElementsByTagName('link')[2:]

    for i in range(count if len(elements) > count else len(elements)):
      headlines.append(elements[i].childNodes[0].data)
      urls.append(links[i].childNodes[0].data.split('=')[-1])

    return headlines, urls

h, u = get_google_new_results( 'marketing+ai', 5 )

pp = pprint.PrettyPrinter(indent=0)
pp.pprint(h)
pp.pprint(u)
