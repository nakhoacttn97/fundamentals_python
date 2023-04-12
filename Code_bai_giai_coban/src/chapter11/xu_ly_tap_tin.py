'''
Created on Feb 13, 2017

@author: KTPHUONG
'''
def read_file(filename):
    f = open(filename,'r')
    str = f.read()
    f.close()
    return str
    

def read_report_file(filename):
    file_in = open(filename,'r')
    count_lines = 0
    count_words = 0
    count_chars = 0
    str = ''
    
    for line in file_in:
        str = str + line
        count_lines = count_lines + 1
        for word in line.split():
            count_words = count_words + 1
        count_chars = count_chars + len(line)
    file_in.close()
    print('Content of file:')
    print(str)
    print("-----Report: Lines/ Words/ Chars-----")
    print('Lines:', count_lines, ', Words:', count_words, ', Chars:', count_chars)
    
def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    #f.write('\n')
    print('Đã ghi nội dung vào tập tin', filename)  
    f.close()

def write_to_end_of_file(filename):
    f = open(filename, 'w')    
    i = 1
    while(i==1):        
        str = input('Nhập nội dung:\n')
        f.write(str)
        f.write('\n')
        i = int(input('Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không\n'))
    print('Đã ghi nội dung vào tập tin', filename)  
    f.close