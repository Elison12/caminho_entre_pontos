from PIL import Image

def generate_image(matriz):
    """
    método responsável por gerar a imagem de saída
    """
    colors = {
        0: (255, 255, 255),  # Branco
        1: (0, 0, 0),        # Preto
        2: (255, 0, 0),      # Vermelho
        3: (0, 255, 0),      # Verde
        4: (0, 0, 255)       # Azul
    }

    height, width = matriz.shape
    image = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), colors[matriz[y, x]])

    return image