import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print(titulo.text)

# Subtítulo
'''subtitulo = noticia.find('div', attrs={'class': 'bstn-relatedtext'})

print(subtitulo.text)'''