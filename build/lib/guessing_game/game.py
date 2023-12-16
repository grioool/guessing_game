class GuessingGame:
    def __init__(self, filename):
        self.filename = filename
        self.questions_and_answers = self.load_questions()

    def load_questions(self):
        questions_and_answers = []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):  # Assuming each Q&A pair is followed by a blank line
                question = lines[i].strip()
                answer = lines[i + 1].strip()
                questions_and_answers.append((question, answer))
        return questions_and_answers

    def play_game(self):
        score = 0
        for question, answer in self.questions_and_answers:
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {answer}")
        print(f"Game Over! Your score was: {score}")

    @staticmethod
    def main():
        game = GuessingGame("questions/questions.txt")
        game.play_game()
