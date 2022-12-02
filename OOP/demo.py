class Question:
    def __init__(self,text,choices,answer):
       self.text=text
       self.choices=choices
       self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("javascript"))

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQustion(self):
        return quiz.questions[quiz.questionIndex]
    def displayQuestion(self):
        question=self.getQustion()
        print(f"Soru {self.questionIndex+1} : {question.text}")

        for q in question.choices:
            print('-'+q)
        answer=input("cevap: ")
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question=self.getQustion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
            
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        print(self.score)
    def displayProgress(self):
        
q1=Question("en iyi programlama dili hangisidir",["C#","Python","Javascript"],"python")
q2=Question("en popüler programlama dili hangisidir",["C#","Python","Javascript"],"javascript")

questions=[q1,q2]


quiz=Quiz(questions)

quiz.displayQuestion()