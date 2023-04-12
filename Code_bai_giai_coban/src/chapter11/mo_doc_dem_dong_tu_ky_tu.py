'''
Created on Feb 6, 2017

@author: KTPHUONG
'''
file_in = open('HumptyDumpty.txt','r')
count_lines = 0
count_words = 0
count_chars = 0
print('Content of file:')
for line in file_in:
    print(line)
    count_lines = count_lines + 1
    for word in line.split():
        count_words = count_words + 1
    count_chars = count_chars + len(line)
file_in.close()

print('Lines:', count_lines, ', Words:', count_words, ', Chars:', count_chars)