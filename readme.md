

# 🛢️ OilSight — Previsão do Preço do Petróleo com ARIMA & Prophet

**OilSight** é uma aplicação interativa e 100% local que permite visualizar e prever os preços do petróleo tipo **Brent** e **WTI** com modelos de séries temporais como **ARIMA** e **Prophet**.

> 📌 Ideal para portfólio, estudos e demonstração prática de análise preditiva sem depender de APIs pagas ou deploy.


## 🎯 Funcionalidades

✅ Visualização interativa dos dados históricos  
✅ Previsão futura com ARIMA ou Prophet  
✅ Escolha de horizonte: 30, 60 ou 90 dias  
✅ Gráficos profissionais com Plotly  
✅ Avaliação do modelo com **MAPE** e **RMSE**  
✅ Salvamento local dos modelos treinados (`.pkl`)  
✅ Interface simples e responsiva com Streamlit



## 🏗️ Estrutura do Projeto

```plaintext
oil_sight/
├── app.py                  # Interface principal com Streamlit
├── data/                   # Arquivos CSV (Brent e WTI)
│   ├── brent.csv
│   └── wti.csv
├── models/                 # Modelos ARIMA salvos com pickle
│   ├── arima_brent.pkl
│   └── arima_wti.pkl
├── utils/
│   ├── loader.py           # Carregamento e preparação dos dados
│   └── forecast.py         # Modelos ARIMA e Prophet + avaliação
├── README.md



## 📦 Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/oilsight.git
cd oilsight
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# ou
source venv/bin/activate     # Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se ainda não tiver o arquivo, crie um `requirements.txt` com o seguinte conteúdo:

```txt
streamlit
pandas
plotly
statsmodels
prophet
scikit-learn
```

### 4. Rode o aplicativo

```bash
streamlit run app.py
```



## 📈 Fonte dos Dados

Os arquivos CSV foram obtidos manualmente em:

* [Investing.com - Brent Oil](https://www.investing.com/commodities/brent-oil-historical-data)
* [Investing.com - WTI Crude](https://www.investing.com/commodities/crude-oil-historical-data)



## 🧪 Modelos Utilizados

### 🔸 ARIMA

Modelo estatístico tradicional de séries temporais, ideal para dados estacionários.

* Implementado com `statsmodels`
* Avaliado com `MAPE` e `RMSE`
* Salvo localmente em `/models/` com `pickle`

### 🔸 Prophet

Modelo criado pelo Facebook, ideal para séries com tendências sazonais.

* Implementado com `prophet`
* Facilita decomposição da série
* Útil para comparações com ARIMA



## 🧠 Tecnologias Usadas

| Ferramenta     | Finalidade                       |
| -------------- | -------------------------------- |
| `Python 3.x`   | Linguagem principal              |
| `Streamlit`    | Interface interativa local       |
| `pandas`       | Manipulação de dados             |
| `Plotly`       | Visualização de séries temporais |
| `statsmodels`  | Modelo ARIMA                     |
| `prophet`      | Modelo Prophet (Facebook)        |
| `scikit-learn` | Métricas de erro (MAPE, RMSE)    |
| `pickle`       | Salvamento local de modelos      |



## 📚 Como usar

1. Escolha entre **Brent** ou **WTI**
2. Visualize os dados históricos
3. Selecione o modelo de previsão: **ARIMA** ou **Prophet**
4. Escolha o período: **30**, **60** ou **90** dias
5. Clique em **Gerar previsão**
6. Visualize a previsão no gráfico e na tabela
7. Veja as métricas de erro (caso ARIMA)


## 💡 Ideias Futuras

* Importar dados automaticamente via API
* Otimização de parâmetros ARIMA via GridSearch
* Forecast com variáveis externas (exógenas)
* Exportação das previsões em CSV ou Excel
* Dashboard com múltiplos ativos financeiros
* Modo Dark / Light Theme


## ✍️ Autor

Desenvolvido por **Pedro Henrique** como projeto pessoal para estudo, aprendizado e portfólio.
🔗 [LinkedIn](https://www.linkedin.com/in/pedro-henrique-rossetto-33216b245/)










