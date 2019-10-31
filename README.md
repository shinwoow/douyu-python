# douyu-python

> 爬取斗鱼主页的所有直播间信息，并保存到Excel文件中

### 环境

``` BASH
# Python 3.7
```

### 库

```
# requests			
获取网页

# re				     
正则匹配出符合要求的元素节点

# Beautiful Soup	 
格式化网页代码，find需要的节点

# xlwt				   
创建Excel文件
```

### 运行

```
# 进入当前目录
cd douyu-python

# 运行Python文件
py douyu.py
或
双击douyu.py文件

# 成功
自动创建douyu.xls
```

### 备注

```
# 由于xlwt库不支持xlsw文件，故最终创建xls文件

# 斗鱼直播间信息可使用以下api进行获取(尾数为页码数，可修改)
https://www.douyu.com/gapi/rkc/directory/0_0/1
```

