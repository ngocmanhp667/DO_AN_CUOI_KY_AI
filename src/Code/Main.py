import pygame
from Maze import Maze
from pygame.locals import *
from queue import PriorityQueue
import time
from ControlPanel import ControlPanel
from AI import AI

def main():
    pygame.init()  
    width, height = 1000, 500 
    screen = pygame.display.set_mode((width, height))  
    pygame.mixer.init() 
    pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3") 
    pygame.mixer.music.set_volume(0.5)  
    music_start_time = None 
    control_panel = ControlPanel(300, 500) 
    maze = Maze(35, 25) 
    ai = AI(maze)
    auto_play = False 
    shortest_path = None  
    ai.maze = maze  
    start_time = None 
    countdown_time = 59 
    running = True 
    show_ai_menu = False       
    selected_algorithm = None  
    game_over = False 
    game_over_time = None 
    maze_completed = False 
    congrats_display_time = None 
    game_over_display_time = None 

    while running:
        current_time = pygame.time.get_ticks()
        if ai.x == maze.end_x and ai.y == maze.end_y:
            maze_completed = True
        for event in pygame.event.get():
            if selected_algorithm:
                if selected_algorithm == "SA":
                    from Algorithms import simulated_annealing
                    shortest_path = simulated_annealing(maze)
                    print("SA path:", shortest_path)

                elif selected_algorithm == "NO_OBS":
                    from Algorithms import searching_with_no_observation
                    shortest_path = searching_with_no_observation(maze)

                elif selected_algorithm == "CSP":
                    from Algorithms import solve_with_csp
                    shortest_path = solve_with_csp(maze)

                elif selected_algorithm == "DQN":
                    from Algorithms import run_dqn_agent
                    shortest_path = run_dqn_agent(maze)

                elif selected_algorithm == "A*":
                    from Algorithms import astar
                    shortest_path = astar(maze)

                elif selected_algorithm == "BFS":
                    from Algorithms import bfs
                    shortest_path = bfs(maze)

                auto_play = True
                start_time = time.time()
                pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
                pygame.mixer.music.play()
                selected_algorithm = None 

            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if show_ai_menu:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    center_x = (width - 200) // 2  
                    if center_x <= mouse_x <= center_x + 200:
                        if 140 <= mouse_y <= 180:
                            selected_algorithm = "SA"
                            show_ai_menu = False
                        elif 190 <= mouse_y <= 230:
                            selected_algorithm = "BELIEF"
                            show_ai_menu = False
                        elif 240 <= mouse_y <= 280:
                            selected_algorithm = "CSP"
                            show_ai_menu = False
                        elif 290 <= mouse_y <= 330:
                            selected_algorithm = "DQN"
                            show_ai_menu = False
                        elif 340 <= mouse_y <= 380:
                            selected_algorithm = "A*"
                            show_ai_menu = False
                        elif 390 <= mouse_y <= 430:
                            selected_algorithm = "BFS"
                            show_ai_menu = False
                maze, ai = control_panel.handle_event(event, maze, ai) 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 750 <= mouse_x <= 950 and 50 <= mouse_y <= 100:
                    auto_play = True
                    start_time = time.time()
                    pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")  
                    pygame.mixer.music.play() 
                elif 750 <= mouse_x <= 950 and 150 <= mouse_y <= 200:
                    show_ai_menu = True
                    auto_play = False
                    control_panel.reset_icon_position(ai)
                    start_time = time.time()
                    pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3") 
                    pygame.mixer.music.play() 
                elif 750 <= mouse_x <= 950 and 250 <= mouse_y <= 300:
                    maze = Maze(35, 25)
                    ai = AI(maze) 
                    auto_play = False
                    shortest_path = None
                    start_time = None  
                    game_over = False 
                    game_over_time = None  
                    pygame.mixer.music.stop()
                elif 750 <= mouse_x <= 950 and 350 <= mouse_y <= 400:
                    running = False


            elif event.type == KEYDOWN and auto_play:
                if not game_over:
                    if event.key == K_UP:
                        ai.move_towards(ai.x, ai.y - 1)
                    elif event.key == K_DOWN:
                        ai.move_towards(ai.x, ai.y + 1)
                    elif event.key == K_LEFT:
                        ai.move_towards(ai.x - 1, ai.y)
                    elif event.key == K_RIGHT:
                        ai.move_towards(ai.x + 1, ai.y)
            
            if ai.x == maze.end_x and ai.y == maze.end_y:
                if not game_over:
                    game_over_time = time.time() 
                    game_over = True 
                    total_time = game_over_time - start_time  
                    start_time = None

                    pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/dendich.mp3")
                    pygame.mixer.music.play()

                    congrats_display_time = pygame.time.get_ticks()
                

        screen.fill((0, 0, 0))
        maze.display_maze(screen, ai)
        control_panel.display(screen)

        if auto_play:
            if shortest_path and len(shortest_path) > 0:
                next_step = shortest_path.pop(0)  
                ai.move_towards(next_step[0], next_step[1])
            player_image = pygame.image.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Picture/icon.png")
            cell_size = 20
            player_image = pygame.transform.scale(player_image, (cell_size, cell_size))
            screen.blit(player_image, (ai.x * cell_size, ai.y * cell_size))

        rewards_to_remove = [] 
        play_reward_music = False 

        for reward in maze.rewards:
            if (ai.x, ai.y) == reward:
                start_time += 3  
                rewards_to_remove.append(reward)  
                play_reward_music = True 

        for reward in rewards_to_remove:
            maze.rewards.remove(reward)
        
        if play_reward_music:
            pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/trungthuong.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            pygame.mixer.music.queue("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
            
        if start_time is not None and not game_over:
            elapsed_time = countdown_time - int(time.time() - start_time) 
            elapsed_time = max(0, elapsed_time)

            font = pygame.font.Font(None, 36)
            time_text = font.render(f"TIME: {elapsed_time} S", True, (0, 0, 0))
            text_rect = time_text.get_rect()
            text_rect.topright = (width - 100, 10)  
            screen.blit(time_text, text_rect)

            if elapsed_time == 0 and not maze_completed:
                game_over = True
                game_over_time = time.time() 
                game_over_display_time = pygame.time.get_ticks()

                pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/gameover.mp3")
                pygame.mixer.music.play()
                
        if congrats_display_time is not None:
            elapsed_congrats_time = current_time - congrats_display_time
            if elapsed_congrats_time < 3000: 
                pygame.draw.rect(screen, (0, 0, 0), (width // 2 - 150, height // 2 - 50, 300, 100)) 
                font = pygame.font.Font(None, 48)  
                congrats_text = font.render("Congratulations!", True, (255, 255, 255)) 
                text_rect = congrats_text.get_rect(center=(width // 2, height // 2))
                screen.blit(congrats_text, text_rect)
            else:
                congrats_display_time = None 

        if game_over_display_time is not None:
            elapsed_game_over_time = current_time - game_over_display_time
            if elapsed_game_over_time < 3000:  
                pygame.draw.rect(screen, (0, 0, 0), (width // 2 - 150, height // 2 - 50, 300, 100)) 
                font = pygame.font.Font(None, 48) 
                game_over_text = font.render("Game Over!", True, (255, 255, 255))
                text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
                screen.blit(game_over_text, text_rect)
            else:
                game_over_display_time = None 
        if show_ai_menu:
            button_color = (0, 191, 255)
            font = pygame.font.SysFont(None, 24)
            button_width = 200
            button_height = 40
            center_x = (width - button_width) // 2 

            algorithms = [
                ("Simulated Annealing", "SA", 140),
                ("No Observation", "NO_OBS", 190),
                ("CSP Solver", "CSP", 240),
                ("Deep Q-Network", "DQN", 290),
                ("A*", "A*", 340),
                ("BFS", "BFS", 390)
            ]

            for label, algo_key, y_pos in algorithms:
                pygame.draw.rect(screen, button_color, (center_x, y_pos, button_width, button_height))
                pygame.draw.rect(screen, (255, 255, 255), (center_x, y_pos, button_width, button_height), 2)  # viền trắng

                text_surface = font.render(label, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(center_x + button_width // 2, y_pos + button_height // 2))
                screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()