import random

print('hello world')
questions = {
    '1': [
        'What is a default and conversion constructor?',
        'What are the advantages and disadvantages of multiple inheritance?',
        'What is a singleton class?',
        'What is a stream?',
        'What is a view?',
        'What is an object?',
        'What is polymorphism?',
        'Is string class final?',
        'What is the difference between overriding and overloading?',
        'What is a character stream?',
        'What is a file?',
        'What is a class? What is a superclass?',
        'What is inheritance?',
        'What are the primary components of a computer system?',
        'What is a chipset?',
        'What is an operating system? What are the popular operating systems used today?',
        'What is primary and secondary memory?',
        'What are the commonly used computer processors?',
        'What is a constructor?',
        'What is an interface?',
        ]
}
answer = input('what are you wanting to study? 1.Computer Science Principles 2. Syntax 3. Make your own study guide. ')

print(random.randint(0,9))

if answer == '1':
    print('=====Computer Science Principles======')
    num = random.randint(0,19)
    print(questions['1'][num])
# print(answer)