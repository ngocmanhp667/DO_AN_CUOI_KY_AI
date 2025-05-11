import pygame
import sys
import subprocess

pygame.init()
music_path = "D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Music/nenstart.mp3"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("WELCOME THE MAZE GAME")
pygame.mixer.music.load(music_path)
pygame.mixer.music.play()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

start_button = pygame.Rect(300, 300, 200, 50)

def draw_start_screen():
    background = pygame.image.load("D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Picture/wellcome.jpg").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    screen.blit(background, (0, 0))
    
    text = font.render("Welcome to the maze game", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)
    
    pygame.draw.rect(screen, BLACK, start_button)
    start_text = font.render("START", True, WHITE)
    start_text_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()

def main_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        pygame.display.flip()

def main():
    running = True
    game_started = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main_py_path = r"D:/DO_An_CUOI_KY_AI/DO_AN_CUOI_KY_AI/src/Code/Main.py"
                    subprocess.Popen(["python", "-u", main_py_path])
                    pygame.quit()
                    sys.exit()

        draw_start_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
