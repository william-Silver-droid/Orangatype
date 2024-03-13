def start_screen(text_font, color1, screen, color2, separator, num_words):
    question = draw_text("How many words do you want to type", text_font, color1, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen)
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
            screen.blit(typed, (SCREEN_WIDTH//2 - typed.get_width()//2, SCREEN_HEIGHT//2))
            print(separator.join(num_words) == question[:-1])
            user_typed = separator.join(num_words)
            if separator.join(num_words) == question[:-1]:  # Checking if typed text matches generated text
                print("here")
                pygame.quit()  # Quitting pygame
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()  # Updating the display
