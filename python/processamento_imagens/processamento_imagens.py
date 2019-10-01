# Talvez seja necessário instalar um pacote para visualizar as imagens
# https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
from skimage import data, io, filters, color, exposure
from argparse import ArgumentParser


def parse_args():
    ap = ArgumentParser()

    ap.add_argument(
        '--exemplo',
        required=True,
        type=str,
        choices=['arestas', 'tons_de_cinza', 'equalizacao', 'recorte'],
        help='Qual exemplo executar?'
    )

    return ap.parse_args()


def arestas():
    image = data.coins()
    io.imshow(image)
    io.show()
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()


def tons_de_cinza():
    image = data.astronaut()
    io.imshow(image)
    io.show()
    grayscale = color.rgb2gray(image)
    io.imshow(grayscale)
    io.show()


def equalizacao():
    image = data.coins()
    io.imshow(image)
    io.show()
    equalized = exposure.equalize_hist(image)
    io.imshow(equalized)
    io.show()


def recorte():
    image = data.astronaut()
    io.imshow(image)
    io.show()
    cropped = image[50:200, 50:200, :]
    io.imshow(cropped)
    io.show()


if __name__ == '__main__':
    args = parse_args()

    if args.exemplo.lower() == 'arestas':
        arestas()
    elif args.exemplo.lower() == 'tons_de_cinza':
        tons_de_cinza()
    elif args.exemplo.lower() == 'equalizacao':
        equalizacao()
    elif args.exemplo.lower() == 'recorte':
        recorte()
