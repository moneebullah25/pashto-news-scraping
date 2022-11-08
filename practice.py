import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
choice = 'y'
unfam_skills = []
while (choice == 'y'):
    unfam_skills.append(input("Enter Skills you are not familiar with : "))
    choice = input("Do you want to enter more skills you are not fimiliar with (y/n) : ")
tim = input("Look for ads posted days ago : ")
print("Searching Data for you")
def check_array(arr1, arr2):
    result = True
    for y in range(0, len(arr1)):
        if arr1[y] in arr2.split(","):
            result = False
            break
    return result

def string(company):
    company = company.split()
    text = ""
    for x in company:
        text = text + x + ' '
    return text[:-1]

def find_jobs():
    global index
    titles = []
    comps = []
    skills = []
    posts = []

    URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=Pakistan"
    html = urllib.request.urlopen(URL)
    soup = BeautifulSoup(html, "lxml")
    li_tags = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    skill_tags = soup.find_all("span", class_="srp-skills")
    posted_tags = soup.find_all("span", class_="sim-posted") 
    for x in range(0, len(li_tags)):
        title = string(li_tags[x].header.h2.a.text)
        comp = string(li_tags[x].header.h3.text)
        skill = string(skill_tags[x].text.replace(" ", ""))
        post = posted_tags[x].text.split()[1]
        res = check_array(unfam_skills, skill)
        if res == True:
            try:
                post = int(post)
            except:
                post = 0
            if int(post) < int(tim):

                titles.append(title)
                comps.append(comp)
                skills.append(skills)
                posts.append(post)

                #with open(f'posts/{index}.txt', 'w') as f:
                #	f.write(f'''\n\nJob Title  :  {title}\nCompany  :  {comp}\nSkills Required  :  {skill}\nPosted : {str(post)} days ago\n\n''')
                #	index += 1
                #print(f'''\n\nJob Title  :  {title}\nCompany  :  {comp}\nSkills Required  :  {skill}\nPosted : {str(post)} days ago\n\n''')
                #print(titles, comps, skills, posts)
                
    return titles, comps, skills, posts
    
index = 0
while True:
    titles, comps, skills, posts = find_jobs()
    print(titles, comps, skills, posts)
    df = pd.DataFrame({'Job Title': np.array(titles), 'Company' : np.array(comps), 'Skills': np.array(skills), 'Posted Days ago': np.array(posts)})
    df.to_csv('output.csv')
    print("Completed")
'''
    print(df)
    time_wait = 10
    print("Waiting {0} minutes".format(time_wait))
    time.sleep(60*time_wait)
'''
