# 列出dataframe指定列的唯一值
df['Column Name'].unique()

# 把列的数据类型转换为数字。如果有非数字值，则会出错。
pd.to_numeric(df['Column Name'])

# 把列的数据类型转换为数字，如果非数字值，则会转换为NaN
pd.to_numeric(df['Column Name'], errors='coerce')

# 获取DataFrame列中有特定值的行
valuelist = ['value1', 'value2', 'value3']
df = df[df.column.isin(valuelist)]

# 获取DataFrame列中没有特定值的行
valuelist = ['value1', 'value2', 'value3']
df = df[~df.column.isin(value_list)]

# 删除DataFrame的列
del df['column']

# dataframe多列条件查询
# (使用`|`替换 `&`做OR条件)
newdf = df[(df['column_one']>2004) & (df['column_two']==9)]

# DataFrame重命名多列
df = df.rename(columns = {
    'col1 old name':'col1 new name',
    'col2 old name':'col2 new name',
    'col3 old name':'col3 new name',
})

# 把DataFrame的所有列名转换为小写字母
df.columns = map(str.lower, df.columns)

# 重命名列名，并且转换为小写
df.rename(columns=lambda x: x.split('.')[-1], inplace=True)

# DataFrame行迭代
for index, row in df.iterrows():
    print index, row['some column']

# 相对快速的迭代DataFrame每一行
for row in df.itertuples():
    print(row)

# 下面的例子演示了pandas文本数据的使用。
# .str函数完整的列表查看: http://pandas.pydata.org/pandas-docs/stable/text.html

# 对DataFrame的值分片
df.column.str[0:2]

# 对DataFrame的列转换为小写
df.column_name = df.column_name.str.lower()

#列数据的长度
df.column_name.str.len()

# 按多列排序
df = df.sort_values(['col1','col2','col3'],ascending=[1,1,0])

# dataframe排序，分组，然后取每组的前几个。
top5 = df.groupby(['groupingcol1', 'groupingcol2']).head(5)

# 获取DataFrame为null的行
newdf = df[df['column'].isnull()]

# 多层多键查询
df.xs(('index level 1 value','index level 2 value'), level=('level 1','level 2'))

# 把NaN改为None
df = df.where((pd.notnull(df)), None)

# More pre-db insert cleanup...make a pass through the dataframe, stripping whitespace
# from strings and changing any empty values to None
df = df.applymap(lambda x: str(x).strip() if len(str(x).strip()) else None)

# 快速统计DataFrame的行数
len(df.index)

# 透视数据 Pandas >= .14
pd.pivot_table(
  df,values='cell_value',
  index=['col1', 'col2', 'col3'], #these stay as columns; will fail silently if any of these cols have null values
  columns=['col4']) #data values in this column become their own column

# 修改DataFrame列的数据类型
df.column_name = df.column_name.astype(np.int64)

# 替换整个DataFrame里的非数字值：
for col in refunds.columns.values:
  refunds[col] = refunds[col].replace('[^0-9]+.-', '', regex=True)

# 根据其他列值设置DataFrame的列值
df.loc[(df['column1'] == some_value) & (df['column2'] == some_other_value), ['column_to_change']] = new_value

# 清除DataFrame多列的缺失值
df = df.fillna({
    'col1': 'missing',
    'col2': '99.999',
    'col3': '999',
    'col4': 'missing',
    'col5': 'missing',
    'col6': '99'
})

# 将DataFrame的两列连接为新列
df['newcol'] = df['col1'].astype(str) + df['col2'].astype(str)

# 使用缺失值得列做计算
# 下面的例子，把df ['col1']null的值替换为0
df['new_col'] = np.where(pd.isnull(df['col1']),0,df['col1']) + df['col2']

# 把DataFrame的列的值分为两列
df['new_col1'], df['new_col2'] = zip(*df['original_col'].apply(lambda x: x.split(': ', 1)))

# 
df.columns = df.columns.get_level_values(0)

# 转换Django的queryset为DataFrame
qs = DjangoModelName.objects.all()
q = qs.values()
df = pd.DataFrame.from_records(q)

# 根据Python的字典新建DataFrame
df = pd.DataFrame(list(a_dictionary.items()), columns = ['column1', 'column2'])

# 查询dataframe里指定列里重复记录
dupes = df[df.duplicated(['col1', 'col2', 'col3'], keep=False)]

# 为了避免大数不以科学记数法显示，设置格式：
pd.set_option('display.float_format', lambda x: '%.3f' % x)
# 以逗号，小数点显示
pd.options.display.float_format = '{:,.0f}'.format