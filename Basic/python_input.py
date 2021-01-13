# 
if __name__ == "__main__":
    import sys
    # 以下命令读取所有行
    print('>>>>>>sys.stdin.read()函数开始读取<<<<<<')
    print('>>>>>>请输入N行，输入完毕后用 ctrl + d 终止输入<<<<<<')
    read_all_line = sys.stdin.read() # 输入完后用 ctrl + d 终止
    print('>>>>>>输入结束<<<<<<')

    print(read_all_line)
    print(read_all_line.split('\n'))
    print('\nsys.stdin.read()函数读取结束')
    print('-'*20)

    
    readline = sys.stdin.readlines()
    print(readline)
    
    # 以下命令是一行一行读取的
    print('sys.stdin.readline()函数开始读取')
    read_first_line = sys.stdin.readline()
    read_second_line = sys.stdin.readline()
    print(read_first_line)
    print('-'*20)
    print(read_second_line)