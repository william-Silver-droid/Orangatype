import pygame  # Importing the pygame library for game development
import random
import numpy as np
import time
import csv
import utils
import text_generator as tg  # Importing custom module text_generator as tg

def main():
    pygame.init()  # Initialize pygame

    # Color declarations
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    orange = (255, 165, 0)
    gray = (35, 35, 35)

    SCREEN_WIDTH = 10000
    SCREEN_HEIGHT = 10000

    # Setting up the display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_font = pygame.font.SysFont("Times New Roman", 30)
    run = True
    separator = ""  # Variable to hold separator for joining strings
    words = tg.generator(words=0, n_words=0)  # Creating an instance of text_generator
    words.load_words()  # Loading words
    words.generate_text()  # Generating text

    # Rendering text
    text = text_font.render(":", True, black)
    current_string = []  # List to hold user input string
    screen.blit(text, (110, 110))
    screen.fill(gray)  # Filling the screen with a gray background

    while run:
        # Drawing text on the screen
        maybe = draw_text(words.type_words, text_font, orange, 0, 0, screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break
                elif event.key == pygame.K_BACKSPACE:
                    current_string = current_string[:-1]  # Removing the last character from the string
                    screen.fill(white)  # Filling the screen with white color
                else:
                    try:
                        print(chr(event.key))
                        current_string.append(chr(event.key))  # Appending the character to the string
                    except:
                        pass
                typed = text_font.render(separator.join(current_string), True, black)  # Rendering typed text
                print("typed", separator.join(current_string))
                print("words", maybe)
                screen.blit(typed, (0, 100))
                print(separator.join(current_string) == maybe[:-1])
                user_typed = separator.join(current_string)
                if separator.join(current_string) == maybe[:-1]:  # Checking if typed text matches generated text
                    print("here")
                    pygame.quit()  # Quitting pygame
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()  # Updating the display

    pygame.quit()  # Quitting pygame
    return 0

def draw_text(text, font, text_col, x, y, screen):
    # Rendering text and drawing it on the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    return text

def text_input(prompt, font, screen, text_col):
    # Function for handling text input
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
            screen.fill((255, 255, 255))
            screen.blit(text, (10, 10))
            pygame.display.flip()
    return ''.join(current_string)

if __name__ == "__main__":
    main()  # Calling the main function if the script is executed directly
