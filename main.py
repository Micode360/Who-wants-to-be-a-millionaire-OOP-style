import random
from path import intro_music
from store.quiz_data import data
from game_modules.music import Music
from utils.index import welcome_message
from game_modules.questions_list import Questions_list
from game_modules.millionare_game import MillionaireGame



def start_game():
    questions = Questions_list()
    run = MillionaireGame() 

    quiz = random.choice(data)
    
    for item in quiz:
        questions.add_question(item)

    run.start_game(questions.store) 

def exit_game():
    print("Exiting game. Goodbye!")
    exit()

def main():
    welcome_message()
    while True:
        print("\nOptions:")
        print("1. Start Game")
        print("2. Exit Game")

        music = Music()
        music.playMusic(intro_music)

        option = input("Enter your choice (1 or 2): ").strip()
        if option == "1":
            start_game()
        elif option == "2":
            exit_game()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
