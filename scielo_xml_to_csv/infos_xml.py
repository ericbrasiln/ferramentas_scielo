from bs4 import BeautifulSoup
import os
import pandas as pd

#Funções para extrair informações do xml     
def find_article_id(soup):
    try: # Tenta encontrar no XML
        article_id = soup.front.find("article-id")
        return(article_id.string)
    except: # Se não encontrar, insere "None"
        article_id = 'None'
        return(article_id)
    
def find_article_title(soup):
    try:
        article_title = soup.front.find("article-title")
        return(article_title.string)
    except:
        article_title = 'None'
        return(article_title)
    
def find_authors(soup):
    try:
        authors_lastnames = soup.front.find_all(["surname"])
        authors_names = soup.front.find_all(["given-names"])
        authors = [] # Lista para armazenar nomes e sobrenomes dos/as autores/as
        for author in range(len(authors_lastnames)): # Iteração juntando nomes e sobrenomes
            authors.append(authors_names[author].string + " " + authors_lastnames[author].string)
        return(", ".join(authors)) # Separa diferentes autores por ','
    except:
        authors = 'None'
        return(authors)

def find_authors_aff(soup):
    try:
        authors_inst = soup.front.find_all(["institution"])
        authors_country = soup.front.find_all(["country"])
        authors_aff = [] # Lista para armazenar filiações institucionais dos/as autores/as
        for aff in range(len(authors_country)): # Iteração juntando instituição com país
            authors_aff.append(authors_inst[aff].string + " " + authors_country[aff].string)
        return(", ".join(authors_aff)) # Separa diferentes instituições por ','
    except:
        authors_aff = 'None'
        return(authors_aff)
  
def find_pub_date(soup):
    try:
        month = soup.front.find("pub-date").contents[3].string
        year = soup.front.find("pub-date").contents[5].string
        date = [year,month] # Cria lista com ano e mês da públicação
        return('-'.join(date)) # Separa ano e mês com "-"
    except:
        date = "None"
        return(date)
    
def find_volume(soup):
    try:
        volume = soup.front.find("volume")
        return(volume.string)
    except:
        volume = "None"
        return(volume)

def find_num(soup):
    try:
        num = soup.front.find("numero")
        return(num.string)
    except:
        num = "None"
        return(num)
           
def find_fpage(soup):
    try:
        fpage = soup.front.find("fpage")
        return(fpage.string)
    except:
        fpage = "None"
        return(fpage)

def find_lpage(soup):
    try:
        lpage = soup.front.find("lpage")
        return(lpage.string)
    except:
        lpage = "None"
        return(lpage)

def find_doi(soup):
    try:
        doi = soup.front.find_all("article-id")
        doi = doi[1]
        return(doi.string)
    except:
        doi = 'None'
        return(doi)

def find_journal_title(soup):
    try:
        journal_title = soup.front.find("journal-title")
        return(journal_title.string)
    except:
        journal_title = "None"
        return(journal_title)
    
def find_journal_issn(soup):
    try:
        journal_issn = soup.front.find("issn")
        return(journal_issn.string)
    except:
        journal_issn = "None"
        return(journal_issn)

def find_journal_publisher(soup):
    try:
        journal_publisher = soup.front.find("publisher-name")
        return(journal_publisher.string)
    except:
        journal_publisher = "None"
        return(journal_publisher)
    
def find_key_words(soup):
    try:
        key_words = soup.front.find_all("kwd") # Encontra o primeiro conjunto de 
        # palavras-chave (idioma principal)
        key_words = [kwd.string for kwd in key_words] # Criação de uma lista com as palavras-chave, atrvés de uma iteração, que tb as transforma em string
        return ", ".join(key_words) # Separa cada palavra-chave com ", "
    except:
        key_words = "None"
        return(key_words)
    
def find_abstract(soup):
    try:
        abstract_text = soup.front.find("abstract") # Encontra o primeiro resumo (idioma principal)
        return(abstract_text.string)
    except:
        abstract_text = "None"
        return(abstract_text)
