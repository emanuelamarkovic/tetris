import pygame,  sys

pygame.init()
screen = pygame.display.set_mode((200, 400))
tetrominos = [
    [(1, 5), (0, 4), (0, 5), (0, 6)],
    [(1, 5), (0, 5), (0, 6), (1, 6)],
    [(1, 4), (0, 4), (0, 5), (0, 6)],
    [(1, 6), (0, 4), (0, 5), (0, 6)],
    [(1, 5), (0, 4), (0, 5), (1, 6)],
    [(1, 5), (0, 5), (0, 6), (1, 4)],
    [(0, 4), (0, 5), (1, 5), (1, 6)]
]
grid = [[0] * 20 for _ in range(10)]
tetrimoni_color =(255, 255, 255)
current_tetromino = tetrominos[1]
movementr_vector =[0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movementr_vector = [0, -1]
            if event.key == pygame.K_RIGHT:
                movementr_vector = [0, 1]
        else: movementr_vector = [1, 0]
    
    screen.fill(pygame.Color("black"))
    for i in range(4):
        pygame.draw.rect(screen, tetrimoni_color, (current_tetromino[i][1] * 20, current_tetromino[i][0] * 20, 20, 20))
        pygame.display.flip()
    pygame.time.delay(100)