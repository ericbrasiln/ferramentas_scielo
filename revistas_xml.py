from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
from xml_scraper import*
import re
import os

def dadosRevistaXml(revista): #função para acessar os dados de cada revista
    nomeRevista = revista.findNext('a').text
    pasta = re.sub(r"\s+", "", nomeRevista)
    pastaScielo = os.path.join('scielo/xml',pasta)
    print(nomeRevista)
    if not os.path.exists(pastaScielo):
        os.makedirs(f'{pastaScielo}') # Cria pasta com nome da revista
        link = revista.findNext('a')['href']
        linkIssues = link.replace('serial', 'issues')
        req1 = urlopen(linkIssues)
        bs = BeautifulSoup(req1.read(), "lxml")
        tabelaContent = bs.find('div', {'class': 'content'})
        tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
        issues = tableIssues.find('tbody')
        issuesItens = issues.find_all('tr')
        for itemFinal in issuesItens:
            rasparXML(itemFinal,pastaScielo) # Função para raspar os arquivos XML
    else:
        print(nomeRevista)
        print('-=- Pasta existente. Passando para próxima revista. -=-')
