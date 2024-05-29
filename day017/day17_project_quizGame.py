from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Build question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# TODO: asking the question
quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")
