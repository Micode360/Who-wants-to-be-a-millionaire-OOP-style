class Evaluation:
    def __init__(self) -> None:
        pass

    def evaluate_choice(self, choice, correct_answer):
        return choice == correct_answer
    
    def prompt_continue(self):
        option = input("Do you want to continue? (y/n): ").strip().lower()
        return option == 'y'
