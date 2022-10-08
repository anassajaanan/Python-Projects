#    dttaaa
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football "
             "pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you "
             "are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you "
             "are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than "
             "7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

#  class

class Question:
    def __init__(self, text,answer):
        self.text = text
        self.answer=answer

class QuizBrain:
    def __init__(self,list_q):
        self.list_of_questions=list_q
        self.number_of_question=0
        self.score=0
        self.guess=""

    def still_questions(self):

        while self.number_of_question < 12:
            return True
        return False

    def next_question(self):
        self.number_of_question+=1

        current_question=self.list_of_questions[self.number_of_question-1].text
        qq=(input(f"Q.{self.number_of_question} : {current_question} (True/False) : ")).title()
        self.guess=qq


    def cheak_answer(self):
        if self.guess==self.list_of_questions[self.number_of_question-1].answer:
            self.score+=1
            print(f"You are right , current score : {self.score}/{self.number_of_question}")
        else:
            print(f"You are wrong, current score : {self.score}/{self.number_of_question}")
            print(f"the correct answer is : {self.list_of_questions[self.number_of_question-1].answer}")
        print("\n")
    def final_score(self):
        print(f"Your final score is : {self.score}/{self.number_of_question}")


        # final code



from data import question_data
from question_model import Question,QuizBrain
question_bank=[]
for i in range(len(question_data)):
    question=Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question)
quiz_brain=QuizBrain(question_bank)
while quiz_brain.still_questions():
    quiz_brain.next_question()
    quiz_brain.cheak_answer()
quiz_brain.final_score()
