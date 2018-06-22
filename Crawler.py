#coding=utf-8
from bs4 import BeautifulSoup
import time
import random
import requests
import re 
from selenium import webdriver

#Create txt to store the contents of the news
def text_create(name, msg):   
    path = 'd:\\robot\\'    
    full_path = path + name + '.txt' 
    file = open(full_path,'w')             
    file.write(msg) 
    file.close() 
    print('Done')
text_create('news1','nothing')
text_create('news2','nothing')
text_create('news3','nothing')
text_create('news4','nothing')
text_create('news5','nothing')
text_create('news6','nothing')
text_create('news7','nothing')
text_create('news8','nothing')
text_create('news9','nothing')
text_create('news10','nothing')

#url_list
url_list=["http://www.ce.cn/cysc/fdc/fc/",
          "http://datanews.dichan.com/NewsList.aspx?pageIndex=1&category=01&SubCategory=",
          "http://datanews.dichan.com/NewsList.aspx?pageIndex=1&category=02&SubCategory=",
          "http://datanews.dichan.com/NewsList.aspx?pageIndex=1&category=04&SubCategory=",
          "http://www.guandian.cn/news/"]

#Initial housing price
result_beijing_final_time='*'
result_suzhou_final_time='*'
result_wuxi_final_time='*'
result_xian_final_time='*'

result_beijing_final_1='*'
result_beijing_final_2='*'
result_shanghai_final_1='*'
result_shanghai_final_2='*'
result_guangzhou_final_1='*'
result_guangzhou_final_2='*'
result_shenzhen_final_1='*'
result_shenzhen_final_2='*'
result_chongqing_final_1='*'
result_chongqing_final_2='*'
result_tianjin_final_1='*'
result_tianjin_final_2='*'
result_suzhou_final_1='*'
result_suzhou_final_2='*'
result_wuhan_final_1='*'
result_wuhan_final_2='*'
result_chengdu_final_1='*'
result_chengdu_final_2='*'
result_hangzhou_final_1='*'
result_hangzhou_final_2='*'
result_nanjing_final_1='*'
result_nanjing_final_2='*'
result_qingdao_final_1='*'
result_qingdao_final_2='*'
result_wuxi_final_1='*'
result_wuxi_final_2='*'
result_changsha_final_1='*'
result_changsha_final_2='*'
result_ningbo_final_1='*'
result_ningbo_final_2='*'
result_shenyang_final_1='*'
result_shenyang_final_2='*'
result_changchun_final_1='*'
result_changchun_final_2='*'
result_xiamen_final_1='*'
result_xiamen_final_2='*'
result_xian_final_1='*'
result_xian_final_2='*'
result_taiyuan_final_1='*'
result_taiyuan_final_2='*'
result_nanchang_final_1='*'
result_nanchang_final_2='*'
result_sanya_final_1='*'
result_sanya_final_2='*'
result_kunming_final_1='*'
result_kunming_final_2='*'
result_nanning_final_1='*'
result_nanning_final_2='*'

#start to crawl   
randomsleep7=random.randint(60,120)
time.sleep(randomsleep7)
while True:
    try:
    #the 1st website
        url1 = url_list[0]
        r1 = requests.get(url1,allow_redirects=False)
        soup1 = BeautifulSoup(r1.content,'lxml')
        link1=soup1.select('.top tr a:nth-of-type(2)')
        href1=link1[0].get('href')
        href1_final='http://www.ce.cn/cysc/fdc'+href1[2:]
        print(link1)
        print(href1)
        print(href1_final)
        #开始解析，得到标题
        randomsleep1=random.randint(60,120)
        time.sleep(randomsleep1)
        r1_final = requests.get(href1_final,allow_redirects=False)
        soup1_final = BeautifulSoup(r1_final.content,'html5lib')
        link1_final1=soup1_final.select('title:nth-of-type(1)')
        result1_1=link1_final1[0].get_text()
        #得到第1段
        link1_final2=soup1_final.select('.content p:nth-of-type(1)')
        result1_2=link1_final2[0].get_text()
        #得到第2段
        link1_final3=soup1_final.select('.content p:nth-of-type(2)')
        result1_3=link1_final3[0].get_text()
        link1_time_1=soup1_final.select('.laiyuan #articleTime')
        result1_time_1=link1_time_1[0].get_text()
        result1_time_2=result1_time_1[-5:]
        #拼接摘要，消除空格
        result10=re.sub('\s','',result1_1)
        result11=result1_2+result1_3
        result12=re.sub('\s','',result11)
        result1_time=re.sub('\s','',result1_time_2)
        #得到第1个网站的最终结果，即拼接标题和摘要
        result1_final=result1_time+'  '+'【'+result10+'】'+'\n'+result12
        print(result1_final)

        fp=open('d:\\robot\\news1.txt','wb')
        fp.write(result1_final.encode('gb18030'))
        fp.close()
        print('The 1st website has been done.——————————————————————————')       
    except:
        print('There is a trouble with the 1st website.——————————————————————————')
        print('There is a trouble with the 1st website.——————————————————————————')
        print('There is a trouble with the 1st website.——————————————————————————')

    try:
        #the 5th website
        url5 = url_list[4]
        r5 = requests.get(url5,allow_redirects=False)
        soup5 = BeautifulSoup(r5.content,'lxml')
        link5=soup5.select('.con_l a:nth-of-type(1)')
        href5=link5[0].get('href')
        href5_final='http://www.guandian.cn'+href5
        print(link5)
        print(href5)
        print(href5_final)
        #开始解析，得到标题
        randomsleep5=random.randint(60,120)
        time.sleep(randomsleep5)
        r5_final = requests.get(href5_final,allow_redirects=False)
        soup5_final = BeautifulSoup(r5_final.content,'lxml')
        link5_final1=soup5_final.select('title:nth-of-type(1)')
        result5_1=link5_final1[0].get_text()
        #得到第1段
        link5_final2=soup5_final.select('.abstract')
        result5_2=link5_final2[0].get_text()
        link5_time_1=soup5_final.select('.con_l_info_l p:nth-of-type(1)')
        result5_time_1=link5_time_1[0].get_text()
        result5_time_2=result5_time_1[-5:]
        #拼接摘要，消除空格
        result50=re.sub('\s','',result5_1)
        result51=result5_2
        result52=re.sub('\s','',result51)
        result5_time=re.sub('\s','',result5_time_2)
        #得到第5个网站的最终结果，即拼接标题和摘要
        result5_final=result5_time+'  '+'【'+result50+'】'+'\n'+result52
        print(result5_final)

        fp=open('d:\\robot\\news5.txt','wb')
        fp.write(result5_final.encode('gb18030'))
        fp.close() 
        print('The 5th website has been done.——————————————————————————')
    except:
        print('There is a trouble with the 5th website.——————————————————————————')
        print('There is a trouble with the 5th website.——————————————————————————')
        print('There is a trouble with the 5th website.——————————————————————————')

    
    try:
        #the 2nd website
        url2 = url_list[1]
        r2 = requests.get(url2,allow_redirects=False)
        soup2 = BeautifulSoup(r2.content,'lxml')
        link2=soup2.select('.fs14 a:nth-of-type(1)')
        href2=link2[0].get('href')
        href2_final=href2
        print(link2)
        print(href2)
        print(href2_final)
        #开始解析，得到标题
        randomsleep2=random.randint(60,120)
        time.sleep(randomsleep2)
        r2_final = requests.get(href2_final,allow_redirects=False)
        soup2_final = BeautifulSoup(r2_final.content,'lxml')
        link2_final1=soup2_final.select('title:nth-of-type(1)')
        result2_1=link2_final1[0].get_text()
        #得到第1段
        link2_final2=soup2_final.select('.quote')
        result2_2=link2_final2[0].get_text()
        link2_time_1=soup2_final.select('#pub_date')
        result2_time_1=link2_time_1[0].get_text()
        result2_time_2=result2_time_1[-8:-3]
        #拼接摘要，消除空格
        result20=re.sub('\s','',result2_1)
        result21=re.sub('\s','',result2_2)
        result21=result21[3:]
        result2_time=re.sub('\s','',result2_time_2)
        #得到第2个网站的最终结果，即拼接标题和摘要
        result2_final=result2_time+'  '+'【'+result20+'】'+'\n'+result21
        print(result2_final)
        
        fp=open('d:\\robot\\news2.txt','wb')
        fp.write(result2_final.encode('gb18030'))
        fp.close()
        print('The 2nd website has been done.——————————————————————————')
    except:
        print('There is a trouble with the 2nd website.——————————————————————————')
        print('There is a trouble with the 2nd website.——————————————————————————')
        print('There is a trouble with the 2nd website.——————————————————————————')
    
    try:
        #the 3rd website
        url3 = url_list[2]
        r3 = requests.get(url3,allow_redirects=False)
        soup3 = BeautifulSoup(r3.content,'lxml')
        link3=soup3.select('.fs14 a:nth-of-type(1)')
        href3=link3[0].get('href')
        href3_final=href3
        print(link3)
        print(href3)
        print(href3_final)
        #开始解析，得到标题
        randomsleep3=random.randint(60,120)
        time.sleep(randomsleep3)
        r3_final = requests.get(href3_final,allow_redirects=False)
        soup3_final = BeautifulSoup(r3_final.content,'lxml')
        link3_final1=soup3_final.select('title:nth-of-type(1)')
        result3_1=link3_final1[0].get_text()
        #得到第1段
        link3_final2=soup3_final.select('.quote')
        result3_2=link3_final2[0].get_text()
        link3_time_1=soup3_final.select('#pub_date')
        result3_time_1=link3_time_1[0].get_text()
        result3_time_2=result3_time_1[-8:-3]
        #拼接摘要，消除空格
        result30=re.sub('\s','',result3_1)
        result31=re.sub('\s','',result3_2)
        result31=result31[3:]
        result3_time=re.sub('\s','',result3_time_2)
        #得到第3个网站的最终结果，即拼接标题和摘要
        result3_final=result3_time+'  '+'【'+result30+'】'+'\n'+result31
        print(result3_final)
        
        fp=open('d:\\robot\\news3.txt','wb')
        fp.write(result3_final.encode('gb18030'))
        fp.close()
        print('The 3rd website has been done.——————————————————————————')
    except:
        print('There is a trouble with the 3rd website.——————————————————————————')
        print('There is a trouble with the 3rd website.——————————————————————————')
        print('There is a trouble with the 3rd website.——————————————————————————')
    
    try:
        #the 4th website
        url4 = url_list[3]
        r4 = requests.get(url4,allow_redirects=False)
        soup4 = BeautifulSoup(r4.content,'lxml')
        link4=soup4.select('.fs14 a:nth-of-type(1)')
        href4=link4[0].get('href')
        href4_final=href4
        print(link4)
        print(href4)
        print(href4_final)
        #开始解析，得到标题
        randomsleep4=random.randint(60,120)
        time.sleep(randomsleep4)
        r4_final = requests.get(href4_final,allow_redirects=False)
        soup4_final = BeautifulSoup(r4_final.content,'lxml')
        link4_final1=soup4_final.select('title:nth-of-type(1)')
        result4_1=link4_final1[0].get_text()
        #得到第1段
        link4_final2=soup4_final.select('.quote')
        result4_2=link4_final2[0].get_text()
        link4_time_1=soup4_final.select('#pub_date')
        result4_time_1=link4_time_1[0].get_text()
        result4_time_2=result4_time_1[-8:-3]
        #拼接摘要，消除空格
        result40=re.sub('\s','',result4_1)
        result41=re.sub('\s','',result4_2)
        result41=result41[3:]
        result4_time=re.sub('\s','',result4_time_2)
        #得到第4个网站的最终结果，即拼接标题和摘要
        result4_final=result4_time+'  '+'【'+result40+'】'+'\n'+result41
        print(result4_final)

        fp=open('d:\\robot\\news4.txt','wb')
        fp.write(result4_final.encode('gb18030'))
        fp.close() 
        print('The 4th website has been done.——————————————————————————')
    except:
        print('There is a trouble with the 4th website.——————————————————————————')
        print('There is a trouble with the 4th website.——————————————————————————')
        print('There is a trouble with the 4th website.——————————————————————————')
        
    try:
        #the 6th website
        url6='http://so.eastmoney.com/news/s?keyword=%E6%88%BF%E5%9C%B0%E4%BA%A7'
        #chrome driver
        options=webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"')
        
        path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        browser=webdriver.Chrome(executable_path=path,chrome_options=options)      
        browser.get(url6)
        time.sleep(8)
        inputs0=browser.find_elements_by_xpath("//span[@class='still']//a")
        time.sleep(8)
        inputs0[0].click()
        time.sleep(8)
        if len(browser.window_handles) > 1:
            browser.close()
            
        browser.switch_to_window(browser.window_handles[0])
        inputs=browser.find_elements_by_xpath("//h3//a")
        inputs[0].click()
        time.sleep(8)
        
        if len(browser.window_handles) > 2:
            browser.close()
    
        browser.switch_to_window(browser.window_handles[1])
        time.sleep(8)
        url6_1=browser.current_url
        r6=requests.get(url6_1,allow_redirects=False)
        soup6 = BeautifulSoup(r6.content,'lxml')
        time.sleep(8)
        browser.close()
        browser.switch_to_window(browser.window_handles[0])
        #print(soup)
        link6_1=soup6.select('title:nth-of-type(1)')
        result6_1=link6_1[0].get_text()
        #print(result6_1)
        link6_2=soup6.select('.Body p:nth-of-type(1)')
        result6_2=link6_2[0].get_text()
        link6_time_1=soup6.select('.time')
        result6_time_1=link6_time_1[0].get_text()
        result6_time_2=result6_time_1[-5:]
        #print(result6_2)
        result60=re.sub('\s','',result6_1)
        result61=re.sub('\s','',result6_2)
        result6_time=re.sub('\s','',result6_time_2)
        #得到第6个网站的最终结果，即拼接标题和摘要
        result6_final=result6_time+'  '+'【'+result60+'】'+'\n'+result61
        #过滤掉乱入的股票信息
        for word in result60 :
            if word =='股':
                result6_final='nothing'
        if len(result61)<=50 :
            result6_final='nothing'
            
        print(result6_final)

        fp=open('d:\\robot\\news6.txt','wb')
        fp.write(result6_final.encode('gb18030'))
        fp.close()
        browser.quit()
        print('The 6th website has been done.——————————————————————————')
    except:
        browser.quit()
        print('There is a trouble with the 6th website.——————————————————————————')
        print('There is a trouble with the 6th website.——————————————————————————')
        print('There is a trouble with the 6th website.——————————————————————————')
                        
    randomsleep6=random.randint(60,120)
    time.sleep(randomsleep6)
    
    current_time = time.localtime(time.time())
    if((current_time.tm_hour == 17) and (current_time.tm_min <= 24)) :
        #第1波城市房价
        try:
            #1 北京
            url_beijing='http://www.creprice.cn/market/bj/forsale/ALL/11.html'
            r_beijing = requests.get(url_beijing,allow_redirects=False)
            soup_beijing = BeautifulSoup(r_beijing.content,'lxml')
            link_beijing_time=soup_beijing.select('.utitle .up_time')
            result_beijing_time=link_beijing_time[0].get_text()
            
            link_beijing_1=soup_beijing.select('.u_list li .value')
            result_beijing_1=link_beijing_1[1].get_text()
            
            link_beijing_2=soup_beijing.select('.u_list li span')
            result_beijing_2=link_beijing_2[16].get_text()
            
            result_beijing_final_time=re.sub('\s','',result_beijing_time)
            result_beijing_final_time=result_beijing_final_time[7:]
            result_beijing_final_1=re.sub('\s','',result_beijing_1)
            result_beijing_final_2=re.sub('\s','',result_beijing_2)
            print(result_beijing_final_time)
            print(result_beijing_final_1)
            print(result_beijing_final_2)
            print('beijing houseprice has been collected_________')
            randomsleep71=random.randint(60,120)
            time.sleep(randomsleep71)
            
            #2 上海
            url_shanghai='http://www.creprice.cn/market/sh/forsale/ALL/11.html'
            r_shanghai = requests.get(url_shanghai,allow_redirects=False)
            soup_shanghai = BeautifulSoup(r_shanghai.content,'lxml')
            link_shanghai_time=soup_shanghai.select('.utitle .up_time')
            result_shanghai_time=link_shanghai_time[0].get_text()
            
            link_shanghai_1=soup_shanghai.select('.u_list li .value')
            result_shanghai_1=link_shanghai_1[1].get_text()
            
            link_shanghai_2=soup_shanghai.select('.u_list li span')
            result_shanghai_2=link_shanghai_2[16].get_text()
            
            result_shanghai_final_time=re.sub('\s','',result_shanghai_time)
            result_shanghai_final_time=result_shanghai_final_time[7:]
            result_shanghai_final_1=re.sub('\s','',result_shanghai_1)
            result_shanghai_final_2=re.sub('\s','',result_shanghai_2)
            print(result_shanghai_final_time)
            print(result_shanghai_final_1)
            print(result_shanghai_final_2)
            print('shanghai houseprice has been collected_________')
            randomsleep72=random.randint(60,120)
            time.sleep(randomsleep72)
            
            #3 广州
            url_guangzhou='http://www.creprice.cn/market/gz/forsale/ALL/11.html'
            r_guangzhou = requests.get(url_guangzhou,allow_redirects=False)
            soup_guangzhou = BeautifulSoup(r_guangzhou.content,'lxml')
            link_guangzhou_time=soup_guangzhou.select('.utitle .up_time')
            result_guangzhou_time=link_guangzhou_time[0].get_text()
            
            link_guangzhou_1=soup_guangzhou.select('.u_list li .value')
            result_guangzhou_1=link_guangzhou_1[1].get_text()
            
            link_guangzhou_2=soup_guangzhou.select('.u_list li span')
            result_guangzhou_2=link_guangzhou_2[16].get_text()
            
            result_guangzhou_final_time=re.sub('\s','',result_guangzhou_time)
            result_guangzhou_final_time=result_guangzhou_final_time[7:]
            result_guangzhou_final_1=re.sub('\s','',result_guangzhou_1)
            result_guangzhou_final_2=re.sub('\s','',result_guangzhou_2)
            print(result_guangzhou_final_time)
            print(result_guangzhou_final_1)
            print(result_guangzhou_final_2)
            print('guangzhou houseprice has been collected_________')
            randomsleep73=random.randint(60,120)
            time.sleep(randomsleep73)
            
            #4深圳
            url_shenzhen='http://www.creprice.cn/market/sz/forsale/ALL/11.html'
            r_shenzhen = requests.get(url_shenzhen,allow_redirects=False)
            soup_shenzhen = BeautifulSoup(r_shenzhen.content,'lxml')
            link_shenzhen_time=soup_shenzhen.select('.utitle .up_time')
            result_shenzhen_time=link_shenzhen_time[0].get_text()
            
            link_shenzhen_1=soup_shenzhen.select('.u_list li .value')
            result_shenzhen_1=link_shenzhen_1[1].get_text()
            
            link_shenzhen_2=soup_shenzhen.select('.u_list li span')
            result_shenzhen_2=link_shenzhen_2[16].get_text()
            
            result_shenzhen_final_time=re.sub('\s','',result_shenzhen_time)
            result_shenzhen_final_time=result_shenzhen_final_time[7:]
            result_shenzhen_final_1=re.sub('\s','',result_shenzhen_1)
            result_shenzhen_final_2=re.sub('\s','',result_shenzhen_2)
            print(result_shenzhen_final_time)
            print(result_shenzhen_final_1)
            print(result_shenzhen_final_2)
            print('shenzhen houseprice has been collected_________')
            randomsleep74=random.randint(60,120)
            time.sleep(randomsleep74)
            
            #5 重庆
            url_chongqing='http://www.creprice.cn/market/cq/forsale/ALL/11.html'
            r_chongqing = requests.get(url_chongqing,allow_redirects=False)
            soup_chongqing = BeautifulSoup(r_chongqing.content,'lxml')
            link_chongqing_time=soup_chongqing.select('.utitle .up_time')
            result_chongqing_time=link_chongqing_time[0].get_text()
            
            link_chongqing_1=soup_chongqing.select('.u_list li .value')
            result_chongqing_1=link_chongqing_1[1].get_text()
            
            link_chongqing_2=soup_chongqing.select('.u_list li span')
            result_chongqing_2=link_chongqing_2[16].get_text()
            
            result_chongqing_final_time=re.sub('\s','',result_chongqing_time)
            result_chongqing_final_time=result_chongqing_final_time[7:]
            result_chongqing_final_1=re.sub('\s','',result_chongqing_1)
            result_chongqing_final_2=re.sub('\s','',result_chongqing_2)
            print(result_chongqing_final_time)
            print(result_chongqing_final_1)
            print(result_chongqing_final_2)
            print('chongqing houseprice has been collected_________')
            randomsleep75=random.randint(60,120)
            time.sleep(randomsleep75)
            
            #6 天津
            url_tianjin='http://www.creprice.cn/market/tj/forsale/ALL/11.html'
            r_tianjin = requests.get(url_tianjin,allow_redirects=False)
            soup_tianjin = BeautifulSoup(r_tianjin.content,'lxml')
            link_tianjin_time=soup_tianjin.select('.utitle .up_time')
            result_tianjin_time=link_tianjin_time[0].get_text()
            
            link_tianjin_1=soup_tianjin.select('.u_list li .value')
            result_tianjin_1=link_tianjin_1[1].get_text()
            
            link_tianjin_2=soup_tianjin.select('.u_list li span')
            result_tianjin_2=link_tianjin_2[16].get_text()
            
            result_tianjin_final_time=re.sub('\s','',result_tianjin_time)
            result_tianjin_final_time=result_tianjin_final_time[7:]
            result_tianjin_final_1=re.sub('\s','',result_tianjin_1)
            result_tianjin_final_2=re.sub('\s','',result_tianjin_2)
            print(result_tianjin_final_time)
            print(result_tianjin_final_1)
            print(result_tianjin_final_2)
            print('tianjin houseprice has been collected_________')
            randomsleep76=random.randint(60,120)
            time.sleep(randomsleep76)
            
            #1针对网站未更新的情况
            if result_beijing_final_1=='--' :
                result_beijing_final_time='*'
                result_beijing_final_1='*'
                result_beijing_final_2='*'
            if result_shanghai_final_1=='--' :
                result_shanghai_final_1='*'
                result_shanghai_final_2='*'
            if result_guangzhou_final_1=='--' :
                result_guangzhou_final_1='*'
                result_guangzhou_final_2='*'
            if result_shenzhen_final_1=='--' :
                result_shenzhen_final_1='*'
                result_shenzhen_final_2='*'
            if result_chongqing_final_1=='--' :
                result_chongqing_final_1='*'
                result_chongqing_final_2='*'
            if result_tianjin_final_1=='--' :
                result_tianjin_final_1='*'
                result_tianjin_final_2='*'                
            
            result7_1='【每日城市房价报道（1）】'+'\n'+result_beijing_final_time+'\n'+'北京：'+result_beijing_final_1+'元/平'+'('+result_beijing_final_2+')'+'\n'
            result7_2='上海：'+result_shanghai_final_1+'元/平'+'('+result_shanghai_final_2+')'+'\n'
            result7_3='广州：'+result_guangzhou_final_1+'元/平'+'('+result_guangzhou_final_2+')'+'\n'
            result7_4='深圳：'+result_shenzhen_final_1+'元/平'+'('+result_shenzhen_final_2+')'+'\n'
            result7_5='重庆：'+result_chongqing_final_1+'元/平'+'('+result_chongqing_final_2+')'+'\n'
            result7_6='天津：'+result_tianjin_final_1+'元/平'+'('+result_tianjin_final_2+')'
            result7_final=result7_1+result7_2+result7_3+result7_4+result7_5+result7_6
            print(result7_final)
    
            fp=open('d:\\robot\\news7.txt','wb')
            fp.write(result7_final.encode('gb18030'))
            fp.close() 
            print('The 7th website has been done.——————————————————————————')
        except:
            print('There is a trouble with the 7th website.——————————————————————————')
            print('There is a trouble with the 7th website.——————————————————————————')
            print('There is a trouble with the 7th website.——————————————————————————') 
        
        #第2波城市房价
        try:
            #7 苏州
            url_suzhou='http://www.creprice.cn/market/su/forsale/ALL/11.html'
            r_suzhou = requests.get(url_suzhou,allow_redirects=False)
            soup_suzhou = BeautifulSoup(r_suzhou.content,'lxml')
            link_suzhou_time=soup_suzhou.select('.utitle .up_time')
            result_suzhou_time=link_suzhou_time[0].get_text()
            
            link_suzhou_1=soup_suzhou.select('.u_list li .value')
            result_suzhou_1=link_suzhou_1[1].get_text()
            
            link_suzhou_2=soup_suzhou.select('.u_list li span')
            result_suzhou_2=link_suzhou_2[16].get_text()
            
            result_suzhou_final_time=re.sub('\s','',result_suzhou_time)
            result_suzhou_final_time=result_suzhou_final_time[7:]
            result_suzhou_final_1=re.sub('\s','',result_suzhou_1)
            result_suzhou_final_2=re.sub('\s','',result_suzhou_2)
            print(result_suzhou_final_time)
            print(result_suzhou_final_1)
            print(result_suzhou_final_2)
            print('suzhou houseprice has been collected_________')
            randomsleep81=random.randint(60,120)
            time.sleep(randomsleep81)
            
            #8 武汉
            url_wuhan='http://www.creprice.cn/market/wh/forsale/ALL/11.html'
            r_wuhan = requests.get(url_wuhan,allow_redirects=False)
            soup_wuhan = BeautifulSoup(r_wuhan.content,'lxml')
            link_wuhan_time=soup_wuhan.select('.utitle .up_time')
            result_wuhan_time=link_wuhan_time[0].get_text()
            
            link_wuhan_1=soup_wuhan.select('.u_list li .value')
            result_wuhan_1=link_wuhan_1[1].get_text()
            
            link_wuhan_2=soup_wuhan.select('.u_list li span')
            result_wuhan_2=link_wuhan_2[16].get_text()
            
            result_wuhan_final_time=re.sub('\s','',result_wuhan_time)
            result_wuhan_final_time=result_wuhan_final_time[7:]
            result_wuhan_final_1=re.sub('\s','',result_wuhan_1)
            result_wuhan_final_2=re.sub('\s','',result_wuhan_2)
            print(result_wuhan_final_time)
            print(result_wuhan_final_1)
            print(result_wuhan_final_2)
            print('wuhan houseprice has been collected_________')
            randomsleep82=random.randint(60,120)
            time.sleep(randomsleep82)
            
            #9 成都
            url_chengdu='http://www.creprice.cn/market/cd/forsale/ALL/11.html'
            r_chengdu = requests.get(url_chengdu,allow_redirects=False)
            soup_chengdu = BeautifulSoup(r_chengdu.content,'lxml')
            link_chengdu_time=soup_chengdu.select('.utitle .up_time')
            result_chengdu_time=link_chengdu_time[0].get_text()
            
            link_chengdu_1=soup_chengdu.select('.u_list li .value')
            result_chengdu_1=link_chengdu_1[1].get_text()
            
            link_chengdu_2=soup_chengdu.select('.u_list li span')
            result_chengdu_2=link_chengdu_2[15].get_text()
            
            result_chengdu_final_time=re.sub('\s','',result_chengdu_time)
            result_chengdu_final_time=result_chengdu_final_time[7:]
            result_chengdu_final_1=re.sub('\s','',result_chengdu_1)
            result_chengdu_final_2=re.sub('\s','',result_chengdu_2)
            print(result_chengdu_final_time)
            print(result_chengdu_final_1)
            print(result_chengdu_final_2)
            print('chengdu houseprice has been collected_________')
            randomsleep83=random.randint(60,120)
            time.sleep(randomsleep83)
            
            #10 杭州
            url_hangzhou='http://www.creprice.cn/market/hz/forsale/ALL/11.html'
            r_hangzhou = requests.get(url_hangzhou,allow_redirects=False)
            soup_hangzhou = BeautifulSoup(r_hangzhou.content,'lxml')
            link_hangzhou_time=soup_hangzhou.select('.utitle .up_time')
            result_hangzhou_time=link_hangzhou_time[0].get_text()
            
            link_hangzhou_1=soup_hangzhou.select('.u_list li .value')
            result_hangzhou_1=link_hangzhou_1[1].get_text()
            
            link_hangzhou_2=soup_hangzhou.select('.u_list li span')
            result_hangzhou_2=link_hangzhou_2[16].get_text()
            
            result_hangzhou_final_time=re.sub('\s','',result_hangzhou_time)
            result_hangzhou_final_time=result_hangzhou_final_time[7:]
            result_hangzhou_final_1=re.sub('\s','',result_hangzhou_1)
            result_hangzhou_final_2=re.sub('\s','',result_hangzhou_2)
            print(result_hangzhou_final_time)
            print(result_hangzhou_final_1)
            print(result_hangzhou_final_2)
            print('hangzhou houseprice has been collected_________')
            randomsleep84=random.randint(60,120)
            time.sleep(randomsleep84)
            
            #11 南京
            url_nanjing='http://www.creprice.cn/market/nj/forsale/ALL/11.html'
            r_nanjing = requests.get(url_nanjing,allow_redirects=False)
            soup_nanjing = BeautifulSoup(r_nanjing.content,'lxml')
            link_nanjing_time=soup_nanjing.select('.utitle .up_time')
            result_nanjing_time=link_nanjing_time[0].get_text()
            
            link_nanjing_1=soup_nanjing.select('.u_list li .value')
            result_nanjing_1=link_nanjing_1[1].get_text()
            
            link_nanjing_2=soup_nanjing.select('.u_list li span')
            result_nanjing_2=link_nanjing_2[16].get_text()
            
            result_nanjing_final_time=re.sub('\s','',result_nanjing_time)
            result_nanjing_final_time=result_nanjing_final_time[7:]
            result_nanjing_final_1=re.sub('\s','',result_nanjing_1)
            result_nanjing_final_2=re.sub('\s','',result_nanjing_2)
            print(result_nanjing_final_time)
            print(result_nanjing_final_1)
            print(result_nanjing_final_2)
            print('nanjing houseprice has been collected_________')
            randomsleep85=random.randint(60,120)
            time.sleep(randomsleep85)
            
            #12 青岛
            url_qingdao='http://www.creprice.cn/market/qd/forsale/ALL/11.html'
            r_qingdao = requests.get(url_qingdao,allow_redirects=False)
            soup_qingdao = BeautifulSoup(r_qingdao.content,'lxml')
            link_qingdao_time=soup_qingdao.select('.utitle .up_time')
            result_qingdao_time=link_qingdao_time[0].get_text()
            
            link_qingdao_1=soup_qingdao.select('.u_list li .value')
            result_qingdao_1=link_qingdao_1[1].get_text()
            
            link_qingdao_2=soup_qingdao.select('.u_list li span')
            result_qingdao_2=link_qingdao_2[16].get_text()
            
            result_qingdao_final_time=re.sub('\s','',result_qingdao_time)
            result_qingdao_final_time=result_qingdao_final_time[7:]
            result_qingdao_final_1=re.sub('\s','',result_qingdao_1)
            result_qingdao_final_2=re.sub('\s','',result_qingdao_2)
            print(result_qingdao_final_time)
            print(result_qingdao_final_1)
            print(result_qingdao_final_2)
            print('qingdao houseprice has been collected_________')
            randomsleep86=random.randint(60,120)
            time.sleep(randomsleep86)

            #2针对网站未更新的情况
            if result_suzhou_final_1=='--' :
                result_suzhou_final_time='*'
                result_suzhou_final_1='*'
                result_suzhou_final_2='*'
            if result_wuhan_final_1=='--' :
                result_wuhan_final_1='*'
                result_wuhan_final_2='*'
            if result_chengdu_final_1=='--' :
                result_chengdu_final_1='*'
                result_chengdu_final_2='*'
            if result_hangzhou_final_1=='--' :
                result_hangzhou_final_1='*'
                result_hangzhou_final_2='*'
            if result_nanjing_final_1=='--' :
                result_nanjing_final_1='*'
                result_nanjing_final_2='*'
            if result_qingdao_final_1=='--' :
                result_qingdao_final_1='*'
                result_qingdao_final_2='*' 
       
            result8_1='【每日城市房价报道（2）】'+'\n'+result_suzhou_final_time+'\n'+'苏州：'+result_suzhou_final_1+'元/平'+'('+result_suzhou_final_2+')'+'\n'
            result8_2='武汉：'+result_wuhan_final_1+'元/平'+'('+result_wuhan_final_2+')'+'\n'
            result8_3='成都：'+result_chengdu_final_1+'元/平'+'('+result_chengdu_final_2+')'+'\n'
            result8_4='杭州：'+result_hangzhou_final_1+'元/平'+'('+result_hangzhou_final_2+')'+'\n'
            result8_5='南京：'+result_nanjing_final_1+'元/平'+'('+result_nanjing_final_2+')'+'\n'
            result8_6='青岛：'+result_qingdao_final_1+'元/平'+'('+result_qingdao_final_2+')'
            result8_final=result8_1+result8_2+result8_3+result8_4+result8_5+result8_6
            print(result8_final)
    
            fp=open('d:\\robot\\news8.txt','wb')
            fp.write(result8_final.encode('gb18030'))
            fp.close() 
            print('The 8th website has been done.——————————————————————————')
        except:
            print('There is a trouble with the 8th website.——————————————————————————')
            print('There is a trouble with the 8th website.——————————————————————————')
            print('There is a trouble with the 8th website.——————————————————————————') 

        #第3波城市房价
        try:
            #13 无锡
            url_wuxi='http://www.creprice.cn/market/wx/forsale/ALL/11.html'
            r_wuxi = requests.get(url_wuxi,allow_redirects=False)
            soup_wuxi = BeautifulSoup(r_wuxi.content,'lxml')
            link_wuxi_time=soup_wuxi.select('.utitle .up_time')
            result_wuxi_time=link_wuxi_time[0].get_text()
            
            link_wuxi_1=soup_wuxi.select('.u_list li .value')
            result_wuxi_1=link_wuxi_1[1].get_text()
            
            link_wuxi_2=soup_wuxi.select('.u_list li span')
            result_wuxi_2=link_wuxi_2[16].get_text()
            
            result_wuxi_final_time=re.sub('\s','',result_wuxi_time)
            result_wuxi_final_time=result_wuxi_final_time[7:]
            result_wuxi_final_1=re.sub('\s','',result_wuxi_1)
            result_wuxi_final_2=re.sub('\s','',result_wuxi_2)
            print(result_wuxi_final_time)
            print(result_wuxi_final_1)
            print(result_wuxi_final_2)
            print('wuxi houseprice has been collected_________')
            randomsleep91=random.randint(60,120)
            time.sleep(randomsleep91)
            
            #14 长沙
            url_changsha='http://www.creprice.cn/market/cs/forsale/ALL/11.html'
            r_changsha = requests.get(url_changsha,allow_redirects=False)
            soup_changsha = BeautifulSoup(r_changsha.content,'lxml')
            link_changsha_time=soup_changsha.select('.utitle .up_time')
            result_changsha_time=link_changsha_time[0].get_text()
            
            link_changsha_1=soup_changsha.select('.u_list li .value')
            result_changsha_1=link_changsha_1[1].get_text()
            
            link_changsha_2=soup_changsha.select('.u_list li span')
            result_changsha_2=link_changsha_2[16].get_text()
            
            result_changsha_final_time=re.sub('\s','',result_changsha_time)
            result_changsha_final_time=result_changsha_final_time[7:]
            result_changsha_final_1=re.sub('\s','',result_changsha_1)
            result_changsha_final_2=re.sub('\s','',result_changsha_2)
            print(result_changsha_final_time)
            print(result_changsha_final_1)
            print(result_changsha_final_2)
            print('changsha houseprice has been collected_________')
            randomsleep92=random.randint(60,120)
            time.sleep(randomsleep92)
            
            #15 宁波
            url_ningbo='http://www.creprice.cn/market/nb/forsale/ALL/11.html'
            r_ningbo = requests.get(url_ningbo,allow_redirects=False)
            soup_ningbo = BeautifulSoup(r_ningbo.content,'lxml')
            link_ningbo_time=soup_ningbo.select('.utitle .up_time')
            result_ningbo_time=link_ningbo_time[0].get_text()
            
            link_ningbo_1=soup_ningbo.select('.u_list li .value')
            result_ningbo_1=link_ningbo_1[1].get_text()
            
            link_ningbo_2=soup_ningbo.select('.u_list li span')
            result_ningbo_2=link_ningbo_2[16].get_text()
            
            result_ningbo_final_time=re.sub('\s','',result_ningbo_time)
            result_ningbo_final_time=result_ningbo_final_time[7:]
            result_ningbo_final_1=re.sub('\s','',result_ningbo_1)
            result_ningbo_final_2=re.sub('\s','',result_ningbo_2)
            print(result_ningbo_final_time)
            print(result_ningbo_final_1)
            print(result_ningbo_final_2)
            print('ningbo houseprice has been collected_________')
            randomsleep93=random.randint(60,120)
            time.sleep(randomsleep93)
            
            #16 沈阳
            url_shenyang='http://www.creprice.cn/market/sy/forsale/ALL/11.html'
            r_shenyang = requests.get(url_shenyang,allow_redirects=False)
            soup_shenyang = BeautifulSoup(r_shenyang.content,'lxml')
            link_shenyang_time=soup_shenyang.select('.utitle .up_time')
            result_shenyang_time=link_shenyang_time[0].get_text()
            
            link_shenyang_1=soup_shenyang.select('.u_list li .value')
            result_shenyang_1=link_shenyang_1[1].get_text()
            
            link_shenyang_2=soup_shenyang.select('.u_list li span')
            result_shenyang_2=link_shenyang_2[16].get_text()
            
            result_shenyang_final_time=re.sub('\s','',result_shenyang_time)
            result_shenyang_final_time=result_shenyang_final_time[7:]
            result_shenyang_final_1=re.sub('\s','',result_shenyang_1)
            result_shenyang_final_2=re.sub('\s','',result_shenyang_2)
            print(result_shenyang_final_time)
            print(result_shenyang_final_1)
            print(result_shenyang_final_2)
            print('shenyang houseprice has been collected_________')
            randomsleep94=random.randint(60,120)
            time.sleep(randomsleep94)
            
            #17 长春
            url_changchun='http://www.creprice.cn/market/cc/forsale/ALL/11.html'
            r_changchun = requests.get(url_changchun,allow_redirects=False)
            soup_changchun = BeautifulSoup(r_changchun.content,'lxml')
            link_changchun_time=soup_changchun.select('.utitle .up_time')
            result_changchun_time=link_changchun_time[0].get_text()
            
            link_changchun_1=soup_changchun.select('.u_list li .value')
            result_changchun_1=link_changchun_1[1].get_text()
            
            link_changchun_2=soup_changchun.select('.u_list li span')
            result_changchun_2=link_changchun_2[16].get_text()
            
            result_changchun_final_time=re.sub('\s','',result_changchun_time)
            result_changchun_final_time=result_changchun_final_time[7:]
            result_changchun_final_1=re.sub('\s','',result_changchun_1)
            result_changchun_final_2=re.sub('\s','',result_changchun_2)
            print(result_changchun_final_time)
            print(result_changchun_final_1)
            print(result_changchun_final_2)
            print('changchun houseprice has been collected_________')
            randomsleep95=random.randint(60,120)
            time.sleep(randomsleep95)
            
            #18 厦门
            url_xiamen='http://www.creprice.cn/market/xm/forsale/ALL/11.html'
            r_xiamen = requests.get(url_xiamen,allow_redirects=False)
            soup_xiamen = BeautifulSoup(r_xiamen.content,'lxml')
            link_xiamen_time=soup_xiamen.select('.utitle .up_time')
            result_xiamen_time=link_xiamen_time[0].get_text()
            
            link_xiamen_1=soup_xiamen.select('.u_list li .value')
            result_xiamen_1=link_xiamen_1[1].get_text()
            
            link_xiamen_2=soup_xiamen.select('.u_list li span')
            result_xiamen_2=link_xiamen_2[16].get_text()
            
            result_xiamen_final_time=re.sub('\s','',result_xiamen_time)
            result_xiamen_final_time=result_xiamen_final_time[7:]
            result_xiamen_final_1=re.sub('\s','',result_xiamen_1)
            result_xiamen_final_2=re.sub('\s','',result_xiamen_2)
            print(result_xiamen_final_time)
            print(result_xiamen_final_1)
            print(result_xiamen_final_2)
            print('xiamen houseprice has been collected_________')
            randomsleep96=random.randint(60,120)
            time.sleep(randomsleep96)

            #3针对网站未更新的情况
            if result_wuxi_final_1=='--' :
                result_wuxi_final_time='*'
                result_wuxi_final_1='*'
                result_wuxi_final_2='*'
            if result_changsha_final_1=='--' :
                result_changsha_final_1='*'
                result_changsha_final_2='*'
            if result_ningbo_final_1=='--' :
                result_ningbo_final_1='*'
                result_ningbo_final_2='*'
            if result_shenyang_final_1=='--' :
                result_shenyang_final_1='*'
                result_shenyang_final_2='*'
            if result_changchun_final_1=='--' :
                result_changchun_final_1='*'
                result_changchun_final_2='*'
            if result_xiamen_final_1=='--' :
                result_xiamen_final_1='*'
                result_xiamen_final_2='*' 
        
            result9_1='【每日城市房价报道（3）】'+'\n'+result_wuxi_final_time+'\n'+'无锡：'+result_wuxi_final_1+'元/平'+'('+result_wuxi_final_2+')'+'\n'
            result9_2='长沙：'+result_changsha_final_1+'元/平'+'('+result_changsha_final_2+')'+'\n'
            result9_3='宁波：'+result_ningbo_final_1+'元/平'+'('+result_ningbo_final_2+')'+'\n'
            result9_4='沈阳：'+result_shenyang_final_1+'元/平'+'('+result_shenyang_final_2+')'+'\n'
            result9_5='长春：'+result_changchun_final_1+'元/平'+'('+result_changchun_final_2+')'+'\n'
            result9_6='厦门：'+result_xiamen_final_1+'元/平'+'('+result_xiamen_final_2+')'
            result9_final=result9_1+result9_2+result9_3+result9_4+result9_5+result9_6
            print(result9_final)
    
            fp=open('d:\\robot\\news9.txt','wb')
            fp.write(result9_final.encode('gb18030'))
            fp.close() 
            print('The 9th website has been done.——————————————————————————')
        except:
            print('There is a trouble with the 9th website.——————————————————————————')
            print('There is a trouble with the 9th website.——————————————————————————')
            print('There is a trouble with the 9th website.——————————————————————————')         
        
        #第4波城市房价
        try:       
            #19 西安
            url_xian='http://www.creprice.cn/market/xa/forsale/ALL/11.html'
            r_xian = requests.get(url_xian,allow_redirects=False)
            soup_xian = BeautifulSoup(r_xian.content,'lxml')
            link_xian_time=soup_xian.select('.utitle .up_time')
            result_xian_time=link_xian_time[0].get_text()
            
            link_xian_1=soup_xian.select('.u_list li .value')
            result_xian_1=link_xian_1[1].get_text()
            
            link_xian_2=soup_xian.select('.u_list li span')
            result_xian_2=link_xian_2[15].get_text()
            
            result_xian_final_time=re.sub('\s','',result_xian_time)
            result_xian_final_time=result_xian_final_time[7:]
            result_xian_final_1=re.sub('\s','',result_xian_1)
            result_xian_final_2=re.sub('\s','',result_xian_2)
            print(result_xian_final_time)
            print(result_xian_final_1)
            print(result_xian_final_2)
            print('xian houseprice has been collected_________')
            randomsleep101=random.randint(60,120)
            time.sleep(randomsleep101)
            
            #20 太原
            url_taiyuan='http://www.creprice.cn/market/ty/forsale/ALL/11.html'
            r_taiyuan = requests.get(url_taiyuan,allow_redirects=False)
            soup_taiyuan = BeautifulSoup(r_taiyuan.content,'lxml')
            link_taiyuan_time=soup_taiyuan.select('.utitle .up_time')
            result_taiyuan_time=link_taiyuan_time[0].get_text()
            
            link_taiyuan_1=soup_taiyuan.select('.u_list li .value')
            result_taiyuan_1=link_taiyuan_1[1].get_text()
            
            link_taiyuan_2=soup_taiyuan.select('.u_list li span')
            result_taiyuan_2=link_taiyuan_2[16].get_text()
            
            result_taiyuan_final_time=re.sub('\s','',result_taiyuan_time)
            result_taiyuan_final_time=result_taiyuan_final_time[7:]
            result_taiyuan_final_1=re.sub('\s','',result_taiyuan_1)
            result_taiyuan_final_2=re.sub('\s','',result_taiyuan_2)
            print(result_taiyuan_final_time)
            print(result_taiyuan_final_1)
            print(result_taiyuan_final_2)
            print('taiyuan houseprice has been collected_________')
            randomsleep102=random.randint(60,120)
            time.sleep(randomsleep102)
            
            #21 南昌
            url_nanchang='http://www.creprice.cn/market/nc/forsale/ALL/11.html'
            r_nanchang = requests.get(url_nanchang,allow_redirects=False)
            soup_nanchang = BeautifulSoup(r_nanchang.content,'lxml')
            link_nanchang_time=soup_nanchang.select('.utitle .up_time')
            result_nanchang_time=link_nanchang_time[0].get_text()
            
            link_nanchang_1=soup_nanchang.select('.u_list li .value')
            result_nanchang_1=link_nanchang_1[1].get_text()
            
            link_nanchang_2=soup_nanchang.select('.u_list li span')
            result_nanchang_2=link_nanchang_2[16].get_text()
            
            result_nanchang_final_time=re.sub('\s','',result_nanchang_time)
            result_nanchang_final_time=result_nanchang_final_time[7:]
            result_nanchang_final_1=re.sub('\s','',result_nanchang_1)
            result_nanchang_final_2=re.sub('\s','',result_nanchang_2)
            print(result_nanchang_final_time)
            print(result_nanchang_final_1)
            print(result_nanchang_final_2)
            print('nanchang houseprice has been collected_________')
            randomsleep103=random.randint(60,120)
            time.sleep(randomsleep103)
            
            #22 海口
            url_haikou='http://www.creprice.cn/market/hk/forsale/ALL/11.html'
            r_haikou = requests.get(url_haikou,allow_redirects=False)
            soup_haikou = BeautifulSoup(r_haikou.content,'lxml')
            link_haikou_time=soup_haikou.select('.utitle .up_time')
            result_haikou_time=link_haikou_time[0].get_text()
            
            link_haikou_1=soup_haikou.select('.u_list li .value')
            result_haikou_1=link_haikou_1[1].get_text()
            
            link_haikou_2=soup_haikou.select('.u_list li span')
            result_haikou_2=link_haikou_2[15].get_text()
            
            result_haikou_final_time=re.sub('\s','',result_haikou_time)
            result_haikou_final_time=result_haikou_final_time[7:]
            result_haikou_final_1=re.sub('\s','',result_haikou_1)
            result_haikou_final_2=re.sub('\s','',result_haikou_2)
            print(result_haikou_final_time)
            print(result_haikou_final_1)
            print(result_haikou_final_2)
            print('haikou houseprice has been collected_________')
            randomsleep104=random.randint(60,120)
            time.sleep(randomsleep104)
            
            #23 昆明
            url_kunming='http://www.creprice.cn/market/km/forsale/ALL/11.html'
            r_kunming = requests.get(url_kunming,allow_redirects=False)
            soup_kunming = BeautifulSoup(r_kunming.content,'lxml')
            link_kunming_time=soup_kunming.select('.utitle .up_time')
            result_kunming_time=link_kunming_time[0].get_text()
            
            link_kunming_1=soup_kunming.select('.u_list li .value')
            result_kunming_1=link_kunming_1[1].get_text()
            
            link_kunming_2=soup_kunming.select('.u_list li span')
            result_kunming_2=link_kunming_2[16].get_text()
            
            result_kunming_final_time=re.sub('\s','',result_kunming_time)
            result_kunming_final_time=result_kunming_final_time[7:]
            result_kunming_final_1=re.sub('\s','',result_kunming_1)
            result_kunming_final_2=re.sub('\s','',result_kunming_2)
            print(result_kunming_final_time)
            print(result_kunming_final_1)
            print(result_kunming_final_2)
            print('kunming houseprice has been collected_________')
            randomsleep105=random.randint(60,120)
            time.sleep(randomsleep105)
            
            #24 南宁
            url_nanning='http://www.creprice.cn/market/nn/forsale/ALL/11.html'
            r_nanning = requests.get(url_nanning,allow_redirects=False)
            soup_nanning = BeautifulSoup(r_nanning.content,'lxml')
            link_nanning_time=soup_nanning.select('.utitle .up_time')
            result_nanning_time=link_nanning_time[0].get_text()
            
            link_nanning_1=soup_nanning.select('.u_list li .value')
            result_nanning_1=link_nanning_1[1].get_text()
            
            link_nanning_2=soup_nanning.select('.u_list li span')
            result_nanning_2=link_nanning_2[16].get_text()
            
            result_nanning_final_time=re.sub('\s','',result_nanning_time)
            result_nanning_final_time=result_nanning_final_time[7:]
            result_nanning_final_1=re.sub('\s','',result_nanning_1)
            result_nanning_final_2=re.sub('\s','',result_nanning_2)
            print(result_nanning_final_time)
            print(result_nanning_final_1)
            print(result_nanning_final_2)
            print('nanning houseprice has been collected_________')
            randomsleep106=random.randint(60,120)
            time.sleep(randomsleep106)       

            #4针对网站未更新的情况
            if result_xian_final_1=='--' :
                result_xian_final_time='*'
                result_xian_final_1='*'
                result_xian_final_2='*'
            if result_taiyuan_final_1=='--' :
                result_taiyuan_final_1='*'
                result_taiyuan_final_2='*'
            if result_nanchang_final_1=='--' :
                result_nanchang_final_1='*'
                result_nanchang_final_2='*'
            if result_haikou_final_1=='--' :
                result_haikou_final_1='*'
                result_haikou_final_2='*'
            if result_kunming_final_1=='--' :
                result_kunming_final_1='*'
                result_kunming_final_2='*'
            if result_nanning_final_1=='--' :
                result_nanning_final_1='*'
                result_nanning_final_2='*' 
      
            result10_1='【每日城市房价报道（4）】'+'\n'+result_xian_final_time+'\n'+'西安：'+result_xian_final_1+'元/平'+'('+result_xian_final_2+')'+'\n'
            result10_2='太原：'+result_taiyuan_final_1+'元/平'+'('+result_taiyuan_final_2+')'+'\n'
            result10_3='南昌：'+result_nanchang_final_1+'元/平'+'('+result_nanchang_final_2+')'+'\n'
            result10_4='海口：'+result_haikou_final_1+'元/平'+'('+result_haikou_final_2+')'+'\n'
            result10_5='昆明：'+result_kunming_final_1+'元/平'+'('+result_kunming_final_2+')'+'\n'
            result10_6='南宁：'+result_nanning_final_1+'元/平'+'('+result_nanning_final_2+')'
            result10_final=result10_1+result10_2+result10_3+result10_4+result10_5+result10_6
            print(result10_final)
    
            fp=open('d:\\robot\\news10.txt','wb')
            fp.write(result10_final.encode('gb18030'))
            fp.close() 
            print('The 10th website has been done.——————————————————————————')
        except:
            print('There is a trouble with the 10th website.——————————————————————————')
            print('There is a trouble with the 10th website.——————————————————————————')
            print('There is a trouble with the 10th website.——————————————————————————')          
        
        
        
