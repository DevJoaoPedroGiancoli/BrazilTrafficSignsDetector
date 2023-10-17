import cv2

# Carregue a imagem
image_path = r"save_test\foto_inteira_do_id_14.jpg"
imagem = cv2.imread(image_path)
clone = imagem.copy()

# Inicialize as variáveis para as coordenadas dos pontos inicial e final
ponto_inicial = None
ponto_final = None
clicando = False

def selecionar_area(event, x, y, flags, param):
    global ponto_inicial, ponto_final, clicando, clone

    # Se o evento for um clique duplo, redefina a imagem de visualização
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clone = imagem.copy()
        ponto_inicial = None
        ponto_final = None

    # Se o botão esquerdo do mouse for pressionado, registre o ponto inicial
    elif event == cv2.EVENT_LBUTTONDOWN:
        ponto_inicial = (x, y)
        clicando = True

    # Se o botão esquerdo do mouse for liberado, registre o ponto final
    elif event == cv2.EVENT_LBUTTONUP:
        ponto_final = (x, y)
        clicando = False

        # Desenhe um retângulo na imagem de visualização
        cv2.rectangle(clone, ponto_inicial, ponto_final, (0, 255, 0), 2)
        cv2.imshow("Selecionar Área", clone)

# Crie uma janela de visualização para a imagem
cv2.namedWindow("Selecionar Área")
cv2.setMouseCallback("Selecionar Área", selecionar_area)

while True:
    # Exiba a imagem de visualização
    cv2.imshow("Selecionar Área", clone)
    key = cv2.waitKey(1) & 0xFF

    # Se a tecla "r" for pressionada, redefina a imagem de visualização
    if key == ord("r"):
        clone = imagem.copy()
        ponto_inicial = None
        ponto_final = None

    # Se a tecla "c" for pressionada, saia do loop
    elif key == ord("c"):
        break

# Se a área de interesse foi selecionada, obtenha as coordenadas
if ponto_inicial and ponto_final:
    x1, y1 = ponto_inicial
    x2, y2 = ponto_final
    print("Coordenadas da área de interesse: (x1, y1, x2, y2) =", (x1, y1, x2, y2))

# Feche a janela e libere recursos
cv2.destroyAllWindows()