score = 0
print('welcome to gamer')

x = input('are you ready to play? yes or no')

if x == 'yes':
    usr = input('you are two questions.do you want to continue ' )
    if usr == 'yes':
        
        ans = input('what is my name? ')
        if ans == 'bryan':
            score += 1
        ans = int(input('how old am i? '))
        if ans == 17:
            score += 1
        print('your score is ', score)
        print('Thank you for playing')



    



print('Goodbye')
