print('Hello , welcome to trivia')

ans = input('Are you ready to play : yes / no:')
score = 0
total_q = 4

if ans. lower() == 'yes':
    ans = input('1.what is the best programming language ?')
if ans. lower() == 'python':
    score += 25
    print('Yeah,you are absolutely correct')
else:
    print('No, you are extremely wrong')

ans = input('2.what is my fav game ?')
if ans. lower() == 'badminton':
    score += 25
    print('Yeah,you are absolutely correct')
else:
    print('No, you are extremely wrong')

ans = input('3.what is 1024 + 1024?')
if ans == '2048':
    score += 25
    print('Yeah,you are absolutely correct')
else:
    print('No, you are extremely wrong')

ans = input('4.which is the smallest state in India?')
if ans == 'Goa':
    score += 25
    print('Yeah,you are absolutely correct')
else:
    print('No, you are extremely wrong')

print('Thanks for playing. \n Your score is: ', score)