import pygame
from Maze import Maze
from pygame.locals import *
from queue import PriorityQueue
import time
from ControlPanel import ControlPanel
from AI import AI

def save_statistics(algo_stats):
    with open("algorithm_statistics.txt", "w") as f:
        f.write("Algorithm Statistics:\n")
        for algo, result in algo_stats.items():
            f.write(f"{algo}: {result}\n")

def main():
    pygame.init()
    width, height = 1200, 500
    screen = pygame.display.set_mode((width, height))
    pygame.mixer.init()
    pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
    pygame.mixer.music.set_volume(0.5)

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
    show_stats = False
    selected_algorithm = None
    game_over = False
    maze_completed = False
    congrats_display_time = None
    game_over_display_time = None

    algo_stats = {
        "SA": "It hasn't run yet",
        "NO_OBS": "It hasn't run yet",
        "CSP": "It hasn't run yet",
        "DQN": "It hasn't run yet",
        "A*": "It hasn't run yet",
        "BFS": "It hasn't run yet"
    }

    while running:
        current_time = pygame.time.get_ticks()
        if ai.x == maze.end_x and ai.y == maze.end_y:
            maze_completed = True

        for event in pygame.event.get():
            if selected_algorithm:
                from Algorithms import simulated_annealing, searching_with_no_observation, solve_with_csp, run_dqn_agent, astar, bfs
                if selected_algorithm == "SA":
                    shortest_path = simulated_annealing(maze)
                elif selected_algorithm == "NO_OBS":
                    shortest_path = searching_with_no_observation(maze)
                elif selected_algorithm == "CSP":
                    shortest_path = solve_with_csp(maze)
                elif selected_algorithm == "DQN":
                    shortest_path = run_dqn_agent(maze)
                elif selected_algorithm == "A*":
                    shortest_path = astar(maze)
                elif selected_algorithm == "BFS":
                    shortest_path = bfs(maze)

                if shortest_path:
                    algo_stats[selected_algorithm] = f"{len(shortest_path)} steps"
                    save_statistics(algo_stats)

                auto_play = True
                start_time = time.time()
                pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
                pygame.mixer.music.play()
                selected_algorithm = None
                show_ai_menu = False

            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if show_ai_menu:
                    cx = (width - 200) // 2
                    algo_map = [("SA", 140), ("NO_OBS", 190), ("CSP", 240), ("DQN", 290), ("A*", 340), ("BFS", 390)]
                    for key, y in algo_map:
                        if cx <= mx <= cx + 200 and y <= my <= y + 40:
                            selected_algorithm = key

                maze, ai = control_panel.handle_event(event, maze, ai)

                if 750 <= mx <= 950:
                    if 50 <= my <= 100:
                        auto_play = True
                        start_time = time.time()
                        pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
                        pygame.mixer.music.play()
                        show_ai_menu = False
                    elif 150 <= my <= 200:
                        show_ai_menu = True
                        auto_play = False
                        control_panel.reset_icon_position(ai)
                        start_time = time.time()
                        pygame.mixer.music.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nhac.mp3")
                        pygame.mixer.music.play()
                    elif 250 <= my <= 300:
                        maze = Maze(35, 25)
                        ai = AI(maze)
                        auto_play = False
                        shortest_path = None
                        start_time = None
                        game_over = False
                        game_over_time = None
                        pygame.mixer.music.stop()
                        for k in algo_stats:
                            algo_stats[k] = "It hasn't run yet"
                        save_statistics(algo_stats)
                    elif 350 <= my <= 400:
                        running = False
                    elif 450 <= my <= 500:
                        shortest_path = None
                        auto_play = False
                        maze.path.clear()
                        ai.path.clear()
                        ai.x = maze.start_x
                        ai.y = maze.start_y

                elif 1000 <= mx <= 1180 and 50 <= my <= 90:
                    show_stats = not show_stats

        screen.fill((0, 0, 0))
        maze.display_maze(screen, ai)
        control_panel.display(screen)

        if auto_play and shortest_path:
            if len(shortest_path) > 0:
                nx, ny = shortest_path.pop(0)
                ai.move_towards(nx, ny)
                icon = pygame.image.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Picture/icon.png")
                icon = pygame.transform.scale(icon, (20, 20))
                screen.blit(icon, (ai.x * 20, ai.y * 20))

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
                pygame.draw.rect(screen, (255, 255, 255), (center_x, y_pos, button_width, button_height), 2)
                text_surface = font.render(label, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(center_x + button_width // 2, y_pos + button_height // 2))
                screen.blit(text_surface, text_rect)

        if show_stats:
            pygame.draw.rect(screen, (20, 20, 20), (1000, 100, 180, 250))
            font = pygame.font.SysFont(None, 22)
            labels = ["SA", "NO_OBS", "CSP", "DQN", "A*", "BFS"]
            for i, k in enumerate(labels):
                txt = font.render(f"{k}: {algo_stats[k]}", True, (255, 255, 255))
                screen.blit(txt, (1010, 110 + i * 35))

        # Restore Remove Path button
        pygame.draw.rect(screen, (255, 69, 0), (750, 450, 200, 50))
        font = pygame.font.SysFont(None, 28)
        text = font.render("Remove Path", True, (255, 255, 255))
        text_rect = text.get_rect(center=(850, 475))
        screen.blit(text, text_rect)

        # Collect Stats button
        pygame.draw.rect(screen, (0, 160, 240), (1000, 50, 180, 40))
        font = pygame.font.SysFont(None, 24)
        label = font.render("Collect Statistics", True, (255, 255, 255))
        screen.blit(label, (1010 + (180 - label.get_width()) // 2, 60))

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()