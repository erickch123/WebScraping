#from bs4 import BeautifulSoup

#with open('######','r') as filename: ##read the file only makanya ada r di second argument
 #   content = filename.read()
  #  print

   # soup = BeautifulSoup(content, 'lxml') ## what is lxml for
    #prettify buat mempercantik
    #soup.find('sadsds') buat yg pertama doang, sama soup.find_all beda bos
    # for course in courses, print (course.text)biar gada h5 h5 nya
    #class_= < perlu karena class is a built in keywordk in python
    # sometimes jg course.h5.text sama course.a.test
    # print(f'{course_name} costs {course_price}') <<< what the hell f means


from bs4 import BeautifulSoup
import requests
import time
import csv

print('skill you dont have')
unfamiliar = input('>')
print('Filtering out')

link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#### dot text penting bet kalo ga soup nya ga kerja gatau napa, tapi kalo sblm itu coba print link dengan dot text bakal panjang bet
print(link)
soup = BeautifulSoup(link, 'lxml')
#unfamiliar_skill = 'java'
#print(unfamiliar_skill)
#print(f'filtering out  {unfamiliar_skill}') ### gw gatau gimana caranya biar gausa pake f'



##### next is the saving to excel
##### pake with open pas input skills yg gabisa, tepatny di bawah if unfamiliarskill not in skill
###### enumerate(jobs) >>>>> ini buat urutin alphabet
  

# class_ biar g bentrok ma python pny class

file = open('jobsearch.csv', 'wb')
writer = csv.writer(file)


job = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
for jobs in enumerate(job):
    date = jobs.find('span', class_= 'sim-posted').span.text #### ini span text ajaib anjg ilangin span diatasnny tp g ngerti
    if 'few' in date:
        company = jobs.find('h3', class_ = 'joblist-comp-name').text ## ' 'kalo replace ya yg kanan replace yg kiri, kalo g pake class_ nanti h3nya bakal keliata
        skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','') ### kalo ini harus pake text , tp yg atas gatau knp kg
        more_info = jobs.header.h2.a['href'] # the heck napa bs header doang
        company = company.strip()
        skills = skills.strip()
        if unfamiliar not in skills:
            #with open(f'posts/{index}.txt','w') as f:
            print(company)
            print(more_info)
            print(f"Company Name: {company} ")
            print(f"Required Skills: {skills}")### pake company.strip() biar rapi
            
            writer.writerow([company.encode('utf-8'), skills.encode('utf-8'), more_info.encode('utf-8')])

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        time.sleep(600)


