#!/usr/bin/env python
# coding: utf-8

# In[50]:


import csv
import matplotlib.pyplot as plt


# In[51]:


this = TemperatureChangedMyBirthday()


# In[52]:


this.read_data()


# In[53]:


print(this.show_highest_temperature())


# In[54]:


#this.save_highest_temperature()


# In[55]:


#this.highest_temperatures_my_birthday()


# In[56]:


data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))


# In[57]:


next(data)


# In[58]:


ls = list(data)


# In[59]:


print([i for i in ls])


# In[60]:


'''
next()는 function 구조로 사용되면 header만 리턴한다
comsumer 구조로 사용되면 데이터에서 header를 제거한다.
row[] = 날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃) 최고기온은 [-1]이다.
data : [] = list() 는  list타입의 data를 list()로 초기화 시킴
단, 한 메소드 내에서만 사용하면 로컬에서 초기화 예제
data : [] = None
def save_highest_temperature(self):
    data = list()
그러나 여러 메소드에서 사용하면 필드에서 초기화 됌
data : [] = list
'''


# In[61]:


print([i[-1] for i in ls])#show_highest_temperature


# In[62]:


highest_temperature = []
[highest_temperature.append(float(i[-1])) for i in ls if i[-1] != ''] 
print({len(highest_temperature)})


# In[64]:


plt.plot(highest_temperature, 'r')
plt.figure(figsize=(10, 2))


# In[74]:


high = [] #  최고기온을 담을 배열
low = [] #최저기온을 담을 배열
for i in ls:
    if i[-1] != '' and i[-2] != '': # 조건문 csv에 있는 인덱스 -1 뒤에서 첫번째 와 두번째가 공백이 없을경우
        if 1983 <= int(i[0].split('-')[0]): # 정수로된 csv에 0번째를 분할해서 분할한것에 인덱스 0번째를 1983보다 작거나 같을때 가지고 와 split()은 기본적으로 문자열공백 자름
            if (i[0].split('-')[1] == '02') and i[0].split('-')[2] == '14':# csv에 0번째 인덱스 를 자른것에 1번째 인덱스와  02를 비교 그리고 2번째인덱스와 14를 비교
                high.append(float(i[-1])) #실수로 된 -1번째 인덱스를 high에 담아라
                low.append(float(i[-2])) #실수로 된 -2번째 인덱스를 low에 담아라


# In[79]:


plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('my birthday')
plt.plot(high, 'hotpink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()


# In[78]:


import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')

font_list[:]


# In[ ]:




