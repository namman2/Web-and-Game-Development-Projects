import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)
brown = (88,44,12)
bg = pygame.image.load('lavacave.jpg')

pygame.init()

surfaceWidth = 1024
surfaceHeight = 768

imageWidth = 75
imageHeight = 48

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Floppy Charizard')
clock = pygame.time.Clock()

img = pygame.image.load('charizard.gif')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text,(0,0))

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, brown, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, brown, [x_block,y_block+block_height+gap,block_width, surfaceHeight])

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        
        return event.key
    
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)
    
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue!', smallText)
    typTextRect.center = surfaceWidth/2, ((surfaceHeight/2)+50)
    surface.blit(typTextSurf, typTextRect)
    
    pygame.display.update()
    time.sleep(1)
    
    while replay_or_quit() == None:
        clock.tick()
        
    main()
        
def gameOver():
    msgSurface('Kaboom! Charizard is out of Flames!')

def charizard(x, y, image):
    surface.blit(img, (x,y))
    
def main():
    x = 50
    y = 200
    y_move = 5
    
    x_block = surfaceWidth
    y_block = 0
    
    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = imageHeight*3
    block_move = 8
    
    current_score = 0
    
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 7
                    
        y += y_move
                
        surface.blit(bg, (0,0))
        charizard(x, y, img)
        score(current_score)
        
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move
        
        if y > surfaceHeight-48 or y < 0:
            gameOver()
        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
        
        if x + imageWidth > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - imageWidth < block_width + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_height+gap:
                if x < block_width + x_block:
                    gameOver()

        if x < x_block and x > x_block - block_move:
            current_score += 1
        
        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()