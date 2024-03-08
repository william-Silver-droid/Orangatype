import pygame
import random
import numpy as np
import time
import csv
import utils
import text_generator as tg
def main():
  pygame.init()
  white = (255, 255, 255)
  green = (0, 255, 0)
  blue = (0, 0, 128)
  black = (0,0,0)
  SCREEN_WIDTH = 10000
  SCREEN_HEIGHT = 10000
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  text_font = pygame.font.SysFont("Arial", 30)
  run = True
  seperator = ""
  words = tg.generator(words=0, n_words=0)
  words.load_words()
  words.generate_text()
  
  text = text_font.render(":", True, black)
  current_string = []
  screen.blit(text, (110, 110))
  screen.fill(white)
  while run:
    
    maybe = draw_text(words.type_words, text_font, (0, 0, 0), 0, 0, screen)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_BACKSPACE:
                current_string = current_string[:-1]
                screen.fill(white)
            else:
                try:
                  print(chr(event.key))
                  current_string.append(chr(event.key))
                except:
                   pass
            typed = text_font.render(seperator.join(current_string), True, black)
            print("typed", seperator.join(current_string))
            print("words", maybe)
            screen.blit(typed, (0, 100))
            print(seperator.join(current_string) == maybe[:-1])
            if seperator.join(current_string) == maybe[:-1]:
               print("here")
               pygame.QUIT
      if event.type == pygame.QUIT:
        run = False
    pygame.display.flip()
  
  pygame.quit()
  return 0

def draw_text(text, font, text_col, x, y, screen):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  return text

def text_input(prompt, font, screen, text_col):
    
    pygame.display.flip()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_BACKSPACE:
                current_string = current_string[:-1]
            else:
                current_string.append(chr(event.key))
            text = font.render(prompt + ''.join(current_string), True, text_col)
            screen.fill((255,255,255))
            screen.blit(text, (10, 10))
            pygame.display.flip()
    return ''.join(current_string)

if __name__ == "__main__":
  main()
