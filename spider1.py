import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def get_infor(url):
    name_list=[]
    href_list=[]
    # url='https://www.80txt.com/sort/{}.html'.format(page)
    sort_list=requests.get(url)
    noval_list=BeautifulSoup(sort_list.text,'lxml')
    noval_infor=noval_list.select("#list_art_2013 > div.list_box > div.title_box > div.book_bg > a") 
    for list in noval_infor:
         name=list.get_text().split(' ')[0]
         href=list.get('href').split('z')[1].split('.')[0].split('/')[1]
         name_list.append(name)
         href_list.append(href)

    return name_list,href_list

def get_list(url):
    name_list,href_list=get_infor(url)
    for i,j in zip(name_list,href_list):
          print(i+str(j))
         
        
urls=['https://www.80txt.com/sort/{}.html'.format(i) for i in  range(1,300)] #the page can set from 1 to 3900


if __name__ == '__main__':
    a=input("input amount of process:")#set number of pool
    pool = Pool(int(a))
    pool.map(get_list,urls) #runing 

