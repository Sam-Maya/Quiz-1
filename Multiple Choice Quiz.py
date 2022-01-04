from Question_Class import question

question_prompts = [
    "What color is the sky? \n(a) Red\n(b) Blue\n(c) Violet\n\n",
    "Who is Queen ELizabeth? \n(a) An engineer\n(b) A comedian\n(c) A queen\n\n",
    "How much is a nickle worth? \n(a) .01\n(b) .05\n(c) .25\n\n"
]

questions = [
    question(question_prompts[0], "b"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(question_prompts)) + " correct.")


run_test(questions)
