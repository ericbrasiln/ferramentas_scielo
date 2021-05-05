from urllib.request import urlopen
from bs4 import BeautifulSoup
from revistas_xml import *
from revistas_pdf import* 
import time

saveMode = ''

def main():
    global saveMode
    while (saveMode != 1 and saveMode != 2):
        print('Script para raspagem de dados e arquivos das revistas da plataforma Scielo.br.\nVocê deve definir a(s) revista(s) a ser(em) baixada(s), através do ISSN, e definir se pretende realizar o download de todos os  arquivos PDF dos artigos ou os arquivos XML.\nPara maiores informações ver https://github.com/ericbrasiln/SCIELO_CRAWLER/blob/master/README.md \nDesenvolvido por Eric Brasil, Leonardo Nascimento e Gabriel Andrade.\n')
        # Definição dos issn das revistas para raspagem
        issnList = list()
        while True:
            issnList.append(str(input('-=- Definição da(s) revista(s) -=-\nDigite o primeiro ISSN que deseja raspar (no formaro XXXX-XXXX): ')))
            resp = str(input('Deseja inserir outro ISSN para raspagem? [S/N] '))
            if resp in 'Nn':
                print('-=-'*50)
                break
        #Definição do tipo de raspagem: se todos os pdfs com um CSV simples para cada revista ou todos os xml
        saveMode = int(input("-=- Definição do tipo de raspagem -=-\n1- Salvar os PDFs e gerar CSV;\n2- Salvar os XMLs.\nTipo de Raspagem (1 ou 2): "))
        for issn in issnList:
            # Acessa o url e cria o objeto com BeautifulSoup
            revista = f'https://www.scielo.br/scielo.php?script=sci_issues&pid={issn}&lng=pt&nrm=iso'
            req = urlopen(revista)
            bs = BeautifulSoup(req.read(), "lxml")
            nomeRevista = bs.center.find('font', {'class':'nomodel'}).text
            alterar = re.sub(r"[(:\(\)<>?/\\|@+)]", "", nomeRevista)
            pasta = re.sub(r"\s+", "_", alterar)
            if saveMode == 1:
                pastaScielo = os.path.join('scielo/pdf',pasta)
                print(nomeRevista)
                if not os.path.exists(pastaScielo):
                    # Cria pasta com nome da revista
                    os.makedirs(f'{pastaScielo}')
                    tabelaContent = bs.find('div', {'class': 'content'})
                    tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                    issues = tableIssues.find('tbody')
                    issuesItens = issues.find_all('tr')
                    for itemFinal in issuesItens:
                        # Função para raspar os arquivos PDF
                        rasparArtigo(itemFinal, pastaScielo, nomeRevista, revista)
                else:
                    print('-=- Pasta exixtente. -=-\n')
                    tabelaContent = bs.find('div', {'class': 'content'})
                    tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                    issues = tableIssues.find('tbody')
                    issuesItens = issues.find_all('tr')
                    for itemFinal in issuesItens:
                        # Função para raspar os dados dos artigos
                        dadosArtigo(itemFinal, pastaScielo, nomeRevista, revista)
            else:
                pastaScielo = os.path.join('scielo/xml',pasta)
                print(nomeRevista)
                if not os.path.exists(pastaScielo):
                    # Cria pasta com nome da revista
                    os.makedirs(f'{pastaScielo}')
                    tabelaContent = bs.find('div', {'class': 'content'})
                    tableIssues = tabelaContent.find('table', {'bordercolor':'#c0c0c0'})
                    issues = tableIssues.find('tbody')
                    issuesItens = issues.find_all('tr')
                    for itemFinal in issuesItens:
                        # Função para raspar os arquivos XML
                        rasparXML(itemFinal,pastaScielo)
                else:
                    print('-=- Pasta já existe -=-')

if __name__ == "__main__":
    main()
