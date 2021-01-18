# 
import sys

if __name__ == "__main__":
    
    # 以下命令读取所有行
    print('>>>>>>sys.stdin.read()函数开始读取<<<<<<')
    print('>>>>>>请输入N行，输入完毕后用 ctrl + d 终止输入<<<<<<')
    read_all_line = sys.stdin.read() # 输入完后用 ctrl + d 终止
    print('>>>>>>输入结束<<<<<<')
    print(read_all_line)
    print('>>>>>>sys.stdin.read()函数读取结束<<<<<<')
    
    print('>>>>>>sys.stdin.readlines()函数开始读取<<<<<<')
    print('>>>>>>请输入N行，输入完毕后用 ctrl + d 终止输入<<<<<<')
    readline = sys.stdin.readlines()
    print('>>>>>>输入结束<<<<<<')
    print(readline)
    print('>>>>>>sys.stdin.readlines()函数读取读取结束<<<<<<')
    
    # 以下命令是一行一行读取的
    # sys.stdin.readline()会讲标注输入全部获取， 也包括末尾的\n. readline() 方法要用 readline.strip('\n')来获得输入的文本
    # 但对于 input() 方法， 输入会把最后的\n 给忽略掉
    print('sys.stdin.readline()函数开始读取')
    read_first_line = sys.stdin.readline()
    read_second_line = sys.stdin.readline().strip('\n')
    print(read_first_line)
    print(read_second_line)
    print('sys.stdin.readline()函数开始读取结束')

    # input() 读取方法
    print('input开始读取')
    input_data = input()
    print(input_data)

    # 打开文件输入信息
    with open('/data/input_test.txt', 'r') as file:
        

