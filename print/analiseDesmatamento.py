#!/usr/bin/env python
# coding: utf-8

# In[2]:


dataset = open('datasetDesmatamento.csv')


# <h1>Uma análise do desmatamento da Amazônia Legal (2004-2019)</h1><br>
# Este estudo foi feito por <b>Gustavo Duregger</b>. <br>
# A interpretação e os demais arquivos podem ser encontrados <a href='https://github.com/GustavoDuregger/AnaliseDesmatamento2004-2019'>neste link</a>. 

# In[1]:


#Importações
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[2]:


#Leitura do arquivo .csv
desmatamento = pd.read_csv('datasetDesmatamento.csv')


# In[3]:


#Retirando a coluna "AMZ Legal" e "Ano/Estados" para não interfirir no modelo, a partir do comando "amznn"
amznn = desmatamento.drop(columns=['AMZ LEGAL','Ano/Estados'])


# In[10]:


#Resumo de informações em colunas
desmatamento.describe()


# In[11]:


#Renomeando as colunas
desmatamento.columns = ['Ano/Estados','Acre','Amazonas','Amapá','Maranhão','MatoGrosso','Pará','Rondônia','Roraima','Tocantins','AMZ LEGAL']


# In[12]:


#Exibição da tabela
desmatamento.head(16)


# In[13]:


#Desmatamento ao longo dos anos
amznn.plot()


# In[14]:


desmatamentoMaximo=amznn.max() #numero mais alto registrado


# In[15]:


desmatamentoMaximo.plot(kind='bar', figsize=(11,5), grid = False, rot=0, color='green')


# In[18]:


#MT,PA,RO criando o ponto crítico


# In[16]:


#Soma dos Anos
somaAcre=sum(desmatamento.Acre)
somaAmazonas=sum(desmatamento.Amazonas)
somaAmapa=sum(desmatamento.Amapá)
somaMaranhao=sum(desmatamento.Maranhão)
somaMatoGrosso=sum(desmatamento.MatoGrosso)
somaPara=sum(desmatamento.Pará)
somaRondonia=sum(desmatamento.Rondônia)
somaRoraima=sum(desmatamento.Roraima)
somaTocantins=sum(desmatamento.Tocantins)

soma = {'Acre': [somaAcre,somaAcre],
       'Amazonas': [somaAmazonas,somaAmazonas],
       'Amapa': [somaAmapa,somaAmapa],
       'Maranhão': [somaMaranhao,somaMaranhao],
       'MatoGrosso': [somaMatoGrosso,somaMatoGrosso],
       'Para': [somaPara,somaPara],
       'Rondonia': [somaRondonia,somaRondonia],
       'Roraima': [somaRoraima,somaRoraima],
       'Tocantins': [somaTocantins,somaTocantins]}

somadf = pd.DataFrame(data=soma)
somadf.head()


# In[17]:


#Plotagem de Soma
somadf.plot(kind='bar', figsize=(11,5), grid = False, rot=0, color='green')

