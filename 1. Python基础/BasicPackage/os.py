import os

# __file__  to show the file path, it is a frequency code
print('__file__的结果为:' ,__file__)

# get the current path
print('现在的路径为:',os.getcwd())
# charge the current path as the variable path
print('更改现在的路径为:')
os.chdir(os.path.dirname(__file__))


'''
os.path.xxx function
these 
'''
# os.path.dirname
path = os.path.dirname(__file__)
file_root = os.path.dirname(__file__) # 返回文件所在目录
os.path.exists(path) # 检查文件或者目录是否存在
os.path.isfile(path) # 判断是否为文件
os.path.isdir(path) # 判断是否为目录

print(os.path.basename("dir1/dir2/file.ext")) 
#返回不包含所在目录的文件名
print(os.path.split("dir1/dir2/file.ext")) 
# 返回一个元组, 元组第一个元素为文件所在目录,第二个元素为文件名
print(os.path.splitext("dir1/dir2/file.ext")) 
# 返回一个元组,元组第一个元素为文件所在目录和文件名(不包含扩展),第二个元素为扩展名

os.path.join(path, path) # 将不同部分string拼接成一个地址
os.path.getsize(path) # 返回文件大小

'''
文件操作
目录操作
'''
os.listdir(path='.') # 返回一个列表,列表里面包含目录下所以文件和文件夹
os.mkdir(path) # 创建一个名为path的文件夹, 比如 "output"
os.makedirs(path) # 递归方式创建路径为path的目录, 比如 "parent/child/newdir"
os.rmdir(path) # 删除目录, 目录必须存在,并且只能删除空目录. 想要递归删除整个目录树,要使用shutil.rmtree()
os.remove(path) # 删除文件