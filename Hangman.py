#!/usr/bin/env python 
# coding=utf-8

def game():
    import random 
    import logging

 
    print("Welcome to my game")

    logging.basicConfig(filename='text.log', level=logging.INFO,
                        format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

    logging.info('This is an info:')
    logging.error('This is an error:')

    logging.info('Reading file : start')
    my_file = open("/Users/tiphaineminguet/Desktop/Simplon/Package/Version2/word_list.txt", "r") 
    lines = my_file.readlines()
    list_word = [elem.strip() for elem in lines]
    logging.info('reading file : end')
    my_file.close()

    ###### Variables

    HANGMANPICS = ['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''','''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''','''
    +---+
    |   |
        |
        |
        |
        |
    =========''']

    Game_is_on = True

    lives = 5

    hidden_list = []

    logging.info('Choosing random word : start')
    random_word = list(random.choice(list_word))
    logging.info('Choosing random word : end')

    #print(random_word) #pour nous 
    #print(type(user_choice))  #pour nous

    ###### Remplacing letter by "_"
    logging.info('Transforming my list in underscore: start')
    def underscore(chosen_word, secret_list):
        for i in chosen_word :
            i = "_"
            secret_list.append(i)
        return secret_list

    underscore_word = underscore(random_word, hidden_list)
    print(" ".join(underscore_word))

    logging.info('Transforming my list in underscore: end')

    logging.info('Function game: start')
    def user_try(life, chosen_word, secret_list): 

        Game_is_on = True

        while Game_is_on:
            guess = input("Choose a letter: ").lower()
            
            for i in range(len(secret_list)):
                letter = chosen_word[i]
                if guess == letter: 
                    secret_list[i]= letter 
            print(secret_list)

            if secret_list.count("_") == 0:
                Game_is_on = False 
                print("You win")
        
            if guess not in chosen_word: 
                life -=1 
                print(life)
                print(HANGMANPICS[life])
                print("You lost a life, you have %s life remaining" %(life)) 

            if life == 0:
                Game_is_on = False
                print("You are dead.")    
                

    #mon user a des vies et il devine la bonne lettre: on remplace l'underscore en la lettre deviné 

    #mon user n'a plus de vie, le jeu s'arrete 

    #autre proposition: tant qu'il y a des underscore dans ma liste et que mes vies sont supérieuses à 0 
                
    user_try(lives, random_word, underscore_word)

    logging.info('Function game: end')
