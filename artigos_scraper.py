from urllib.request import urlopen, HTTPError, urlretrieve
from urllib.error import URLError
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import time
import wget

timestr = time.strftime("%Y%m%d")
listaFinal = []

def rasparArtigo(itemFinal, pasta, nomeRevista, linkIssues): #função para baixar PDF e dados do artigo
    item = itemFinal.find_all('td')
    timestr = time.strftime("%Y-%m-%d")
    for issue in item:
        try:
            linkissue = issue.find('a')['href']
            print('Acessando a edição: ' + linkissue +'\n')
            req = urlopen(linkissue)
            bs = BeautifulSoup(req.read(), 'lxml')
            try:
                em = bs.find('em').parent.parent
                em = em.text
                start = em.find('versão impressa ISSN ') + len('versão impressa ISSN ')
                end = em.find('On-line')
                ISSN1 = em[start:end - 7]
                ISSN2 = em[end + len('On-line ISSN '):]
            except:
                ISSN1 = ''
                ISSN2 = ''
            tabelaGeral = bs.find(class_='content')
            pdfArtigos = tabelaGeral.find_all('a',href=re.compile(r'/pdf/[a-z]*/'))
            for artigo in pdfArtigos:
                link = artigo['href']
                idArtigo = link.replace('/pdf/', '')
                linkFinal = 'http://www.scielo.br' + link
                fullName = idArtigo.replace('/','_')
                path = os.path.join(pasta, fullName)
                listaInterna = [nomeRevista, ISSN1, ISSN2, linkIssues, fullName]
                listaFinal.append(listaInterna)
                df = pd.DataFrame(listaFinal, columns=['Nome da Revista', 'ISSN - impresso', 'ISSN - digital', 'Link', 'ID do artigo'])
                df.to_csv(f'{pasta}/infos_{timestr}.csv')
                try:
                    #urlretrieve(linkFinal, path)
                    wget.download(linkFinal, path)
                except Exception as e:
                    print (f'Erro ao baixar: {e}\n')
                    print(f'PDF: {fullName}')
                    pass
        except:
            pass

def dadosArtigo(itemFinal, pasta, nomeRevista, linkIssues): # função para baixar apenas os dados do artigo
    item = itemFinal.find_all('td')  
    timestr = time.strftime("%Y-%m-%d")  
    for issue in item:
        try:
            linkissue = issue.find('a')['href']
            print('Acessando a edição: ' + linkissue+'\n')
            req = urlopen(linkissue)
            bs = BeautifulSoup(req.read(), 'lxml')
            try:
                em = bs.find('em').parent.parent
                em = em.text
                start = em.find('versão impressa ISSN ') + len('versão impressa ISSN ')
                end = em.find('On-line')
                ISSN1 = em[start:end - 7]
                ISSN2 = em[end + len('On-line ISSN '):]
            except:
                ISSN1 = ''
                ISSN2 = ''
            tabelaGeral = bs.find(class_='content')
            pdfArtigos = tabelaGeral.find_all('a',href=re.compile(r'/pdf/[a-z]*/'))
            for artigo in pdfArtigos:
                link = artigo['href']
                idArtigo = link.replace('/pdf/', '')
                fullName = idArtigo.replace('/','_')
                listaInterna = [nomeRevista, ISSN1, ISSN2, linkIssues, fullName]
                listaFinal.append(listaInterna)
                df = pd.DataFrame(listaFinal, columns=['Nome da Revista', 'ISSN - impresso', 'ISSN - digital', 'Link', 'ID do artigo'])
                df.to_csv(f'{pasta}/infos_{timestr}.csv')
        except:
            pass
