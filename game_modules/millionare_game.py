import random
from game_modules.music import Music
from game_modules.evaluation import Evaluation
from path import winner_music, final_answer_music, lose_music, walk_away, question_music, tense_music, you_are_a_millionaire
from store.quiz_data import prize_unicode, success_remarks, failure_remarks, walk_away_remarks


# this class displays the question
class MillionaireGame:
    def __init__(self):
        self.score = 0

    def display_result(self, type, text): # will be in evaluation
        print("==" * 26)
        if type == "pass":
            print(random.choice(success_remarks))
        elif type == "walk_away":
            print(walk_away_remarks)
        else:
            print(random.choice(failure_remarks))
        
        print(text)
        print("==" * 26)
    
    def display_question(self, question):
        print(f"{question['question']}")
        for index, item in enumerate(question['options']):
            print(f"{index + 1}. {item}")
    
    def start_game(self, questionList):
        # Creating music object
        music = Music()

        # Creating evaluation object
        evaluation = Evaluation()        

        while self.score < len(questionList):
            if int(prize_unicode[self.score].replace("₦", "").replace(",", "")) < 100000:
                music.playMusic(question_music)    
            else: 
                music.playMusic(tense_music) 
                
            self.display_question(questionList[self.score])
            choice = input("Choose 1/2/3/4: ")

            music.playMusic(final_answer_music) if int(prize_unicode[self.score].replace("₦", "").replace(",", "")) >= 100000 else None
            confirm = input("Are you sure this is your final answer (y/n): ")
            

            if evaluation.evaluate_choice(choice, questionList[self.score]["answer"]) and confirm == 'y': 
                self.score += 1
                if self.score == len(questionList):
                     self.display_result(
                    "pass",
                    f"You have done it. You are a millionaire !!!"
                    )
                     music.playMusic(you_are_a_millionaire, 25)
                     break
                else:
                     self.display_result(
                        "pass",
                        f"You now have {prize_unicode[self.score - 1]}"
                    )
                music.playMusic(winner_music)
                option = input("Do you want to continue? (y/n): ").strip().lower()
                if option == 'y':
                    continue
                else:
                     self.display_result(
                    "walk_away",
                    f"You just walked away with {prize_unicode[self.score - 1] if self.score != 0 else '₦0'}"
                )
                music.playMusic(walk_away, 9)
                break 
            elif confirm == "n":
                print("Let me show you again")
            else:
                self.display_result(
                    "fail",
                    f"You just won {prize_unicode[self.score - 1] if self.score != 0 else '₦0'}"
                )
                music.playMusic(lose_music, 9)
                break
