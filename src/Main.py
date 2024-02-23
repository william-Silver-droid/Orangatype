import pygame
import random
import numpy as np
import time
import csv
import utils
print("here")
def main():
  print("made it to main ")
  pygame.init()
  white = (255, 255, 255)
  green = (0, 255, 0)
  blue = (0, 0, 128)
  
  SCREEN_WIDTH = 400
  SCREEN_HEIGHT = 400
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  text_font = pygame.font.SysFont("Arial", 30)
  print("right before run")
  run = True
  while run:

    screen.fill(white)
  
    draw_text("Hello, Orangutype", text_font, (0, 0, 0), 0, 0, screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    pygame.display.flip()
  
  pygame.quit()
  return 0

def draw_text(text, font, text_col, x, y, screen):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  
if __name__ == "__main__":
  main()
