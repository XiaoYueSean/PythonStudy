import os 
import sys
if __name__ == "__main__":

    # 获取当前文件夹路径
    current_dir_path = sys.path[0]
    # 得到文件的路径
    data_path = os.path.join(current_dir_path, 'data/input_test.txt')

    print('readline读取数据方法')
    with open(data_path, 'r') as file:
        read_firstline = file.readline() # readline 方法读取每一行最后有换行符 \n 
        read_secondline = file.readline()
        read_thirdline = file.readline()
        print(read_firstline)
        print(read_thirdline)

