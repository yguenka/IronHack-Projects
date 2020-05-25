import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from PIL import Image
import joblib

model = joblib.load('pipe.pkl')


st.title('Skin Cancer Scanner')

def sobre():
    st.header("Sobre o aplicativo")
    st.write("Este aplicativo tem o intuito de analisar a chance de ter o câncer de pele através de uma foto.")

    st.header("O que é Câncer de Pele ?")
    st.write("O câncer de pele é um tumor que atinge a pele, sendo o câncer mais frequente no Brasil e no mundo." )
    st.write("É mais comum em pessoas com mais de 40 anos e é considerado raro em crianças e pessoas negras." )
    st.write("Causado principalmente pela exposição excessiva ao sol.")
    st.write("O câncer de pele ocorre quando as células se multiplicam sem controle.")

    st.header("Tipos de Câncer")
    st.write("MELANOMA")
    st.write("Tem origem nas células produtoras da melanina, sustância que determina a cor da pele.")
    st.write(" - Pele branca: Comum no corpo todo - pele e mucosas (em forma de manchas , pintas ou sinais).")
    st.write(" - Pele escura: Comum nas áreas mais claras como palma das mãos e dos pés.")
    st.write("NÃO MELANOMA")
    st.write("Em ambas as peles, é caracterizada por uma lesão (ferida ou nódulo), ou sobre ela.")
    st.write(" - Carcinoma basocelular: mais comum e menos agressivo. A evolução é lenta.")
    st.write(" - Carcinoma epidermóide: por ter grande possibilidade de apresentar metástase, possui maior gravidade. Ela surge por meio de uma ferida ou sobre uma cicatriz, principalmente as que são decorrentes de queimadura.")

    st.write("O método abaixo serve para avaliar o risco de uma mancha ou sinal. Cada letra corresponde a um aspecto de sinal de pele que requer atenção.")
    image = Image.open('abcde.jpg')
    st.image(image, caption='Fonte: https://gbm.org.br/dezembro-laranja-importancia-de-uma-campanha-contra-o-cancer-de-pele/abcde/')

    st.header("Como funciona o aplicativo ?")
    st.write("1. Insira a foto para análise. De preferência tirada sob luz do flash com foco ajustado na mancha e com as com dimensões de 224 x 224")
    st.write("2. Vamos analisar a foto diminuindo a resolução para 12 x 12 como na ilustração abaixo.")
    image2 = Image.open('ilustracao.jpg')
    st.image(image2, caption='imagem real x imagem tratada')
    st.write("3. Após a análise, vamos retornar a % de chance de ter câncer de pele.")
    st.write("Vale ressaltar que este aplicativo não substitui um exame médico. Ao constatar uma anomalia citada acima, consulte um médico especiailsta.")
    
    st.write("Fonte: https://saude.gov.br/saude-de-a-z/cancer-de-pele")

def scanner():
    st.header("Scanner")

    st.write("Imagem ideal: focalizada e tirada com flash, com dimensões de 224 x 224")
    uploaded_file = st.file_uploader("Escolha uma imagem...", type="jpg",)
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image)
        new_image = image.resize((224, 224))
        scaled = np.array(new_image) / 255.0
        X_upload = scaled.reshape(scaled.shape[0] * scaled.shape[1] * scaled.shape[2])
        X_upload = pd.DataFrame(X_upload).T
        result = model.predict_proba(X_upload)
        st.title(f"Chance de câncer de pele: {(result[0][1]*100):.2f}%")
        st.write("Lembrando que esse resultado não substitui um exame médico.") 
        st.write("Procure um médico.")

def prevencao():
    st.header("Prevenção")
    st.write("As recomendações para prevenções são: ")
    st.write(" - Evitar exposição ao sol, principalmente nos horários entre 10h e 16h;")
    st.write(" - Uso de filtros solares acima do fator FPS 15;")
    st.write(" - Utilização de óculos de sol com proteção UV; e")
    st.write(" - Roupas e acessórios como chapéus / guarda-sol / sombrinhas que protegem o corpo.")
    st.write("Em caso de exposição necessária, o filtro solar deve ser aplicado corretamente, já que o real fator de proteção desses produtos varia com a espessura da camada de creme aplicada, a frequêcnia da aplicação, a perspiraçãoe a exposição à água. E vale lembrar que isso pode ser aplicado também para protetor labial.")
    st.write("As recomendações em especial devem ser direcionadas aos bebês e às crianças, pois na infância é o período da vida mais suscetível aos efeitos danosos da radiação UV que se manifestam mais tardiamente na fase adulta")
    
    st.write("Fonte: https://saude.gov.br/saude-de-a-z/cancer-de-pele")

st.sidebar.title('Skin Cancer Scanner')

goto = st.sidebar.radio('O aplicativo:', ['Sobre', 'Scanner', 'Prevenção'])
if goto == 'Sobre':
    sobre()
if goto == 'Scanner':
    scanner()
if goto == 'Prevenção':
	prevencao()