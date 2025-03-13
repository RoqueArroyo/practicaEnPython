import pygame
import sys

def f(x, y):
    if y > 0.5:
        return 2 * x, 2 * y - 1
    elif x > 0.5:
        return 2 * x - 1, 2 * y
    else:
        return 2 * x, 2 * y

def main():
    numits = 20
    a, b, c, d = 0, 0, 1, 1
    M = 100
    R = 200
    screen_size = (500, 500)
    
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill((255, 255, 255))
    
    for p in range(1, M + 1):
        for q in range(1, M + 1):
            x = (a + (c - a) * p / M)
            y = (b + (d - b) * q / M)
            
            n = 1
            while n <= numits:
                x, y = f(x, y)
                
                if x * x + y * y > R:    
                    break
                
                n += 1

            if n <= numits:
                pygame.draw.rect(screen, (0, 0, 0), (int(500*x), int(500*y), 10, 10))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (int(500*x), int(500*y), 10, 10))
        
    pygame.display.flip()
    #"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    #"""
if __name__ == "__main__":
    main()