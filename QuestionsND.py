class Questions():
                            
    def __init__(self, question, correct_answer,answer_choices):
        self.question = question
        self.correct_answer = correct_answer
        self.answer_choices = answer_choices
    def __str__(self):
        choice1 = self.answer_choices[0]
        choice2 = self.answer_choices[1]
        choice3 = self.answer_choices[2]
        choice4 = self.answer_choices[3]
        return (self.question + "\n" +
                "1. " + choice1 + "\n"
                "2. " + choice2 + "\n"
                "3. " + choice3 + "\n"
                "4. " + choice4 + "\n")

    def get_answer(self,answer):
        if answer == self.correct_answer:
            return True
        else:
            return False
    def answer(self):
        return self.correct_answer
    
    
