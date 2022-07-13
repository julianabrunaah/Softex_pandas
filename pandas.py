#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
df=pd.read_csv("notas_alunos.csv", sep=";")
df["MEDIA"] = (df["NOTA1"]+df["NOTA2"])/2
df.loc[df["MEDIA"]>=7, "SITUAÇÃO"]="APROVADO"
df.loc[df["MEDIA"]<7, "SITUAÇÃO"]="REPROVADO"
df.loc[df["FALTAS"]>=5, "SITUAÇÃO"]="REPROVADO"
df.to_csv("alunos_situacao.csv", sep=";")
print(df)


# In[30]:


somamedia= df["MEDIA"].sum()
mediageral= somamedia/7
maior= df["MEDIA"].max()
maiorfalta = df["FALTAS"].max()
print("Media geral = "+str(mediageral))
print("Maior media = "+str(maior))
print("Maior número de faltas = "+str(maiorfalta))


# In[ ]:




