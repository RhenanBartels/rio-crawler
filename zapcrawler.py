# coding: utf-8
from selenium.webdriver import Chrome

URL = 'http://www.zapimoveis.com.br/aluguel/{type}/#{{"precomaximo":"2147483647","parametrosautosuggest":[{{"Bairro":"{neighbourhood}","Zona":"{zone}","Cidade":"RIO DE JANEIRO","Agrupamento":"","Estado":"RJ"}}],"pagina":"{page}","ordem":"Relevancia","paginaOrigem":"ResultadoBusca","semente":"1463671937","formato":"Lista"'


class ZapCrawlerManager(object):
    def __init__(self, url):
        self.url = url
        self.browser = Chrome()

    def visit(self):
        self.browser.get(self.url)
