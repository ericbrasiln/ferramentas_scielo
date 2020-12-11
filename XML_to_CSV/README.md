# scielo_xml_to_csv

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

**Scripts para converter Dataset de XML  das revistas de Ciências Humanas do _Scielo_ (previamente baixado) para CSV.**
  
Esses scripts tem como objetivos analisar, selecionar, organizar e salvar informações de um dataset de arquivos XML de todas as revistas categorizadas como [Ciências Humanas na base do Scielo](https://www.scielo.br/scielo.php?script=sci_subject&lng=pt&nrm=iso#subj5) e um arquivo .csv.

---

O `run.py` acessa o diretório contendo as pastas de cada revista e analisa cada XML, inserindo os dados em um arquivo CSV salvo com o nome `metadata_{revista}.csv`. 

:warning: _É preciso definir o caminho do diretório com o dataset. E a estrutura desse dataset deve conter diretórios de cada revista com seus arquivos XML a serem analisados._

---

As seguintes informações são inseridas no CSV:

- index,
- file_name,
- article_id,
- authors,
- authors affiliation,
- article_title,
- journal_title,
- journal_issn,
- journal_publisher,
- pub_date,
- abstract,
- key_words,
- volume,
- num,
- fpage,
- lpage,
- doi,
- link pdf

---

Em seguida, com a função `df_final()`, todos os arquivos CSV são unidos em um único dataframe com `Pandas` e salvos em um CSV chamados `metadata_scielo_{yyyy-mm-dd_HhMmSs}.csv`.

---

Elementos presentes nesse repositório foram retirados de [Scielo_Journal_Metadata_Downoader](https://github.com/johnsgomez/Scielo_Journal_Metadata_Downoader), criado por [johnsgomez](https://github.com/johnsgomez)

---
## Licença

MIT licence

2020 Eric Brasil, Leonardo Nascimento e Gabriel Andrade
