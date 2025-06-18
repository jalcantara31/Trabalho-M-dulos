import streamlit as st
import random as rdm

st.title("Gerador de Senhas")
st.header("Customize sua senha")

tamanho=st.slider("Tamanho da senha",8,32,12)
senha=''
for i in range(tamanho):
    escolha=rdm.choice(1,2)
    if escolha==1:
        caractere=rdm.choice("abcdefghijklmnopq")
st.button("Criar Senha")
st.code(senha_gerada)
