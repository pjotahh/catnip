import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

# Configurações da tela
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('CAT-NIP')
tamanho_sprite = (500, 500)

# Caminho para a pasta de assets
caminho_assets = os.path.join(os.path.dirname(__file__), 'assets')

# Imagens de animação "idle" (parado)
sprites = [
    pygame.transform.scale(pygame.image.load(os.path.join(caminho_assets, 'sprites', f'base_{i}.png')).convert_alpha(), tamanho_sprite)
    for i in [1, 2, 3, 4, 3, 2]
]

# Variáveis de controle
executando = True
cat = pygame.Rect(470, 280, 200, 200)

# Controle da animação
indice_frame = 0  # Índice da imagem atual
tempo_entre_frames = 150  # Milissegundos entre cada frame
ultimo_tempo = pygame.time.get_ticks()  # Tempo inicial

while executando:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Preenche a tela com preto (limpa a tela)
    tela.fill((0, 0, 0))
    
    # Atualiza o frame da animação de "parado" (idle)
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - ultimo_tempo > tempo_entre_frames:
        indice_frame = (indice_frame + 1) % len(sprites)  # Alterna os frames em loop
        ultimo_tempo = tempo_atual
    
    # Desenha a imagem atual na posição do "cat"
    tela.blit(sprites[indice_frame], (cat.x, cat.y))
    
    pygame.display.flip()
    pygame.time.delay(30)
