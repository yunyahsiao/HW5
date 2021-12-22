# coding: utf-8
#更改路徑
import os
os.chdir('C:\\Users\\ASUS\\Desktop\\python')

#讀檔案
filename = 'IMDB-Movie-Data.csv'
f = open(filename,'r')
line = f.readline()

#將每行存為字串
lineList = []
while len(line)>0:
    #print(line,end='')
    lineList.append(line.strip())
    line = f.readline()
f.close()
#把資料第1行取出命名為標題，將標題內容分開方便處理
header = lineList[0].split(",")

#內容
movie = lineList[1:]

#將裡面資料進行切割
movie2=[]
for i in range(len(movie)):
    movie2.append(movie[i].split(","))

#將資料依標題進行分類
value=[]

for i in range(len(header)):
    a = []
    for j in range(len(movie2)):
        a.append(movie2[j][i])
    value.append(a)
#將分類好的資料存進字典裡，以方便查詢
data = {}
for i in range(len(header)):
    data[header[i]]=value[i]
###(1)
def highest_rating(year):
    #將電影跟對應的rating寫進字典
    rating={}
    for i in range(len(movie)):
        #找出特定的年份的rating
        if int(data['Year'][i]) == int(year):
            rating[data['Title'][i]]=data['Rating'][i]

    #從最大到最小排序資料
    rating = sorted(rating.items(),key=lambda x:x[1],reverse=True)
    #列出前三名
    highest_rating = []
    for i in range(3):
        highest_rating.append(rating[i][0]) 
    return(highest_rating)
print('(1)Top-3 movie with the highest ratings in 2016:',highest_rating(2006))
###(2)
revenue = {}
for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
        revenue[actor]=[]
for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
            #將演員演過的電影的revenue找出來
            revenue[actor].append(data['Revenue (Millions)'][i])
for key in revenue:
    for i in range(len(revenue[key])):
        #將缺少的值用0取代
        if revenue[key][i]=='':
            revenue[key][i]=0
#算出平均
for key in revenue:
    sum = 0
    for i in range(len(revenue[key])):
        sum += float(revenue[key][i])
    average = sum/len(revenue[key]) 
    revenue[key]= '%6.2f' % (average)

#從高到低排列
revenue = sorted(revenue.items(),key=lambda x:x[1],reverse=True)

print('(2)The actor generating the highest average revenue:',revenue[0][0],',',revenue[1][0])
###(3)
def average_rating(actor):
    Rating = []
    for i in range(len(movie)):
        #將這個演員演過電影的rating找出來
        if actor in data['Actors'][i]:
            Rating.append(data['Rating'][i])
    sum = 0
    #算出平均
    for i in range(len(Rating)):
        sum += float(Rating[i])
    average = sum/len(Rating)
    print('(3)The average rating of',actor+'\'s movie:',average)
average_rating('Emma Watson')
###(4)
director={}
for i in range(len(movie)):
    director[data['Director'][i]]=[]
#key是導演,value為跟導演合作過的演員
for i in range(len(movie)):
    for j in data['Actors'][i].split("|"):
        director[data['Director'][i]].append(j)


for key in director:
    #用Set避免重複計算
    director[key]=len(set(director[key]))

#排出前三名
number_of_actor=[]
director = sorted(director.items(),key=lambda x:x[1],reverse=True)
for i in range(3):
    number_of_actor.append(director[i][0])
print('(4)Top-3 directors who collaborate with the most actors:',number_of_actor)
###(5)
genre = {}
for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
        genre[actor]=[]

#在一部電影裡，actor&genre不單單只有一個，所以要先用split拆開
for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
        for j in data['Genre'][i].split('|'):
            genre[actor].append(j)

#計算數量
for key in genre:
    genre[key]=len(set(genre[key]))


#演過類型數量從大排到小
genre=sorted(genre.items(),key=lambda x:x[1],reverse=True)

number_of_genre=[]
#選出前2名，有並排的
for i in range(13):
    number_of_genre.append(genre[i][0])
print('(5)Top-2 actors playing in the most genres of movies:',number_of_genre)
###(6)
year={}

for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
        year[actor]=[]

#演員對應年份
for i in range(len(movie)):
    for actor in data['Actors'][i].split('|'):
        year[actor].append(data['Year'][i])

#算出差距
def gap_year(key):
    gap_year = int(max(year[key]))-int(min(year[key]))
    return(gap_year)


gap=[]    
name=[]
for key in year:
    year[key]=gap_year(key)
    a = year[key]
    #將所有gap存在同個list
    gap.append(a)

for key in year: 
    if year[key]==max(gap):
        #將符合條件的演員存在同個list
        name.append(key)
print('(6)Top-3 actors whose movies lead to the largest maximum gap of years:',set(name))
