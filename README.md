# Trabalho Final - Pós-Graduação em Ciência de Dados e Machine Learning

**Nomes dos Integrantes:** 

1- João Pedro Melo Rodrigues

Este repositório foi criado como parte do trabalho final da pós-graduação em Ciência de Dados e Machine Learning. O objetivo deste projeto é aplicar os conhecimentos adquiridos durante o curso utilizando a metodologia CRISP-DM.

## Objetivos do Projeto

Nosso objetivo será investigar a relação entre o consumo de álcool, o índice de massa corporal (IMC) e a expectativa de vida.

Seguiremos as seguintes etapas. 

1. Entendimento do Problema.
2. Realizar análise exploratória dos dados e Limpeza e preparação dos dados para modelagem..
3. Desenvolvimento de modelos preditivos para a expectativa de vida.
4. Avaliação e validação dos modelos desenvolvidos.
5. Deployment.

## Estrutura do projeto

Estrutura básica do projeto abaixo:

```
projeto-ciencia-de-dados
│   README.md
└───ml
│   └─── data
│       └─── Life Expectancy Data.csv
│       CRISP-DM Projeto Final.ipynb
└─── app
    │   **.py
    └─── docs
        └─── predict.yaml
    |   normalizer.pkl
    |   model.pkl
    |   encoder.pkl
```

Pasta `ml` = Pasta de machine learning e modelo estatistico

Pasta `app` = Aplicacao flask para servir o modelo. Disponibilizada em uma imagem do docker

## Machine Learning - Pasta ml

### Arquivo de Dados

O arquivo utilizado para este projeto é `Life Expectancy Data.csv`, presente dentro de ml/data, disponivel em https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who?resource=download que contém dados relevantes para a análise proposta. Este arquivo inclui informações sobre expectativa de vida e variáveis associadas, que serão exploradas e modeladas durante o desenvolvimento do projeto.

## Aplicação - Pasta app

### Deployment

O deploy é feito via docker. Foi optado por nao usar compose, para simplicidade. Entretanto, nada impediria de usar compose, helm charts ou qualquer outra estrutura no k8s.

## Construir

1 - A partir da raiz do projeto, gere o modelo. Execute no shell de preferencia:

```powershell
cd ml
pip install numpy
pip install flask
pip install pandas
pip install scikit-learn
pip install seaborn 
pip install plotly.express
pip install XGBoost
```

2 - Após isto, pode executar o notebook normalmente

```powershell
jupyter notebook
```

3 - A partir da raiz do projeto, gere a imagem do docker

```powershell
cd app
docker build . -t ml-joao-pedro
```

4 - Execute na porta 5000
```powershell
docker run -p 5000:5000 ml-joao-pedro
```
