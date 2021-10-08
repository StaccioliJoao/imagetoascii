import PIL.Image

# caracteres que vão ser utilizados para converter os pixels
caracteres_ascii = ['@', '#', '%', '?', '*', '+', ';', ':', ',', "'", '.']

# Reescala a imagem mantendo o aspecto da imagem


def reescalar(imagem, novo_comprimento=100):
    w, h = imagem.size
    ratio = h / w / 1.65
    nova_altura = int(novo_comprimento * ratio)
    imagem_rescalada = imagem.resize((novo_comprimento, nova_altura))
    return(imagem_rescalada)


# Converte a imagem para greyscale
def greyscaler(imagem):
    cinza = imagem.convert("L")
    return(cinza)


# converte os pixels para caracteres
def pixels_para_caracteres(imagem):
    pixels = imagem.getdata()
    caracteres = ''.join([caracteres_ascii[pixel // 25] for pixel in pixels])
    return(caracteres)


# Entrada da imagem
def main(novo_comprimento=100):
    caminho = input("Digite o caminho da imagem no seu computador:\n")
    try:
        imagem = PIL.Image.open(caminho)
    except:
        print(f'{caminho} não é um endereçamento valido!')
        return

    # converte a imagem para caracteres
    imagem = reescalar(imagem)
    imagem = greyscaler(imagem)
    nova_imagem = pixels_para_caracteres(imagem)

    # formata a imagem para manter o tamanho dela correto
    pixel_quant = len(nova_imagem)
    imagem_ascii = "\n".join(nova_imagem[i:(i + novo_comprimento)] for i in range(0, pixel_quant, novo_comprimento))

    # mostrar a imagem e salvar a imagem em um txt
    print(imagem_ascii)
    with open("imagem_ascii.txt", "w") as arq:
        arq.write(imagem_ascii)


main()
