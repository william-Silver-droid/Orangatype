import pygame  # Importing the pygame library for game development
import time
import matplotlib.pyplot as plt
import text_generator as tg  # Importing custom module text_generator as tg

def main():
    global accuracies
    global wpms
    global times


    pygame.init()  # Initialize pygame
    # Color declarations
    while True:
        accuracies = []
        wpms = []
        times = []
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        black = (0, 0, 0)
        orange = (255, 165, 0)
        gray = (35, 35, 35)

        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 1000
        clock = pygame.time.Clock()
        # Setting up the display screen
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        text_font = pygame.font.SysFont("Times New Roman", 30)
        run = True
        separator = ""  # Variable to hold separator for joining strings
        words = tg.generator(words=0, n_words=0, n=0)  # Creating an instance of text_generator
        words.load_words()  # Loading words
        words.generate_text()  # Generating text

        # Rendering text
        text = text_font.render(":", True, orange)
        current_string = []  # List to hold user input string
        screen.blit(text, (110, 110))
        screen.fill(gray)  # Filling the screen with a gray background
        num_words = []
        starting = True
        start_time = None
        wpm = 0
        accuracy = 0
        start_time = 0

        while run:
            # Drawing text on the screen
            if not starting:
                wpm, accuracy, etime, current_string, run, start_time = main_screen(words, text_font, orange, gray, start_time, SCREEN_WIDTH, SCREEN_HEIGHT, screen, separator, current_string, wpm, accuracy)
                accuracies.append(accuracy)
                wpms.append(wpm)
                times.append(etime)
                pygame.display.flip()  # Updating the display
            else:
                start = start_screen(text_font, orange, screen, gray, separator, num_words)
                if start:
                    words, starting = start
            clock.tick(60)
      # Quitting pygame
        print(wpms)
        w = wpms[0]
        counter = 0
        while w == 0:
            w = wpms[counter]
            counter += 1
        print(counter)
        accuracies = accuracies[counter+10:]
        times = times[counter+10:]
        wpms = wpms[counter+10:]
        plt.figure(figsize=(8, 6))
        plt.plot(times, wpms, label='Words per minute')
        plt.plot(times, accuracies, label='Accuracies')

        # Adding labels and title
        plt.xlabel('Time')
        plt.ylabel('Words or %')
        plt.title('Accuracy and WPM with respect to time')
        plt.legend()
        plt.savefig('graph.png')
        graph_image = pygame.image.load('graph.png')
        while not run:
            run = end_screen(screen, graph_image)
def end_screen(screen, graph_image):
    run = False
    button_rect = pygame.Rect(300, 700, 100, 50)  # Button position and dimensions
    button_color = (0, 255, 0)  # Green color for the button
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click
            if button_rect.collidepoint(event.pos):  # Check if the click is inside the button
                run = True

    # Draw the graph image onto the screen
    screen.fill((255, 255, 255))
    screen.blit(graph_image, (0, 0))
    
    # Draw the button with the "restart" text
    font = pygame.font.Font(None, 36)
    text = font.render("Restart", True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    return run



def main_screen(words, text_font, color1, color2, start_time, SCREEN_WIDTH, SCREEN_HEIGHT, screen, separator, current_string, wpm, accuracy):
    user_typed= separator.join(current_string)
    run = True
    if wpm == 0:
        start_time = time.time()
    screen.fill((35, 35, 35))
    key = draw_text(words.type_words.lower(), text_font, color1, 0, SCREEN_WIDTH // 4, screen)
    typed = text_font.render(separator.join(current_string), True, color1)  # Rendering typed text
    screen.blit(typed, (0, SCREEN_WIDTH // 3.5))
    display_circle_numbers(wpm, accuracy, color1, SCREEN_WIDTH, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                run = False
            elif event.key == pygame.K_BACKSPACE:
                current_string = current_string[:-1]  # Removing the last character from the string
                screen.fill(color2)  # Filling the screen with white color
            else:
                try:
                    current_string.append(chr(event.key))
                except:
                    pass

            user_typed = separator.join(current_string)
            accuracy = calculate_accuracy(user_typed, key)

            display_circle_numbers(wpm, accuracy, color1, SCREEN_WIDTH, screen)
            if user_typed == key[:-1]:  # Checking if typed text matches generated text
                run = False  # Quitting pygame
    elapsed_time = time.time() - start_time
    wpm = calculate_wpm(user_typed, elapsed_time)
    return wpm, accuracy, elapsed_time, current_string, run, start_time



def draw_text(text, font, text_col, x, y, screen):
    # Rendering text and drawing it on the screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    return text

def start_screen(text_font, color1, screen, color2, separator, num_words):
    question = draw_text("How many words do you want to type", text_font, color1, 0, 0, screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(color2)
                try:
                    starting = False
                    n = num_words
                    words = tg.generator(words=0, n_words=0,
                                         n=int(separator.join(n)))  # Creating an instance of text_generator
                    words.load_words()  # Loading words
                    words.generate_text()
                    num_words = ""
                    return words, starting
                except:
                    pass
            elif event.key == pygame.K_BACKSPACE:
                num_words = num_words[:-1]  # Removing the last character from the string
                screen.fill(color2)  # Filling the screen with white color
            else:
                try:
                    print(chr(event.key))
                    num_words.append(chr(event.key))  # Appending the character to the string
                except:
                    pass
            typed = text_font.render(separator.join(num_words), True, color1)  # Rendering typed text
            screen.blit(typed, (0, 100))
            print(separator.join(num_words) == question[:-1])
            user_typed = separator.join(num_words)
            if separator.join(num_words) == question[:-1]:  # Checking if typed text matches generated text
                print("here")
                pygame.quit()  # Quitting pygame
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()  # Updating the display

def calculate_accuracy(typed_text, correct_text):
    # Calculate the accuracy based on the number of correct characters up to the current point
    total_correct_characters = sum(1 for a, b in zip(typed_text, correct_text[:len(typed_text)]) if a == b)
    total_characters = len(typed_text)
    accuracy = (total_correct_characters / total_characters) * 100 if total_characters > 0 else 0

    return accuracy

def calculate_wpm(typed_text, elapsed_time):
    # Calculate the total number of characters typed
    total_characters = len(typed_text)

    # Calculate the WPM
    wpm = (total_characters / 5) / (elapsed_time / 60) if elapsed_time > 0 else 0

    return wpm


def display_circle_numbers(left_number, right_number, color1, SCREEN_WIDTH, screen): #left = wpm righht= accuracy
    # Clear the screen

    # Draw circles
    circle_radius = 50
    circle_padding = 20
    circle_y = circle_radius + circle_padding
    circle_left_x = circle_radius + circle_padding
    circle_right_x = SCREEN_WIDTH - circle_radius - circle_padding
    pygame.draw.circle(screen, color1, (circle_left_x, circle_y), circle_radius)
    pygame.draw.circle(screen, color1, (circle_right_x, circle_y), circle_radius)
    # Render text
    font = pygame.font.Font(None, 36)
    text_left = font.render(str(left_number)[:4], True, (0, 0, 0))
    text_right = font.render(str(right_number)[:4], True, (0, 0, 0))

    text_left_rect = text_left.get_rect(center=(circle_left_x, circle_y))
    text_right_rect = text_right.get_rect(center=(circle_right_x, circle_y))
    screen.blit(text_left, text_left_rect)
    screen.blit(text_right, text_right_rect)

if __name__ == "__main__":
    main()  # Calling the main function if the script is executed directly
