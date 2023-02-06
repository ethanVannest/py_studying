# IMPORTS
import random

print('Hello World!')

score = 0

# DICTIONARY FOR QUESTIONS FOR STUDY GUIDE
questions = {
    '1': [
        'What is a default and conversion constructor? ',
        'What are the advantages and disadvantages of multiple inheritance? ',
        'What is a singleton class? ',
        'What is a stream? ',
        'What is a view? ',
        'What is an object? ',
        'What is polymorphism? ',
        'Is string class final? ',
        'What is the difference between overriding and overloading? ',
        'What is a character stream? ',
        'What is a file? ',
        'What is a class? What is a superclass? ',
        'What is inheritance? ',
        'What are the primary components of a computer system? ',
        'What is a chipset? ',
        'What is an operating system? What are the popular operating systems used today? ',
        'What is primary and secondary memory? ',
        'What are the commonly used computer processors? ',
        'What is a constructor? ',
        'What is an interface? ',
        ]
}
answer = input('what are you wanting to study? 1.Computer Science Principles 2. Syntax 3. Make your own study guide. ')


def comp_science_principles(score): 
    num = random.randint(0,19)
    comp_answer = input(questions['1'][num])
    next_num = num + 1
    if comp_answer == questions['1'][next_num]:
        print('Correct!', 'Score:',score)
    else:
        print('Wrong answer.', 'Final Score:',score)
        quit()
    


if answer == '1':
    print('===== Computer Science Principles ======')
    while score != 20:
        score = score + 1
        comp_science_principles(score)
# print(answer)