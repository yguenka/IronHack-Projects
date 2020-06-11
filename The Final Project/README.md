![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# 👩‍🔬 The Final Project | Skin Cancer Scanner

<p align="center">
  <img src="https://media3.giphy.com/media/3orifftBj3OpF6gY8w/giphy.gif?cid=ecf05e47927c999023469afe7d9ee0588d05fd500b89447a&rid=giphy.gif">
</p>

<p align="justify">Projeto realizado a partir do dataset [Câncer de Pele](https://www.kaggle.com/fanconic/skin-cancer-malignant-vs-benign) com o objetivo de fazer um aplicativo que retorne se o  tumor é benigno ou maligno.

Como a segmentação do dataset foi realizado no projeto 6, foi feito o tratamento de 100 imagens com tumores málígos e 100 imagens de turmores benígnos, utilizando o ***PCA*** para diminuir a quantidade de colunas (= diminuir a dimensão das imagens) em 80%. Neste caso, as dimensões foram de 224 x 224 para 12 x 12. 
Após o tratamento das imagens. foi realizado a modelagem dos dados utilizando a ***Regressão Logística*** para que seja possível a diferenciação entre os dois tipos de tumores na pele.

Para desenvolver o app, foi necessário fazer o pipeline da transformação do ***PCA*** e o modelo da ***Regressão Logística*** transformar em `pipe.pkl`. Após a transformação foi feito o deploy utilizando o ***Streamlit*** no ***Heroku***.

A apresentação está disponível em: [Skin Cancer Scanner - Apresentação](https://docs.google.com/presentation/d/1TjSlaU27YxH-52qqAKaaZk35n2RQsFTMblQZIyWv3Wg/edit?usp=sharing).

Já o app está disponível em: [Skin Cancer Scanner - App](https://skin-cancer-scanner.herokuapp.com/)</p>

## Como funciona o app ?

<p align="center">
  <img src="https://github.com/yguenka/IronHack-Projects/blob/master/The%20Final%20Project/video.gif?raw=true">
</p>

## Status do Projeto
Concluido ✅ - Para a apresentação do dia 22/05/2020

Em andamento 👣 - Para a finalização satisfatória

## Pré-requisito
1. [Python](https://www.python.org/)
2. [Jupyter Notebook](https://jupyter.org/try)
3. [Numpy](https://pypi.org/project/numpy/)
4. [Pandas](https://pandas.pydata.org/)
5. [Matplotlib](https://pypi.org/project/matplotlib/)
6. [Scikit Lean](https://pypi.org/project/scikit-learn/)
7. [Seaborn](https://pypi.org/project/seaborn/)
8. [Skimage](https://pypi.org/project/skimage/)
9. [Yellowbrick](https://pypi.org/project/yellowbrick/)
10. [Plotly](https://pypi.org/project/plotly/)
11. [LightGBM](https://pypi.org/project/lightgbm/)
12. [Streamlit](https://www.streamlit.io/)

## Autores
+ **Yukari Guenka Yshida**

## Agradecimentos
+ [André Aguiar](https://github.com/aguiarandre)
+ [Matheus Lavado](https://github.com/matheuslavado)
+ [Lucas White Rossi](https://github.com/LucasWhiteRossi)
+ [Raiana Rocha](https://github.com/Rairocha)