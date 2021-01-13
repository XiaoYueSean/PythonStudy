CSV文件是一种常见的文件格式，用来存储批量数据
CSV文件操作
 
存储命令：
`np.savetxt(frame, array, fmt='%.18e', delimiter=None) `  

frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件  
array : 存入文件的数组   
fmt : 写入文件的格式，例如：%d %.2f %.18e  
delimiter : 分割字符串，默认是任何空格
	
读取命令：`np.loadtxt(frame, dtype=np.float,delimiter=Noneunpack=False)`

frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件  
dtype : 数据类型，可选   
delimiter : 分割字符串，默认是任何空格  
unpack : 如果True，读入属性将分别写入不同变量  
**CSV文件只能有效存储一维和二维数据**

---
arr.mean() #axis = 0 means across the columns/ axis means down the rows

arr.sum()

arr.cumsum() # return the cumulative sum of the elements along a given axis 
```
arr = np.arange(4)
```

arr.cumsum()  # 累加     arr.cumsum(0) 从 column方向加   
```
arr.cumsum(1)  #从 row 的方向加
```

arr.cumprod() # 累乘
 
bools.any( )   # any test whether one or more values in an array is True

bools.all( )   # all checks if every value is True

np.unique(arr) # returns the sorted unique values in a array
