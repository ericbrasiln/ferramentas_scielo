from urllib.request import urlopen
from bs4 import BeautifulSoup
from revistas_xml import *
from revistas_pdf import* 
import time

timestr = time.strftime("%Y%m%d")
saveMode = ''
def main():
    global saveMode
    while (saveMode != 1 and saveMode != 2):
        # Definição da área do conhecimento para raspagem
        print('Script para raspagem de dados e arquivos das revistas da plataforma Scielo.br.\nVocê deve definir a área de conhecimento e definir se pretende realizar o download de todos os  arquivos PDF dos artigos ou os arquivos XML.\nDevido ao volume de dados, contando dezenas de milhares de artigos, o download de todos os arquivos PDF demandará  muito tempo e uso intenso de sua máquina.\n')
        subject = int(input('-=- Definição da área do conhecimento -=-\n1- Ciências Agrárias\n2- Ciências Biológicas\n3- Ciências da Saúde\n4- Ciêncas Exatas e da Terra\n5- Ciências Humanas\n6- Ciências Sociais Aplicadas\n7- Engenharias\n8- Linguística, Letras e Artes\nDigite o número correspondente à área de conhecimento que será raspada: '))
        #Definição do tipo de raspagem: se todos os pdfs com um CSV simples para cada revista ou todos os xml
        saveMode = int(input("-=- Definição do tipo de raspagem -=-\n1- Salvar os PDFs e gerar CSV;\n2- Salvar os XMLs.\nTipo de Raspagem (1 ou 2): "))
        urlRevistas = 'https://www.scielo.br/scielo.php?script=sci_subject&lng=pt&nrm=iso'
        print('\n-=- Acessando base do Scielo -=-\n')
        # Acessa o url e cria o objeto com BeautifulSoup
        req = urlopen(urlRevistas)
        bs = BeautifulSoup(req.read(), "lxml")
        ch = bs.find('a', {'name': f'subj{subject}'})
        revCorrentes = ch.find_next('p')
        listaRevCorrentes = revCorrentes.find_next('p')
        # Criando lista com as revistas correntes da área de conhecimento
        revistas = listaRevCorrentes.find_all('font', {'class': 'linkado'})
        print('-=- Criando lista de Revistas -=-\n')
        for revista in revistas:        
            if saveMode == 1:
                # Se a opção foi raspar os PDFs, passa para a função dadosRevista
                dadosRevista(revista)
            else:
                # Se a opção foi raspar os XMLs, passa para a função dadosRevistaXml
                dadosRevistaXml(revista)

if __name__ == "__main__":
    main()