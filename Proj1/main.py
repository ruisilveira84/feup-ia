import sys
import pygame
from pygame.locals import *
from draw import *
from utils import *
from levels import levels as level_select
from gamelogic import *
from levels import *
from algorithms import *
import tracemalloc
import threading
from queue import Queue, Empty

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

screen_width, screen_height = screen.get_size()

class GameState:
    MAIN_MENU = "main_menu"
    OPTIONS_MENU = "options_menu"
    CREDITS_SCREEN = "credits_screen"
    PLAYING = "Interface"



# Variáveis para o menu principal
button_start_width = 400
button_start_height = 100
x_button_start = (screen_width - button_start_width) // 2
y_button_start = ((screen_height - button_start_height) // 2) - 50

button_options_width = 400
button_options_height = 100
x_button_options = (screen_width - button_options_width) // 2
y_button_options = ((screen_height - button_options_height) // 2) + 75

button_quit_width = 400
button_quit_height = 100
x_button_quit = (screen_width - button_quit_width) // 2
y_button_quit = ((screen_height - button_quit_height) // 2) + 200

button_start = Button(x_button_start, y_button_start, button_start_width, button_start_height, "Start - AI", (125, 0, 150), (255, 255, 255), 60)
# button_options = Button(x_button_options, y_button_options, button_options_width, button_options_height, "Options", (0, 80, 255), (255, 255, 255), 60)
button_quit = Button(x_button_quit, y_button_quit, button_quit_width, button_quit_height, "Quit", (255, 40, 100), (255, 255, 255), 60)

# Variáveis para o menu de opções
button_controls_width = 400
button_controls_height = 100
x_button_controls = (screen_width - button_controls_width) // 2
y_button_controls = ((screen_height - button_controls_height) // 2) - 50

button_credits_width = 400
button_credits_height = 100
x_button_credits = (screen_width - button_credits_width) // 2
y_button_credits = ((screen_height - button_credits_height) // 2) + 75

button_return_width = 400
button_return_height = 100
x_button_return = (screen_width - button_return_width) // 2
y_button_return = ((screen_height - button_return_height) // 2) + 200

#button_controls = Button(x_button_controls, y_button_controls, button_controls_width, button_controls_height, "Controls", (0, 80, 255), (0, 0, 0), 60)
#button_credits = Button(x_button_credits, y_button_credits, button_credits_width, button_credits_height, "Credits", (0, 80, 255), (255, 255, 255), 60)
#button_return = Button(x_button_return, y_button_return, button_return_width, button_return_height, "Return", (0, 80, 255), (255, 255, 255), 60)






def main_menu_loop(screen):
    draw_main_menu(screen)
    #checkbox = CheckBox(50,screen_height-200,100,100,(255,255,255),(0,255,0),(255,0,0),10)
    #checkbox.draw(screen)
    current_state = GameState.MAIN_MENU
    #Reaproveitado do botao opcoes
    button_start.draw(screen)
    button_play_human = Button((screen_width - button_options_width) // 2, y_button_options, 400, 100, "Start - Human", (0, 80, 255), (255, 255, 255), 60)
    button_play_human.draw(screen)
    button_quit.draw(screen)
    """
    left_arrow = ClickableArrow(screen,100,100,50,50,"left")
    left_arrow.draw()
    right_arrow = ClickableArrow(screen,100,200,50,50,"right")
    right_arrow.draw()
    down_arrow = ClickableArrow(screen,100,300,50,50,"down")
    down_arrow.draw()
    up_arrow = ClickableArrow(screen,100,400,50,50,"up")
    up_arrow.draw()
    """
    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_start.is_clicked(pygame.mouse.get_pos()):
                    current_state = GameState.PLAYING
                #elif checkbox.is_clicked(screen,pygame.mouse.get_pos()):
                    #print("yes")
                    """if current_state == GameState.PLAYING:
                        # Lógica do jogo
                        # Você pode usar level_1["initial_state"] e level_1["objective_state"] para configurar o estado inicial e objetivo do nível

                        # Exemplo:
                        current_level: Dict[str, List[List[str]]] = beginner_1  # Escolha o nível atual
                        initial_state = current_level["initial_state"]
                        objective_state = current_level["objective_state"]
                        game = Game(initial_state, objective_state)
                        game.run(screen, screen_width, screen_height)"""

                #elif button_options.is_clicked(pygame.mouse.get_pos()):
                #    current_state = GameState.OPTIONS_MENU
                    # Adicione outros elementos do menu de opções conforme necessário
                    # Exemplo: Botões para ajustar configurações
                #elif left_arrow.is_clicked(pygame.mouse.get_pos()):
                #    print("yes")
                elif button_play_human.is_clicked(pygame.mouse.get_pos()):
                    level_menu_human_loop(screen)
                elif button_quit.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        if current_state == GameState.OPTIONS_MENU:
            options_menu(screen)

        elif current_state == GameState.CREDITS_SCREEN:
            draw_credits_screen(screen, screen_width)
            
        elif current_state == GameState.PLAYING:
            level_menu_loop(screen)

        """elif current_state == GameState.MAIN_MENU:
            draw_main_menu(screen)
            button_start.draw(screen)
            button_play_human.draw(screen)
            button_quit.draw(screen)"""
            # Voltar para o menu principal ao clicar na tela de créditos

        pygame.display.flip()
        fpsClock.tick(fps)

def level_human_loop(screen,level):
    draw_menu_settings(screen)
    write_on_text(screen,"Tip:",(255,255,255),100,200,100)
    checkbox = CheckBox(200,150,100,100,(255,255,255),(128,128,128),(0,0,0),10)
    checkbox.draw(screen)
    button_continue = Button(50,screen_height-150,300,100,"Continue!",(0,0,255),(255,255,255),50)
    button_continue.draw(screen)
    draw_board_initial(screen,level.board,200,200,800,100)
    draw_arrow(screen, (900, 350), (900, 450))
    draw_board_initial(screen, level.final_board, 200,200,800,500)
    pygame.display.flip()
    tip = False
    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if checkbox.is_clicked(screen,pygame.mouse.get_pos()):
                    if(tip): 
                        tip = False
                    else: 
                        tip = True
                    print("aqui")
                elif button_continue.is_clicked(pygame.mouse.get_pos()):
                    game_human_loop(screen,level,tip)
                    
        pygame.display.flip()
        fpsClock.tick(fps)

def clear_queue(queue):
    try:
        while True:
            queue.get_nowait()
    except Empty:
        pass  # Queue is empty

def seconds_to_MM_SS(seconds):
    # Convert seconds to minutes and seconds
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    
    # Format minutes and seconds as MM:SS
    time_str = "{:02d}:{:02d}".format(minutes, seconds)
    
    return time_str

def game_human_loop(screen,level,tip):
    draw_game_human_menu(screen)
    button_main = Button(0, screen_height-100, 200, 100, "Main Menu", (255, 0, 0), (255, 255, 255), 50)
    button_main.draw(screen)
    result_queue = Queue()
    draw_board_initial(screen,level.board,400,400,(screen_width/2)-200,(screen_height/2)-150)
    draw_board_initial(screen,level.final_board,100,100,screen_width-150,screen_height-150)
    write_on_text(screen,"Objective:",(255,255,255),screen_width-100,screen_height-180,35)
    up = [0]*len(level.board)
    down = [0]*len(level.board)
    left = [0]*len(level.board)
    right = [0]*len(level.board)
    unit = (400 / len(level.board))
    def run_concurrent(level,h2):
        print("b")
        result = a_star_search_limited_time(level,h2)
        result_queue.put(result)
    initial_x_horizontal = (screen_width/2)-200 + ((400 / len(level.board))/2)
    initial_y_vertical = (screen_height/2)-152 + ((400 / len(level.board))/2)
    for i in range(0,len(level.board)):
        up[i] = ClickableArrow(screen,initial_x_horizontal+ ((400 / len(level.board))*i),(screen_height/2)-210,unit-10,50,"up")
        up[i].draw()
    for i in range(0,len(level.board)):
        down[i] = ClickableArrow(screen,initial_x_horizontal+ ((400 / len(level.board))*i),(screen_height/2)+305,unit-10,50,"down")
        down[i].draw()
    for i in range(0,len(level.board)):
        left[i] = ClickableArrow(screen,(screen_width/2)-260,initial_y_vertical+ ((400 / len(level.board))*i),50,unit-10,"left")
        left[i].draw()
    for i in range(0,len(level.board)):
        right[i] = ClickableArrow(screen,(screen_width/2)+255,initial_y_vertical+ ((400 / len(level.board))*i),50,unit-10,"right")
        right[i].draw()
    if tip:
        write_on_text(screen,"Tip Board:",(255,255,255),screen_width-100,180,35)
    write_on_text(screen,"Step number:",(255,255,255),200,200,50)
    write_on_text(screen,"0",(255,255,255),350,200,65)
    write_on_text(screen,"Time:",(255,255,255),180,300,50)
    write_on_text(screen,seconds_to_MM_SS(0),(255,255,255),300,300,65)
    start = time.time()
    step = 0
    change = False
    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()   
                for i in range(0,len(level.board)):
                    if up[i].is_clicked(pos):
                        new_board = level.move(Direction.UP,Line.COLUMN,i)
                        old_board = level.board
                        level = Cogito(new_board,level.final_board,level.move_history)
                        draw_board_change(screen,old_board,new_board,400,400,(screen_width/2)-200,(screen_height/2)-150)
                        step += 1
                        change = True
                        pygame.draw.rect(screen,(0,0,0),(screen_width-150,200,100,100))
                        if tip:
                            threading.Thread(target=run_concurrent, args=(level,h2)).start()
                        pygame.draw.rect(screen,(0,0,0),(315,150,100,90))
                        write_on_text(screen,str(step),(255,255,255),355,200,65)
                    elif down[i].is_clicked(pos):
                        new_board = level.move(Direction.DOWN,Line.COLUMN,i)
                        old_board = level.board
                        level = Cogito(new_board,level.final_board,level.move_history)
                        draw_board_change(screen,old_board,new_board,400,400,(screen_width/2)-200,(screen_height/2)-150)
                        step += 1
                        change = True
                        if tip:
                            threading.Thread(target=run_concurrent, args=(level,h2)).start()
                        pygame.draw.rect(screen,(0,0,0),(screen_width-150,200,100,100))
                        pygame.draw.rect(screen,(0,0,0),(315,150,100,90))
                        write_on_text(screen,str(step),(255,255,255),355,200,65)
                    elif left[i].is_clicked(pos):
                        new_board = level.move(Direction.LEFT,Line.ROW,i)
                        old_board = level.board
                        level = Cogito(new_board,level.final_board,level.move_history)
                        draw_board_change(screen,old_board,new_board,400,400,(screen_width/2)-200,(screen_height/2)-150)
                        step += 1
                        if tip:
                            threading.Thread(target=run_concurrent, args=(level,h2)).start()
                        pygame.draw.rect(screen,(0,0,0),(screen_width-150,200,100,100))
                        pygame.draw.rect(screen,(0,0,0),(315,150,100,90))
                        write_on_text(screen,str(step),(255,255,255),355,200,65)
                        change = True
                    elif right[i].is_clicked(pos):
                        new_board = level.move(Direction.RIGHT,Line.ROW,i)
                        old_board = level.board
                        level = Cogito(new_board,level.final_board,level.move_history)
                        draw_board_change(screen,old_board,new_board,400,400,(screen_width/2)-200,(screen_height/2)-150)
                        step += 1
                        change = True
                        if tip:
                            threading.Thread(target=run_concurrent, args=(level,h2)).start()
                        pygame.draw.rect(screen,(0,0,0),(screen_width-150,200,100,100))
                        pygame.draw.rect(screen,(0,0,0),(315,150,100,90))
                        write_on_text(screen,str(step),(255,255,255),355,200,65)
                if button_main.is_clicked(pos):
                    main_menu_loop(screen)
        if change:
            if check_win(level.board,level.final_board):
                pygame.draw.rect(screen,(0,255,0),((screen_width/2)-400,(screen_height/2)-200,800,400))
                write_on_text(screen,"YOU WON!",(255,255,255),screen_width/2,screen_height/2,200)
                pygame.display.flip()
                time.sleep(3.0)
                main_menu_loop(screen)
            """else:
                if tip:
                    tip_calculate = True
        if tip_calculate:
            pool = multiprocessing.Pool()
            print("pqp")
            tip_calculate = False
            result = pool.apply_async(a_star_search_limited_time, args=(level,h2,))
            value = result.get()
            draw_board_initial(screen,value,100,100,screen_width-150,250)"""
        if not result_queue.empty():
            result = result_queue.get()
            resultinho = result[len(result)-1]
            draw_board_initial(screen,resultinho,100,100,screen_width-150,200)
            clear_queue(result_queue)
            pygame.display.flip()
            print("A")
        pygame.draw.rect(screen,(0,0,0),(230,270,140,70))
        write_on_text(screen,seconds_to_MM_SS(time.time()-start),(255,255,255),300,300,65)
        pygame.display.flip()
        fpsClock.tick(fps)
    


def level_menu_human_loop(screen):
    draw_level_select_menu(screen)
    min_y = 30 + 140
    min_x = 30 + ((screen_width-30-300)/4)
    x_increment = ((screen_width-30-300)/4)
    y_increment = (screen_height - min_y - 30-300)/4 
    x = min_x
    levels = [0]*9
    for i in range(0,3):
        if i == 0:
            write_on_text(screen,"Super Easy",(255,255,255),x+50,min_y-20,50)
            write_on_text(screen,"Easy",(255,255,255),x+50,min_y+150,50)
        elif i == 1:
            write_on_text(screen,"Medium",(255,255,255),x+50,min_y-20,50)
        elif i == 2:
            write_on_text(screen,"Hard",(255,255,255),x+50,min_y-20,50)
        y = min_y
        for j in range(1,4):
            levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
            levels[j+(i*3)-1].draw(screen)
            y+=y_increment+100
        x += x_increment+100
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if levels[0].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][0]["initial_state"],level_select["Beginner"][0]["objective_state"]))
                elif levels[1].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][1]["initial_state"],level_select["Beginner"][1]["objective_state"]))
                elif levels[2].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][2]["initial_state"],level_select["Beginner"][2]["objective_state"]))
                elif levels[3].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][0]["initial_state"],level_select["Amateur"][0]["objective_state"]))
                elif levels[4].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][1]["initial_state"],level_select["Amateur"][1]["objective_state"]))
                elif levels[5].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][2]["initial_state"],level_select["Amateur"][2]["objective_state"]))
                elif levels[6].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][0]["initial_state"],level_select["Expert"][0]["objective_state"]))
                elif levels[7].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][1]["initial_state"],level_select["Expert"][1]["objective_state"]))
                elif levels[8].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][2]["initial_state"],level_select["Expert"][2]["objective_state"]))
            """elif event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:

                ## TODO: NAO FUNCIONA, perguntar ao prof se deve suportar isto
                draw_level_select_menu(screen)
                print("hellyeah")
                screen_width_new, screen_height_new = screen.get_size()
                min_y = 30 + 140
                min_x = 30 + ((screen_width_new-30-300)/4)
                x_increment = ((screen_width_new-30-300)/4)
                y_increment = (screen_height_new - min_y - 30-300)/4 
                x = min_x
                for i in range(0,3):
                    y = min_y
                    for j in range(1,4):
                        levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
                        levels[j+(i*3)-1].draw(screen)
                        y+=y_increment+100
                    x += x_increment+100"""
        pygame.display.flip()
        fpsClock.tick(fps)

def options_menu(screen):
    draw_options_menu(screen)
    current_state = GameState.OPTIONS_MENU

    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                    current_state = GameState.CREDITS_SCREEN
            if current_state == GameState.CREDITS_SCREEN:
                draw_credits_screen(screen, screen_width)
def level_menu_loop(screen):
    draw_level_select_menu(screen)
    min_y = 30 + 140
    min_x = 30 + ((screen_width-30-300)/4)
    x_increment = ((screen_width-30-300)/4)
    y_increment = (screen_height - min_y - 30-300)/4 
    x = min_x
    levels = [0]*9
    for i in range(0,3):
        if i == 0:
            write_on_text(screen,"Super Easy",(255,255,255),x+50,min_y-20,50)
            write_on_text(screen,"Easy",(255,255,255),x+50,min_y+150,50)
        elif i == 1:
            write_on_text(screen,"Medium",(255,255,255),x+50,min_y-20,50)
        elif i == 2:
            write_on_text(screen,"Hard",(255,255,255),x+50,min_y-20,50)
        y = min_y
        for j in range(1,4):
            levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
            levels[j+(i*3)-1].draw(screen)
            y+=y_increment+100
        x += x_increment+100
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if levels[0].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][0]["initial_state"],level_select["Beginner"][0]["objective_state"]))
                elif levels[1].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][1]["initial_state"],level_select["Beginner"][1]["objective_state"]))
                elif levels[2].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][2]["initial_state"],level_select["Beginner"][2]["objective_state"]))
                elif levels[3].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][0]["initial_state"],level_select["Amateur"][0]["objective_state"]))
                elif levels[4].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][1]["initial_state"],level_select["Amateur"][1]["objective_state"]))
                elif levels[5].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][2]["initial_state"],level_select["Amateur"][2]["objective_state"]))
                elif levels[6].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][0]["initial_state"],level_select["Expert"][0]["objective_state"]))
                elif levels[7].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][1]["initial_state"],level_select["Expert"][1]["objective_state"]))
                elif levels[8].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][2]["initial_state"],level_select["Expert"][2]["objective_state"]))
            """elif event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:

                ## TODO: NAO FUNCIONA, perguntar ao prof se deve suportar isto
                draw_level_select_menu(screen)
                print("hellyeah")
                screen_width_new, screen_height_new = screen.get_size()
                min_y = 30 + 140
                min_x = 30 + ((screen_width_new-30-300)/4)
                x_increment = ((screen_width_new-30-300)/4)
                y_increment = (screen_height_new - min_y - 30-300)/4 
                x = min_x
                for i in range(0,3):
                    y = min_y
                    for j in range(1,4):
                        levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
                        levels[j+(i*3)-1].draw(screen)
                        y+=y_increment+100
                    x += x_increment+100"""
        pygame.display.flip()
        fpsClock.tick(fps)

def level_loop(screen,level):
    draw_level_menu(screen)
    button_bfs = Button(50, 200, 110, 100, "BFS", (125, 125, 125), (255, 255, 255), 80)
    button_bfs.draw(screen)
    button_ids = Button(50, 420, 400, 70, "Iterative Deepening Search", (125, 125, 125), (255, 255, 255), 40)
    button_ids.draw(screen)
    button_greedy = Button(50, 500, 320, 100, "Greedy Search", (125, 125, 125), (255, 255, 255), 60)
    button_greedy.draw(screen)
    button_a_star = Button(50, 610, 320, 100, "A* Search", (125, 125, 125), (255, 255, 255), 80)
    button_a_star.draw(screen)
    draw_board_initial(screen,level.board,200,200,800,100)
    draw_arrow(screen, (900, 350), (900, 450))
    draw_board_initial(screen, level.final_board, 200,200,800,500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_bfs.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,"BFS",level)
                elif button_ids.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,"IDS",level)
                elif button_greedy.is_clicked(pygame.mouse.get_pos()):
                    heuristic_choice_loop(screen,"GreedySearch",level)
                elif button_a_star.is_clicked(pygame.mouse.get_pos()):
                    heuristic_choice_loop(screen,"A_Star_Search",level)
        pygame.display.flip()
        fpsClock.tick(fps)
                
def calculating_loop(screen,algorithm,level,heuristic=""):
    draw_calculating_screen(screen)
    tracemalloc.start()
    start = 0
    end = 0
    if algorithm=="BFS":
        start_snapshot = tracemalloc.take_snapshot()
        start = time.time()
        goale = breadth_first_search(level,check_win,get_moves)
        end = time.time()
        goal = goale.state.move_history
        end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="IDS":
        start_snapshot = tracemalloc.take_snapshot()
        start = time.time()
        goale = iterative_deepening_search(level,check_win,get_moves)
        end = time.time()
        goal = goale.state.move_history
        end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="GreedySearch":
        if heuristic=="h1":
            start_snapshot = tracemalloc.take_snapshot()
            start = time.time()
            goal = greedy_search(level,h1)
            end = time.time()
            end_snapshot = tracemalloc.take_snapshot()
        elif heuristic=="h2":
            start_snapshot = tracemalloc.take_snapshot()
            start = time.time()
            goal = greedy_search(level,h2)
            end = time.time()
            end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="A_Star_Search":
        if heuristic=="h1":
            start_snapshot = tracemalloc.take_snapshot()
            start = time.time()
            goal = a_star_search(level,h1)
            end = time.time()
            end_snapshot = tracemalloc.take_snapshot()
        elif heuristic=="h2":
            start_snapshot = tracemalloc.take_snapshot()
            start = time.time()
            goal = a_star_search(level,h2)
            end = time.time()
            end_snapshot = tracemalloc.take_snapshot()
    time_total = end-start
    # Calculate the memory difference
    memory_diff = end_snapshot.compare_to(start_snapshot, 'filename')
    total_memory_usage = sum(stat.size for stat in memory_diff)
    total_memory_usage_kb = total_memory_usage/1024
    results_loop(screen,time_total,total_memory_usage_kb,goal)

def results_loop(screen,time_total,memory_total_kb,result):
    draw_results_menu(screen,time_total,memory_total_kb,result)
    button_main = Button((screen_width/3)-100, 500, 200, 100, "Main Menu", (255, 0, 0), (255, 255, 255), 50)
    button_main.draw(screen)
    button_step = Button(((screen_width/3)*2)-100, 500, 200, 100, "See Steps", (0, 255, 0), (255, 255, 255), 50)
    button_step.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_main.is_clicked(pygame.mouse.get_pos()):
                    main_menu_loop(screen)
                elif button_step.is_clicked(pygame.mouse.get_pos()):
                    steps_loop(screen,result)
        pygame.display.flip()
        fpsClock.tick(fps)

def steps_loop(screen,result):
    draw_steps_menu(screen)
    button_main = Button(0, screen_height-100, 200, 100, "Main Menu", (255, 0, 0), (255, 255, 255), 50)
    button_main.draw(screen)
    draw_board_initial(screen,result[0],400,400,(screen_width/2)-200,(screen_height/2)-150)
    write_on_text(screen,"Step number:",(255,255,255),screen_width/2-50,200,50)
    write_on_text(screen,"1",(255,255,255),screen_width/2+100,200,65)
    button_before = Button(screen_width/2 - 200, (screen_height/2)-150+420, 150, 80, "BEFORE", (0, 128, 128), (255, 255, 255), 50)
    button_before.draw(screen)
    button_next = Button(screen_width/2 + 50, (screen_height/2)-150+420, 150, 80, "NEXT", (54, 1, 63), (255, 255, 255), 50)
    button_next.draw(screen)
    pygame.display.flip()
    index = 0
    step_show = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_main.is_clicked(pygame.mouse.get_pos()):
                    main_menu_loop(screen)
                elif button_next.is_clicked(pygame.mouse.get_pos()) and index!=(len(result)-1):
                    draw_board_change(screen,result[index],result[index+1],400,400,(screen_width/2)-200,(screen_height/2)-150)
                    index += 1
                    step_show += 1
                    pygame.draw.rect(screen,(0,0,0),(screen_width/2+65,150,100,90))
                    write_on_text(screen,str(step_show),(255,255,255),screen_width/2+100,200,65)
                    pygame.display.flip()
                elif button_before.is_clicked(pygame.mouse.get_pos()) and index!=0:
                    draw_board_change(screen,result[index],result[index-1],400,400,(screen_width/2)-200,(screen_height/2)-150)
                    index -= 1
                    step_show -= 1
                    pygame.draw.rect(screen,(0,0,0),(screen_width/2+65,150,100,90))
                    write_on_text(screen,str(step_show),(255,255,255),screen_width/2+100,200,65)
                    pygame.display.flip()
                    #pygame.draw.rect(screen, (51, 153, 255), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))
        pygame.display.flip()
        fpsClock.tick(fps)
    #raw_arrow(screen, (900, 350), (900, 450))
    #draw_board_initial(screen, level.final_board, 200,200,800,500)

def heuristic_choice_loop(screen,algorithm,level):
    button_incorrect, button_manhattan = draw_heuristic_choice_screen(screen)
    heuristic_chosen = None

    while heuristic_chosen is None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_incorrect.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,algorithm,level,"h1")
                elif button_manhattan.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,algorithm,level,"h2")

        pygame.display.flip()
        fpsClock.tick(fps)




main_menu_loop(screen) 