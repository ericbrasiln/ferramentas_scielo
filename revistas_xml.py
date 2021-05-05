from urllib.request import urlopen
from bs4 import BeautifulSoup
from xml_scraper import*
import re
import os

def dadosRevistaXml(revista):
    '''
    função para acessar os dados de cada revista, definir as variáveis e passar para a função de
    raspagem dos Xml
    '''
    # Definição do título da revista
    nomeRevista = revista.findNext('a').text
    alterar = re.sub(r"[(:\(\)<>?/\\|@+)]", "", nomeRevista)
    pasta = re.sub(r"\s+", "_", alterar)
    # Definição do caminho para criar a pasta para os PDFs
    pastaScielo = os.path.join('scielo/xml',pasta)
    print(nomeRevista)
    if not os.path.exists(pastaScielo):
        # Se a pasta ainda não existir, cria a pasta
        os.makedirs(f'{pastaScielo}') 
        link = revista.findNext('a')['href']
        linkIssues = link.replace('serial', 'issues')
        req1 = urlopen(linkIssues)
        bs = BeautifulSoup(req1.read(), "lxml")
        tabelaContent = bs.find('div', {'class': 'content'})
        tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
        issues = tableIssues.find('tbody')
        issuesItens = issues.find_all('tr')
        for itemFinal in issuesItens:
            # Função para raspar os arquivos XML
            rasparXML(itemFinal,pastaScielo) 
    else:
        print(nomeRevista)
        print('-=- Pasta existente. Passando para próxima revista. -=-')
