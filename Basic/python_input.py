# 
if __name__ == "__main__":
    import sys
    
    # 以下命令读取所有行
    print('请输入N行，输入完毕后用 ctrl + d 终止输入')
    read_all_line = sys.stdin.read() # 输入完后用 ctrl + d 终止
    print(read_all_line)
    print(read_all_line.split('\n'))
    print('-'*20)

    s = sys.stdin.readlines()
    print(s)
    
    # 以下命令是一行一行读取的
    read_first_line = sys.stdin.readline()
    read_second_line = sys.stdin.readline()
    print(read_first_line)
    print('-'*20)
    print(read_second_line)