import os
from PIL import Image, ImageOps

base = os.path.dirname(os.path.abspath(__file__))
origem = os.path.join(base, "fotos-originais")
destino = os.path.join(base, "img")
os.makedirs(destino, exist_ok=True)

escolhidas = {
    "DSC03830.JPG": "hero-sala.jpg",
    "DSC03811.JPG": "logo-parede.jpg",
    "DSC03760.JPG": "recepcao-certificados.jpg",
    "DSC03817.JPG": "recepcao.jpg",
    "DSC03819.JPG": "cadillac.jpg",
    "DSC03820.JPG": "cadillac-detalhe.jpg",
    "DSC03821.JPG": "reformer-torre.jpg",
    "DSC03826.JPG": "reformer.jpg",
    "DSC03823.JPG": "chair.jpg",
    "DSC03824.JPG": "barrel-ladder.jpg",
    "DSC03822.JPG": "corredor.jpg",
    "DSC03761.JPG": "toalha-unite.jpg",
    "DSC03818.JPG": "trx.jpg",
    "DSC03829.JPG": "sala-tv.jpg",
    "DSC03816.JPG": "bolas.jpg",
}

for nome_origem, nome_final in escolhidas.items():
    caminho = os.path.join(origem, nome_origem)
    img = Image.open(caminho)
    img = ImageOps.exif_transpose(img)  # aplica orientação EXIF, se houver
    img = img.convert("RGB")
    if img.width > 1600:
        proporcao = 1600 / img.width
        img = img.resize((1600, int(img.height * proporcao)), Image.LANCZOS)
    img.save(os.path.join(destino, nome_final), "JPEG", quality=82, optimize=True)
    print(nome_final, img.size)
