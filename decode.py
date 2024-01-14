# decode.py
# importing limited functions
# defined in staircase.py
from staircase import create_staircase2

'''
In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you
In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

  1
 2 3
4 5 6
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers
and your function should return the string "I love computers".
'''

# save file content into tuple array
def filecontent_tuple_array (filename):
    result = []
    
    with open(filename, 'r') as f :
       
       for i in f.readlines() :
        
        tmp1 = i.split(" ")
        
        try :
            tmp2 = (int(tmp1[0]), str(tmp1[1]).strip())
            result.append(tmp2)
            
            # print(t)

        except : pass
    
    return result

# place file_contents into staircase, decode message
def decode(fc) :
    pyr_fc = [] #pyramid file contents
    msg = ""
    
    for (x,y) in fc :
        pyr_fc.append(y)
                      
    pyr_fc = create_staircase2(pyr_fc)

    for i in pyr_fc :
        if len(i) == 1 :
            msg = i [len(i) - 1]
        
        else :
            msg = msg + " " + i [len(i) - 1] # decoded message, store last word in each array within pyramid
    
    return(msg)

res = filecontent_tuple_array('coding_qual_input.txt')
res.sort(key=lambda x: x [0])
decode(res)

'''
    TO-DO
    sort
    put into pyramid
    print last tuple of each row
'''

## ********
## BONEYARD
## ********

'''

# b = [1, 2, 3, 4, 5, 6]
# print(b)
# print(create_staircase2(b))

sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)],key=lambda x: x[1], reverse=True)

    p = "/home/vivek/Desktop/test.txt"
    result = []
    with open(p, "rb") as fp:
        for i in fp.readlines():
            tmp = i.split(",")
            try:
                result.append((float(tmp[0]), string(tmp[1])))
                # result.append((eval(tmp[0]), eval(tmp[1])))
            except:pass

    print result
'''

'''
#open the file
text_file = open('/Users/pankaj/abc.txt','r')

#get the list of line
line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)

text_file.close() #don't forget to close the file
'''

'''
        f = open(filename, 'r')
        l = f.readlines();
        i = 0

        for line in l:
            print("i: ", i, line, end="")
            i = i + 1

        f.close()
        # ***

result = []

# fc: file_content

    with open(filename, 'rb') as f :
       
       # print("*1")
       print(f.readlines(0))

       file_contents = f.read()
       
       # print(file_contents)
       print(type(file_contents))
       # for i in file_contents.read() :

       # file_contents.sort()
       # print(file_contents)

       # tmp = file_contents[0].split('\r')
       # print('i:' + i + ' word: ' + tmp)
       # print('*3' + tmp)

       # try :
       #     result.append((int(tmp[0], eval(tmp[1]))))

       # except : pass   

    print (result)

            # print (tmp [1], end="")
            # print(len(tmp))
            # tmp = i.split('\n')
            # tmp [1] = tmp [1].strip('\n')
            # print(tmp)
            # print(f.readlines())
            # tmp = 
            # result.append((int(tmp[0], str(tmp[1]))))
            # print ("*")
   
            # print ("tmp[0]: ", tmp[0, " tmp[1]: ", tmp[1]])

            # from calc import addNumbers, multiplyNumbers

# sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)],key=lambda x: x[1], reverse=True)

# result.append(tmp)

            # print(tmp [0])
            # print(tmp [1])

            # print_contents('coding_qual_input.txt')
# print("result: ", filecontent_tuple_array('coding_qual_input.txt'))
# filecontent_tuple_array('coding_qual_input.txt')

# print contents of file
def print_contents(filename) :
    f = open (filename, 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

'''