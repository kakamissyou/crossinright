#Read file
try:
    f = file('lesson15.py')
    data = f.read()
    print data
    f.close()
except:
    print 'file lesson15-1.py does not exist!'

#write file
#x = open('sex.txt','w')
#x.write(data)
#x.close()