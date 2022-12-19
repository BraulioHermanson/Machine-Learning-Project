#!/usr/bin/env python
# coding: utf-8

# ## Streamlit
# - https://streamlit.io/
# - https://docs.streamlit.io/library/get-started/main-concepts
# - https://docs.streamlit.io/library/api-reference
#     - title: título da página
#     - number_input: entrada de dados numéricos
#     - button: botão
#         - é possível atribuir ações a esse botão

# In[ ]:


# Instalando
# !pip install streamlit


# In[ ]:


# Importando o streamlit
import streamlit as st
from joblib import load

reg = load('regressor.joblib')

st.title('Prevendo a venda quantidade')

preco = st.number_input('Preço de Venda')
desconto = st.number_input('Desconto')

botao = st.button('PREVER')

if botao:
    texto = reg.predict([[preco,desconto]])
    st.write(texto)

