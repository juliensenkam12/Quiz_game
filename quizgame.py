print('Hello, welcome to our Quiz Game!')

playing = input('Do you want to play? ')
if playing.lower() != 'yes': quit()

print("Okay, let's play!")
score = 0

questions = [
    ('What does CPU stand for? ', 'central processing unit'),
    ('What does RAM stand for? ', 'random access memory'),
    ('What does GPU stand for? ', 'graphics processing unit'),
    ('What does IDE stand for? ', 'integrated development environment'),
    ('What does PSU stand for? ', 'power supply')
]

for question, correct_answer in questions:
    answer = input(question)
    if answer.lower() == correct_answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

print(f"You got {score} questions correct!")
print(f"You got {(score / len(questions)) * 100} %.")




'''print('Hello, welcome to our Quiz Game!')

playing = input('Do you want to play? ')

if playing.lower() != ('yes'):
    quit()
    
print ("okay, Let's play!")
score = 0

answer = input('what does CPU stand for? ')

if answer.lower() == 'central processing unit':
    print('correct!')
    score += 1

else:
    print('incorrect!')
    


answer = input('what does RAM stand for? ')

if answer.lower() == 'ramdom access memory':
    print('correct!')
    score += 1

else:
    print('incorrect!')
    
    
    answer = input('what does GPU stand for? ')

if answer.lower() == 'graphics processing unit':
    print('correct!')
    score += 1

else:
    print('incorrect!')
    
    
    answer = input('what does IDE stand for? ')

if answer.lower() == 'integrated development environment':
    print('correct!')
    score += 1

else:
    print('incorrect!')
    
    
    answer = input('what does PSU stand for? ')

if answer.lower() == 'power supply':
    print('correct!')
    score += 1

else:
    print('incorrect!')
    
print ("you got " +  str(score) +  " questions correct!")
print ("you got " +  str((score / 5) * 100) +  " %.")

'''
