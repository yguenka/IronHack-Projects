![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# 🔗 Project 3 | Web Scrapping and API

<p align="center">
  <img src="https://media2.giphy.com/media/ADgfsbHcS62Jy/giphy.gif?cid=ecf05e47fadefb496c2757a9fc27a41444378b95e914a0cb&rid=giphy.gif">
</p>

## Descrição

O Web Scrapping foi feito no site [Wordometers](https://www.worldometers.info/coronavirus/country/brazil/) para captar informações sobre a quantidade de novos casos do Corona Virus (COVID-19) durante os meses de fevereiro e março, de 41 dias.

Já o uso do API foi utilizado no site [AwesomeAPI](https://economia.awesomeapi.com.br/json/daily/USD-BRL/41) para captar informações sobre a variação do dolar nos meses de fevereiro e março , de 41 dias também.

## Status do Projeto
Concluido ✅

## Pré-requisito
1. [Python](https://www.python.org/)
2. [Jupyter Notebook](https://jupyter.org/try)
3. [Pandas](https://pandas.pydata.org/)
4. [Requests](https://pypi.org/project/requests/)
5. [BS4](https://pypi.org/project/bs4/)(BeautifulSoap)
6. [Regex](https://pypi.org/project/regex/)
7. [DateTime](https://pypi.org/project/DateTime/)



## Como foi feito ?
Com o uso do ***requests*** e ***BeautifulSoap*** , foi possível extrair as informações da página do site [Wordometers](https://www.worldometers.info/coronavirus/country/brazil/), para que seja possível aplicar o ***Regex***, possibilitando a extração de informações de novos casos de COVID-19 no Brasil, dos 41 dias. 

Para a extração de informações via API, foi utilizado o ***requests*** e para o data cleaning, o ***Regex***.

Após o data cleaning das informações extraídas, elas foram exportadas para o CSV.

## Autores
+ **Yukari Guenka Yshida**

## Agradecimentos
+ [André Aguiar](https://github.com/aguiarandre)
+ [Matheus Lavado](https://github.com/matheuslavado)
+ [Lucas White Rossi](https://github.com/LucasWhiteRossi)
+ [Raiana Rocha](https://github.com/Rairocha)