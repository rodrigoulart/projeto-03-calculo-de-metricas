# 🎯 Projeto 03 — Avaliação de Modelos de Classificação (Dígitos 0-9)  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Modelagem-lightgrey?logo=python)](https://scikit-learn.org/stable/)  
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos-green?logo=matplotlib)](https://matplotlib.org/)  
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualização-orange?logo=python)](https://seaborn.pydata.org/)  

> Terceiro projeto do **Bootcamp Machine Learning** da [DIO](https://www.dio.me/) em parceria com a **BairesDev**.  
> Aplicação prática de **avaliação de modelos de classificação multiclasse** usando o dataset de dígitos de 0 a 9.  

---

## **📌 Sobre o Projeto**  

Este projeto demonstra como calcular e analisar métricas de avaliação de modelos de classificação em Python, utilizando um dataset de dígitos (0–9).  

O programa realiza:  

1. Treinamento de um classificador RandomForest.  
2. Cálculo das métricas: **Acurácia, Precisão, Recall, F1-Score e Especificidade**.  
3. Plotagem da **matriz de confusão** com os valores de cada classe.  
4. Geração da **Curva ROC Multiclasse** utilizando abordagem One-vs-Rest.  

**Objetivos do projeto**:  
- 🧮 Avaliar desempenho de modelos de classificação multiclasse.  
- 📊 Visualizar matriz de confusão com contagem de predições corretas e incorretas.  
- 📈 Plotar curva ROC para cada classe do dataset.  
- 💾 Explorar ferramentas de análise visual para aprendizado de máquina.  

---

## **🛠️ Tecnologias e Ferramentas**  

- **Python 3.10+** ([link](https://www.python.org/))  
- **Scikit-Learn** → Treinamento do modelo e métricas  
- **Matplotlib** → Plotagem da curva ROC  
- **Seaborn** → Visualização da matriz de confusão  

---

## **📂 Estrutura do Projeto**  

```text
projeto-03-avaliacao-classificacao/
├── LICENSE                      # Arquivo de licença MIT
├── README.md                    # Este arquivo
└── projeto_calculo_metricas.py  # Script principal com todo o código do projeto
