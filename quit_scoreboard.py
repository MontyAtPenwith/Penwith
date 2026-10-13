total_score = 0
questions_answered = 0

def record_answer(points):
    global total_score, questions_answered
    total_score = total_score + points
    questions_answered += 1
    print("Recorded. Running score:", total_score)

def show_summary():
    print("Questions answered:", questions_answered)
    print("Show score:", total_score)

record_answer(5)
record_answer(3)
record_answer(5)
show_summary()