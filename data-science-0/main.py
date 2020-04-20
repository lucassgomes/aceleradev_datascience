#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[11]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[10]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return len(black_friday.query('Age == "26-35" & Gender == "F"'))


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[13]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday.User_ID.nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[11]:


def q5():
    # Retorne aqui o resultado da questão 5.
    nrows = black_friday.shape[0]
    return (nrows - black_friday.dropna().shape[0])/nrows


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[12]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isna().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[14]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday.Product_Category_3.mode().sum()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[8]:


def q8():
    # Retorne aqui o resultado da questão 8.
    min_values = black_friday.Purchase.min()
    max_values = black_friday.Purchase.max()
    return float(np.mean((black_friday.Purchase - min_values) / (max_values-min_values)))


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[7]:


def q9():
    # Retorne aqui o resultado da questão 9.
    mean = black_friday.Purchase.mean()
    std = black_friday.Purchase.std()
    purchaseNorm = (black_friday.Purchase - mean) / std
    return int(((purchaseNorm >= -1) & (purchaseNorm <= 1)).sum())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[47]:


def q10():
    # Retorne aqui o resultado da questão 10.
    aux_isna_product_category_2 = black_friday[black_friday.Product_Category_2.isna() == True]
    return aux_isna_product_category_2.Product_Category_2.equals(aux_isna_product_category_2.Product_Category_3)

