import urllib # urllib é um pacote que coleciona vários módulos para trabalhar com URLs
import urllib.request # urllib.request para abrir e ler URLs, parse para analisar URLs.

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print('o site não está assisevel no momento')
else:
    print('está tudo ok ')
    print(site.read()) # esse read vai mostrar todo o código do site
#esta biblioteca é muito útil