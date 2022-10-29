from PIL import Image
from pathlib import Path
import io
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import to_hex
from sklearn.cluster import KMeans

def get_Palette(img,n_cores):
    # salvar a imagem do streamlit
    with open('imagem.jpg', 'wb') as file:
        file.write(img.getbuffer())
    # ler a imagem
    image = Image.open('imagem.jpg')
    # transformar os pixels em linhas de uma matriz
    N, M = image.size
    X = np.asarray(image).reshape((M*N, 3))
    # criar e aplicar o k-means na imagem
    model = KMeans(n_clusters=n_cores, random_state=42).fit(X)
    # capturar os centros (cores médias dos grupos)
    cores = model.cluster_centers_.astype('uint8')[np.newaxis]
    cores_hex = [to_hex(cor/255) for cor in cores[0]]

    # apagar imagem salva
    Path('imagem.jpg').unlink()
    # retornar cores
    return cores, cores_hex


def show(cores):
    fig = plt.figure()
    plt.imshow(cores)
    plt.axis('off')
    return fig

def save(fig):
    img = io.BytesIO()
    plt.axis("off")
    return img