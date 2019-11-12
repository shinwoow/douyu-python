#!/usr/bin/env python

# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import xlwt

#爬取地址
url = "https://www.douyu.com/directory/all"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

p = 0

s ='python'
result = []


r = requests.get(url, headers = headers)
r.encoding ='utf-8'
so_url = r.request.url
html = r.text
soup = BeautifulSoup(html, "html.parser")

for dlin in soup.find_all('li', class_="layout-Cover-item"):
	#排除10个推荐直播间
	if( p < 10) :
		p += 1
		continue
	text = dlin.prettify()	#格式化样式
	classfy = dlin.find('span', class_="DyListCover-zone").text			#类别
	title = dlin.find('h3', class_="DyListCover-intro").text			#标题
	hot = dlin.find('span', class_="DyListCover-hot is-template").text	#热度
	user = dlin.find('h2', class_="DyListCover-user is-template").text	#主播名
	info = {
		'user': user,
		'classfy': classfy,
		'title': title,
		'hot': hot
	}
	result.append(info)

#创建xls表格
work_book=xlwt.Workbook(encoding='utf-8')
sheet=work_book.add_sheet('1', cell_overwrite_ok=True)
#设置列宽
sheet.col(1).width = 300*20
sheet.col(2).width = 300*20
sheet.col(3).width = 512*20
#写入表头
sheet.write(0,0,"ID")
sheet.write(0,1,"主播")
sheet.write(0,2,"类别")
sheet.write(0,3,"标题")
sheet.write(0,4,"热度")

for i in range(len(result)):#控制行

	for j in range(5):#控制列
		if(j == 0):
			sheet.write(i + 1,j,i + 1)
			continue
		if(j == 1):
			sheet.write(i + 1,j,result[i]['user'])
			continue
		if(j == 2):
			sheet.write(i + 1,j,result[i]['classfy'])
			continue
		if(j == 3):
			sheet.write(i + 1,j,result[i]['title'])
			continue
		if(j == 4):
			sheet.write(i + 1,j,result[i]['hot'])
			continue

work_book.save('douyu.xls')

