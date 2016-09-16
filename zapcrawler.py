# coding: utf-8
import re

from selenium.webdriver import Chrome

URL = 'http://www.zapimoveis.com.br/aluguel/{type}/#{{"precomaximo":"2147483647","parametrosautosuggest":[{{"Bairro":"{neighbourhood}","Zona":"{zone}","Cidade":"RIO DE JANEIRO","Agrupamento":"","Estado":"RJ"}}],"pagina":"{page}","ordem":"Relevancia","paginaOrigem":"ResultadoBusca","semente":"1463671937","formato":"Lista"'


class ZapCrawlerManager(object):
    def __init__(self, url):
        self.url = url
        self.browser = Chrome()
        patterns = [r'R\$\s\d*.[0-9]*', r'[0-9]*m2', r'\d\squarto']
        self.compiled_patterns = [re.compile(pat) for pat in patterns]

    def visit(self):
        self.browser.get(self.url)

    def get_information(self):
        self.content = self.browser.find_elements_by_class_name('list-cell')

    def normalize_information(self):
        contents = self.get_information()

        return [[m.search(content.text).group()
                 for content in contents]
                for m in self.compiled_patterns]
