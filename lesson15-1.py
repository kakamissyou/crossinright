from random import choice
YOUR_SCORE =0
COMPUTER_SCORE = 0
for i in range(1,7):
    print 'please choose one side to shoot!left center right!'
    #Goal
    direction = ['left','center','right']
    com = choice(direction)
    print 'Computer saved %s'%com
    #Guess
    you = raw_input()
    print 'You kicked%s '%you
    if you!=com:
        print 'Oops!,you get worng!'
        COMPUTER_SCORE+=1
        print 'Round %d,currently,you have %d,computer have %d'%(i,YOUR_SCORE,COMPUTER_SCORE)
    else:
        print 'Goal!'
        YOUR_SCORE+=1
        print 'Round %d,currently,you have %d,computer have %d'%(i,YOUR_SCORE,COMPUTER_SCORE)

#以上是循环部分，下面是显示最终结果。
print 'Finala Result:'
print 'you_score is %d'%YOUR_SCORE
print 'computer_score is %d'%COMPUTER_SCORE

