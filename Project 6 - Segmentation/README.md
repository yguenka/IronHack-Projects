![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# 📋 Project 6 | Segmentation

<p align="center">
  <img src="https://media1.giphy.com/media/SiM1Su83stF8untgcB/giphy.gif?cid=ecf05e47e2be75bebba76a5947a1bd17951a1f5d1bb53925&rid=giphy.gif">
</p>

<p align="justify">Este projeto foi realizado a partir do dataset [Câncer de Pele](https://www.kaggle.com/fanconic/skin-cancer-malignant-vs-benign) com o objetivo de fazer a segmentação entre o tumor benigno e maligno do câncer de pele. As imagens estão na pasta `data`.

Para fazer o teste de direcionamento, foi feito a conversão das cores da imagem `girassol.jpg` em 4 cores, então foi transformado em `girassol_4.png`. Após isso, foram retirados 100 imagens para treino de tumores benígnos e 100 imagens de tumores malígnos para fazer o mesmo tratamento da imagem dos girassóis, de diminuir para 4 cores. A tentativa de clusterização diminuindo a quantidade de informações em duas colunas utilizando o ***PCA***, foi feita mas a segmentação não funcionou como esperado.


Já na segunda tentativa foram retirados as mesmas 200 imagens totais dos tumores e foram tratados para a escala de cinza. Além disso, foi feito a equalização das imagens (acentuar detalhes não visíveis anteriormente) para tentar tentativa de segmentação mais clara. Após o tratamento, foi feito a tentativa novamente de segmentar mas não foi possível enxergar com clareza, as divisões delas.</p>

## Status do Projeto
Concluido ✅

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


## Autores
+ **Yukari Guenka Yshida**

## Agradecimentos
+ [André Aguiar](https://github.com/aguiarandre)
+ [Matheus Lavado](https://github.com/matheuslavado)
+ [Lucas White Rossi](https://github.com/LucasWhiteRossi)
+ [Raiana Rocha](https://github.com/Rairocha)