import streamlit as st

import numpy as np
import gerador_paletta as gp


st.title("Gerador de paletas")

#carregando imagem
imagem = st.file_uploader("Envie sua imagem",["jpg","jpeg"])
col1,col2 = st.columns([.7,.3])

if imagem:
    col1.image(imagem)
    n_cores = col1.slider(
        "quantidade de cores",
        min_value=2,
        max_value=10,
        value=5,
    )
    btn_gera_paleta = col2.button("Gerar paleta!")

    if btn_gera_paleta:
        # aplicação do algoritmo
        cores, cores_hex = gp.get_Palette(imagem,n_cores)
        figure = gp.show(cores)
        col2.pyplot(fig = figure)
        col2.code(f"{cores_hex}")
        
        col2.download_button("Download",gp.save(figure),"paleta.png","image/png")
        