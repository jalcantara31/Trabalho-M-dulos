import streamlit as st
import random as rdm

st.title("Gerador de Senhas 🔐")
st.header("Customize sua senha")

tamanho=st.slider("Tamanho da senha",8,32,12)

def criar_senha(tamanho):
    senha=''
    for i in range(tamanho):
        opcoes=[1,2,3,4]
        escolha=rdm.choice(opcoes)
        if escolha==1:
            caractere=rdm.choice("abcdefghijklmnopqrstuwxyz")
        elif escolha==2:
            caractere=rdm.randint(0,9)
        elif escolha==3:
            caractere=rdm.choice("ABCDEFGHIJKLMNOPQRSTUWXYZ")
        elif escolha==4:
            caractere=rdm.choice(",.;#$%&*!@/")
        senha+=str(caractere)
    return senha

if st.button("Criar Senha"):
    st.session_state.senha_gerada = criar_senha(tamanho)

if "senha_gerada" in st.session_state:
    st.success(f"Senha gerada: {st.session_state.senha_gerada}")
#O f"..." serve para utilizarmos uma string e, dentro dela, utilizarmos uma variável, chamando a variável com {}
