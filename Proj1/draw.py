import os
import pygame
from pygame.locals import *
from levels import Piece
from utils import Button

def draw_main_menu(screen):
    screen.fill((95, 158, 160))

    # Title - Load, Scale and Position
    directory = os.path.dirname(__file__)
    image_path = os.path.join(directory, 'images', "title.png")
    img = pygame.image.load(image_path)

    img_width, img_height = img.get_size()
    new_width = img_width * 3
    new_height = img_height * 3
    
    scaled_image = pygame.transform.scale(img, (new_width, new_height))
    screen_width, screen_height = screen.get_size()
    image_width, image_height = scaled_image.get_size()

    x = (screen_width - image_width) // 2
    y = ((screen_height - image_height) // 2) - 200
    screen.blit(scaled_image,(x, y))

def draw_level_menu(screen):
    screen.fill((95, 158, 160))
    screen_width, screen_height = screen.get_size()

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"Level",(255,255,255),screen_width/2,70,80)
    write_on_text(screen,"Choose AI search method:",(255,255,255),260,160,50)
    pygame.display.flip()

def draw_level_select_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    screen_width, screen_height = screen.get_size()
    

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"Level Selection",(255,255,255),screen_width/2,70,80)
    pygame.display.flip()

    # To draw the level buttons, as they are 9, lets create a 3x3 grid

def draw_level_button(screen,text,x,y):
    level_button_width = 100
    level_button_height = 100

    level_button = Button(x , y, level_button_width, level_button_height, text, (0, 0, 0), (255, 255, 255), 80)
    level_button.draw(screen)

def draw_options_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    # Title - Load, Scale and Position
    directory = os.path.dirname(__file__)
    image_path = os.path.join(directory, 'images', "title.png")
    img = pygame.image.load(image_path)

    img_width, img_height = img.get_size()
    new_width = img_width * 3
    new_height = img_height * 3

    scaled_image = pygame.transform.scale(img, (new_width, new_height))
    screen_width, screen_height = screen.get_size()
    image_width, image_height = scaled_image.get_size()

    x = (screen_width - image_width) // 2
    y = ((screen_height - image_height) // 2) - 200
    screen.blit(scaled_image, (x, y))

    # Adicione outros elementos do menu de opções conforme necessário
    # Exemplo: Botões para ajustar configurações
    draw_option_button(screen, "Controls", 200, 300)
    draw_option_button(screen, "Credits", 200, 425)
    draw_option_button(screen, "Return", 200, 550)

def draw_results_menu(screen,time_total,memory_total_kb,result):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    screen_width, screen_height = screen.get_size()
    

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"RESULTS",(255,255,255),screen_width/2,70,80)
    write_on_text(screen,"Steps: "+str(len(result)),(255,255,255),screen_width/2,200,40)
    write_on_text(screen,"Time: "+str(time_total)+" seconds.",(255,255,255),screen_width/2,250,40)
    write_on_text(screen,"Memory: "+str(memory_total_kb)+" KB",(255,255,255),screen_width/2,300,40)
    pygame.display.flip()

def draw_option_button(screen, text, x, y):
    # Configurações para os botões de opção
    option_button_width = 400
    option_button_height = 100

    option_button = Button(x * 2.2, y, option_button_width, option_button_height, text, (0, 80, 255), (255, 255, 255), 60)
    option_button.draw(screen)


def draw_calculating_screen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", 48)
    text = font.render("Calculating...", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def draw_heuristic_choice_screen(screen):
    screen.fill((95, 158, 160)) 

    # Definindo as posições e textos dos botões
    screen_width, screen_height = screen.get_size()
    button_width = 400
    button_height = 100
    button_y_start = screen_height // 2 - 150
    button_x = (screen_width - button_width) // 2

    # Criando os botões de escolha de heurística
    button_incorrect = Button(button_x, button_y_start, button_width, button_height, "Peças Incorretas", (125, 0, 150), (255, 255, 255), 36)
    button_manhattan = Button(button_x, button_y_start + 150, button_width, button_height, "Distância de Manhattan", (125, 0, 150), (255, 255, 255), 36)

    button_incorrect.draw(screen)
    button_manhattan.draw(screen)

    pygame.display.flip()

    return button_incorrect, button_manhattan


def draw_credits_screen(screen, screen_width):
    screen.fill((95, 158, 160))  # Cor de fundo para a tela de créditos

    # Adicione elementos da tela de créditos
    font = pygame.font.SysFont(None, 55)
    credits_text = [
        "Game Developed by:",
        "Francisco Lopes",
        "João Fernandes",
        "Rui Silveira"
    ]

    # Desenha o texto de créditos na tela
    y = 200
    for line in credits_text:
        text = font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, y))
        screen.blit(text, text_rect)
        y += 60

def draw_menu_settings(screen):
    screen.fill((95, 158, 160))
    screen_width, screen_height = screen.get_size()
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"SETTINGS",(255,255,255),screen_width/2,70,80)
    pygame.display.flip()


def write_on_text(screen,text,color,x,y,font_size):
    directory = os.path.dirname(__file__)
    font_path = os.path.join(directory, 'font', "RadiantKingdom-m5LeV.ttf")
    font = pygame.font.SysFont(font_path,font_size)
    text = font.render(text, True, color) 
    text_rect = text.get_rect(center=(x,y))
    screen.blit(text, text_rect)
    
def draw_board_initial(screen, level, screen_width, screen_height,initial_x,initial_y):
    # screen.fill((95, 158, 160))  # Cor de fundo para o tabuleiro

    initial_state = level
    # Desenha o tabuleiro
    for row in range(len(initial_state)):
        for col in range(len(initial_state[row])):
            x = (col * (screen_width // len(initial_state[row]))+initial_x)
            y = (row * (screen_height // len(initial_state))+initial_y)
            #pygame.draw.rect(screen, (192, 192, 192), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)), 5)

            # Desenha o conteúdo do tabuleiro
            if initial_state[row][col] == Piece.NORMAL:
                # Desenha um círculo para representar uma peça normal
                pygame.draw.rect(screen, (51, 153, 255), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))


            elif initial_state[row][col] == Piece.SPECIAL:
                # Desenha um círculo para representar uma peça especial
                pygame.draw.rect(screen, (0, 204, 0), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))

def draw_game_human_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    screen_width, screen_height = screen.get_size()
    

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"Have Fun!",(255,255,255),screen_width/2,70,80)
    pygame.display.flip()

def draw_board_change(screen, level_actual, level_objective, screen_width, screen_height,initial_x,initial_y):
    objective_state = level_objective
    initial_state = level_actual

    # Desenha o tabuleiro
    for row in range(len(objective_state)):
        for col in range(len(objective_state[row])):
            x = (col * (screen_width // len(objective_state[row]))+initial_x)
            y = (row * (screen_height // len(objective_state))+initial_y)
            #pygame.draw.rect(screen, (192, 192, 192), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)), 5)

            # Verifica se o estado atual é diferente do objetivo
            if initial_state[row][col] != objective_state[row][col]:
                # Desenha o conteúdo do tabuleiro
                if objective_state[row][col] == Piece.NORMAL:
                    # Desenha um círculo para representar uma peça normal
                    pygame.draw.rect(screen, (51, 153, 255), (x, y, screen_width // len(objective_state[row]), screen_height // len(objective_state)))

                elif objective_state[row][col] == Piece.SPECIAL:
                    # Desenha um círculo para representar uma peça especial
                    pygame.draw.rect(screen, (0, 204, 0), (x, y, screen_width // len(objective_state[row]), screen_height // len(objective_state)))

def draw_steps_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    screen_width, screen_height = screen.get_size()
    

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"STEP HISTORY:",(255,255,255),screen_width/2,70,80)
    pygame.display.flip()

def draw_arrow(screen, start_pos, end_pos):
    # Calcula a direção da seta
    direction = (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])

    # Desenha as pontas da seta
    pygame.draw.polygon(screen, (51, 153, 255), ((end_pos[0], end_pos[1]), (end_pos[0] - direction[0] - direction[1], end_pos[1] - direction[1] + direction[0]), (end_pos[0] - direction[0] + direction[1], end_pos[1] - direction[1] - direction[0])))

