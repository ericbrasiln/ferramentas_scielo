# ferramentas_scielo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

>Esse repositório é parte dos projetos desenvolvidos pelos membros do [LABHDUFBA](http://labhd.ufba.br/) e tem como objetivo oferecer ferramentas de raspagem, organização e análise de artigos ciêntíficos publicados na plataforma [Scielo.br](https://www.scielo.br/scielo.php?script=sci_home&lng=pt&nrm=iso).

## Instalação

Para executar os Scripts desse repositório, você precisa clonar ou fazer download para sua máquina. Antes de executar os scripts, é preciso preparar seu computador, como mostramos abaixo.

### Python

A ferramentas desse projeto foram escritas em [Python 3.8](https://www.python.org/). Esta é uma linguagem de programação que te permite trabalhar rapidamente e integrar diferentes sistemas com maior eficiência.
Para executar o arquivo .py é preciso instalar o Python3 em seu computador.

[Clique aqui](https://python.org.br/instalacao-windows/) para um tutorial de instalação do Python no Windows, [clique aqui](https://python.org.br/instalacao-linux/) para Linux e [clique aqui](https://python.org.br/instalacao-mac/)
para Mac.

Após a instalação, vc pode executar o arquivo .py direto do prompt de comando do Windows ou pelo terminal do Linux, ou utilizar as diversas [IDE](https://pt.wikipedia.org/wiki/Ambiente_de_desenvolvimento_integrado) disponíveis.

Exemplo de como executar utilizando o terminal do Linux, após instalar o Python3.8:

1. Acesse o diretório em que o arquivo .py está salvo:
   ```sh
   $ cd user/local
   ```
1. Instale as bibliotecas requeridas:
   ```sh
   $ pip3 install -r requirements.txt
   ```
1. Execute o arquivo usando Python3.8
   ```sh
   $ python3.8 run_scielo_scraper.py
   ```
## run_scielo_scraper.py

Esse script permite aos usuário selecionar qual assunto ele pretende raspar de acordo com a categorização estabelecida pela plataforma [Scielo.br](https://www.scielo.br/scielo.php?script=sci_subject&lng=pt&nrm=iso). É possível escolher entre oito assunto:

* Ciências Agrárias
* Ciências Biológicas
* Ciências da Saúde
* Ciêncas Exatas e da Terra 
* Ciências Humanas
* Ciências Sociais Aplicadas
* Engenharias
* Linguística, Letras e Artes

Após a definição do assunto, é preciso definir o tipo de raspagem: 

1. Realizar o download de todos os arquivos PDF de cada revista do assunto selecionado. É criado um CSV com informações básicas sobre a raspagem (nome da revista, ISSN, nome do arquivo e link para o PDF)

    :warning: Devido ao volume de dados, contando dezenas de milhares de artigos, o download de todos os arquivos PDF demandará  muito tempo e uso intenso de sua máquina.

2. Realizar o download dos arquivos XML de cada revista do assunto selecionado.
    
    :warning: Os arquivos XML possuem todos os metadados dos artigos, incluíndo as referências bibliográficas) e usando a ferramenta `XML_to_CSV` será possível convertar todos os XML para uma planilha.

## run_scielo_ISSN.py

Nesse script é possível raspar uma revista específica através do ISSN.

Possui as mesmas características do `run_scielo_scraper.py`, porém a definição da revista a ser raspada é feita do ISSN, uma revista de cada vez.

## :warning: Atenção

Ambos os scripts criarão diretórios para armazenar os arquivos e dados.

- `scielo/pdf/nomeDaRevista` no caso da raspagem de PDFs;
- `scielo/xml/nomeDaRevista` no caso da raspagem de XMls.

Entretanto, se a pasta com o nome de uma revista já exixtir, o algoritmo entenderá que a raspagem dela já foi efetuada e **passará para a seguinte**.

## Licença MIT
2020 [Eric Brasil](https://github.com/ericbrasiln), [Gabriel Andrade](https://github.com/gabrielsandrade), [Leonardo Nascimento](https://github.com/leofn)
