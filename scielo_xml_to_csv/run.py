from bs4 import BeautifulSoup
import os
import pandas as pd
import re
from xml.etree import ElementTree as ET
from pdflink_xml import *
from infos_xml import *
from csv_final import *
from refs import *

# Definir o caminho para o diretório com as pastas da revistas
print('Scripts para converter Dataset de XML  das revistas do Scielo.br (previamente baixado) para CSV.\nPara maiores informações ver https://github.com/LABHDUFBA/ferramentas_scielo/ \nDesenvolvido por Eric Brasil, Leonardo Nascimento e Gabriel Andrade.\n')
print('-='*50)
print('\nLembrando que o diretório do dataset precisa conter pastas das revistas do Scielo, cada pasta contento os artigos em arquivo XML.')
print('-='*50)
datasetXML = str(input('\nInsira o caminho do diretório onde se encontra o dataset: '))
# Criar diretório para salvar os arquivos CSV
datasetCSV = os.path.join('scielo', 'xml', 'CSVs2')
if not os.path.exists(datasetCSV): # Se não existir, será criada.
    os.makedirs(datasetCSV)
# Abrir o diretório e iterar em cada revista
with os.scandir(datasetXML) as pastas:
    for pasta in pastas:
        # Listas de cada parâmetro a ser arquivado 
        file_name = []
        article_id = []
        authors = []
        authors_aff = []
        article_title = []
        journal_title = []
        journal_issn = []
        journal_publisher = []
        pub_date = []
        abstract = []
        key_words = []
        volume = []
        num = [] 
        fpage = [] 
        lpage = []
        doi = []
        linkPDF = []
        refs = []
        # Encontrar e definir o nome da revista
        xml_dir = pasta
        revista = str(pasta)
        revista = revista.replace('<DirEntry \'', '')
        revista = revista.replace('\'>','')
        # Definir o nome do csv
        csv_file = os.path.join(datasetCSV, f"metadata_{revista}.csv" )
        print(f'\nRevista: {revista}\n')
        # Se o CSV ainda não existir, acessar o diretório da revista.
        if not os.path.exists(csv_file):
            #Iteração em cada arquivo XML de cada diretório de revista
            with os.scandir(xml_dir) as entries:
                for entry in entries:
                    # Função para buscar e armazenar o link do PDF do item.
                    find_pdf_link(entry, linkPDF)
                    # Função para buscar as referências do artigo
                    referenciasXml(entry, refs)
                    # Abrir e analisar cada XML
                    with open(entry, "r", encoding="ISO-8859-1") as file: 
                        soup = BeautifulSoup(file, "html.parser")
                        file_name.append(entry.name)
                        # Executa as funções de coleta das informações e insere
                        # nas listas respectivas
                        article_id.append(find_article_id(soup))
                        authors.append(find_authors(soup))
                        authors_aff.append(find_authors_aff(soup))
                        article_title.append(find_article_title(soup))
                        journal_title.append(find_journal_title(soup))
                        journal_issn.append(find_journal_issn(soup))
                        journal_publisher.append(find_journal_publisher(soup))
                        pub_date.append(find_pub_date(soup))
                        abstract.append(find_abstract(soup))
                        key_words.append(find_key_words(soup))
                        volume.append(find_volume(soup))
                        num.append(find_num(soup))
                        fpage.append(find_fpage(soup))
                        lpage.append(find_lpage(soup))
                        doi.append(find_doi(soup))
            # Dicionário com os itens que serão armazenados no dataframe
            data = {"file_name": file_name, "article_id": article_id, "authors":authors, "authors affiliation": authors_aff,"article_title":article_title, "journal_title": journal_title, "journal_issn": journal_issn, "journal_publisher":journal_publisher,"pub_date": pub_date, "abstract": abstract,"key_words":key_words, "volume":volume, "num":num, "fpage":fpage, "lpage":lpage, "doi": doi, 'refs': refs, "link pdf":linkPDF}
            # Criação do dataframe
            df = pd.DataFrame.from_dict(data, orient='index')
            df = df.transpose()
            # Salvar o CSV
            csv_file = os.path.join(datasetCSV, f"metadata_{revista}.csv" ) #definir nome do csv
            df.to_csv(csv_file)
        # Se o CSV já exitir na pasta, o programa retorna mensagem e passa para o
        # próximo diretório
        else:
            print(f'CSV da revista {revista} já existe.\n')
            pass
# Executa função para unir todos os arquivos CSV em um único dataframe e salvar em CSV.
df_final(datasetCSV)
print('Script concluído.')
