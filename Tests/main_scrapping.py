"""
La idea de este archivo es probar la libreria scrapy para descartar la innformacion sobre el paro de la web del SEPE
de nanera automatizada.
La idea es descargar los archivos .xlsx de la web que luego parseare.   (NO ACENTOS PARA QUE NO SE QUEJE, NO SOY TONTITO).
"""

#import scrapy

# Obtaining and saving the data
import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin


MAIN_URL = 'https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/datos-avance/datos.html'

DATA_ROOT = 'downloaded_files'

req = requests.get(MAIN_URL)
soup = BeautifulSoup(req.text, "html.parser")

if __name__ == "__main__":

    document_links = []

    for link in soup.select('a'):     #soup.select('a[href^="http://"]'):
        href = link.get('href')

        if (href.endswith('.xls')) | (href.endswith('.xlsx')) | (href.endswith('.csv')):
            document_links.append(href)

    # DOWNLOADING
    counter = 0
    for link in document_links:
        complete_link = 'https://www.sepe.es/' + link
        print('(' + str(counter) +  ') - ' + complete_link)
        filename = complete_link.split('/')[-1]
        filename = DATA_ROOT + '/' + filename
        urlretrieve(complete_link, filename)
        counter +=1



"""
REFERENCES:
===========

(1) https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211
(2) https://stackoverflow.com/questions/34632838/download-xls-files-from-a-webpage-using-python-and-beautifulsoup
(3) https://docs.scrapy.org/en/latest/intro/overview.html
(4) https://docs.scrapy.org/en/latest/
(5) https://docs.scrapy.org/en/latest/intro/examples.html
(6) https://github.com/scrapy/quotesbot
(7) https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main/32185
(8) https://www.atlassian.com/git/tutorials/saving-changes/gitignore#:~:text=If%20you%20want%20to%20ignore,directory%20as%20an%20ignored%20file.
"""



"""
BAD_CODE_BUCKET:
================

class Documents_Spider(scrapy.Spider):
    #TODO: expliar como funciona esta mierda
        
    name = 'SEPE_spider'
    start_urls = ['https://www.sepe.es/HomeSepe/que-es-el-sepe/estadisticas/datos-avance/datos.html']

    def parse(self, response):
        for element in respose.css('a'):
            print(element)

    def __str__(self):   
        message = 'Se trata de una clase heredada de Spider que recoge los documentos exvel de la url especificada.'


=================

lista_links = soup.a
print(len(lista_links))
print('====')
for element in lista_links:
    print(element)
    print('----')
print(lista_links)


u = urlopen(MAIN_URL)
    try:
        html = u.read().decode('utf-8')
    except:
        print('Error abriendo la url')
        pass
    finally:
        u.close()


soup = BeautifulSoup(html, 'html.parser')
# Select all A elements with href attributes containing URLs starting with http://
for link in soup.select('a[href^="http://"]'):
    href = link.get('href')

    # Make sure it has one of the correct extensions
    if not any(href.endswith(x) for x in ['.csv', '.xls', '.xlsx']):
        continue

    filename = href.rsplit('/', 1)[-1]
    print("Downloading %s to %s..." % (href, filename))
    urlretrieve(href, filename)
    print("Done.")

"""