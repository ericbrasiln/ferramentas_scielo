from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
from revistas_xml import *
from revistas_pdf import* 
import time

saveMode = ''

def main():
    global saveMode
    while (saveMode != 1 and saveMode != 2):
        print('Script para raspagem de dados e arquivos das revistas da plataforma Scielo.br.\nVocê deve definir a revista a ser baixada, através do ISSN, e definir se pretende realizar o download de todos os  arquivos PDF dos artigos ou os arquivos XML.\nPara maiores informações ver https://github.com/ericbrasiln/SCIELO_CRAWLER/blob/master/README.md \nDesenvolvido por Eric Brasil, Leonardo Nascimento e Gabriel Andrade.\n')
        issn = input('-=- Definição da revista a ser baixada -=-\nDigite o ISSN da revista que pretende baixar (XXXX-XXXX): ')
        saveMode = int(input("-=- Definição do tipo de raspagem -=-\n1- Salvar os PDFs e gerar CSV;\n2- Salvar os XMLs.\nTipo de Raspagem (1 ou 2): "))
        revista = f'https://www.scielo.br/scielo.php?script=sci_issues&pid={issn}&lng=pt&nrm=iso'
        req = urlopen(revista)
        bs = BeautifulSoup(req.read(), "lxml")
        nomeRevista = bs.center.find('font', {'class':'nomodel'}).text
        pasta = re.sub(r"\s+", "", nomeRevista)
        if saveMode == 1:
            pastaScielo = os.path.join('scielo/pdf',pasta)
            print(nomeRevista)
            if not os.path.exists(pastaScielo):
                os.makedirs(f'{pastaScielo}')
                tabelaContent = bs.find('div', {'class': 'content'})
                tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                issues = tableIssues.find('tbody')
                issuesItens = issues.find_all('tr')
                for itemFinal in issuesItens:
                    rasparArtigo(itemFinal, pastaScielo, nomeRevista, revista)
            else:
                print('-=- Pasta exixtente. -=-\n')
                tabelaContent = bs.find('div', {'class': 'content'})
                tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                issues = tableIssues.find('tbody')
                issuesItens = issues.find_all('tr')
                for itemFinal in issuesItens:
                    dadosArtigo(itemFinal, pastaScielo, nomeRevista, revista)
        else:
            pastaScielo = os.path.join('scielo/xml',pasta)
            print(nomeRevista)
            if not os.path.exists(pastaScielo):
                os.makedirs(f'{pastaScielo}') # Cria pasta com nome da revista
                tabelaContent = bs.find('div', {'class': 'content'})
                tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                issues = tableIssues.find('tbody')
                issuesItens = issues.find_all('tr')
                for itemFinal in issuesItens:
                    rasparXML(itemFinal,pastaScielo) # Função para raspar os arquivos XML
            else:
                print('-=- Pasta já existe -=-')

if __name__ == "__main__":
    main()
