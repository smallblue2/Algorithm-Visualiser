import pygame
import random
pygame.display.set_caption("Algorithm Visualiser")

# GLOBAL VARIABLES
HEIGHT = 400
WIDTH = 1500
LIST = []
LIST_SIZE = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# DRAW FUNCTION
def draw():
    prev_width = 0
    WIN.fill((0, 0, 0))
    for height in LIST:
        element = pygame.Rect(prev_width, HEIGHT - height, (WIDTH / len(LIST)) - 1, height)
        prev_width += element.width + 1
        pygame.draw.rect(WIN, (255, 255, 255), element)
    pygame.display.update()

# FILL LIST FUNCTION
def fill_list():
    LIST.clear()
    i = 0
    while i < LIST_SIZE:
        n = random.randint(1, 400)
        LIST.append(n)
        i += 1

# SORT FUNCTION
def sort():
    # SELECTION SORT
    i = 0
    while i < len(LIST):
        p = i
        j = i + 1
        while j < len(LIST):
            if LIST[j] < LIST[p]:
                p = j
            j = j + 1
        tmp = LIST[p]
        LIST[p] = LIST[i]
        LIST[i] = tmp
        i += 1
        # DRAW SORT STEP
        draw()

# MAIN FUNCTION
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fill_list()
                    draw()
                if event.key == pygame.K_RETURN:
                    sort()

if __name__ == '__main__':
    main()