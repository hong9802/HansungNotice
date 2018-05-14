from bs4 import BeautifulSoup
import re
import requests
import subprocess

def parshing() :
    r = requests.get('http://hansung.ac.kr/web/www/cmty_01_01')
    soup = BeautifulSoup(r.text, "html.parser")
    mr = soup.find("table", class_="bbs-list")
    first = mr.find_all("td", class_="subject")
    result = first[0].find('a')
    strchange = str(result)
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', strchange)
    return cleantext

f = open("hansung.txt", 'r+')
line = f.read()
if(line == '') :
    print("초기 Data 구축중...")
    result = parshing()
    f.write(result)
    f.close()
else :
    print("비교 시작...")
    result = parshing()
    if(line == result) :
        f.close()
        pass
    else :
        f.close()
        f = open("hansung.txt", 'w')
        subprocess.Popen(['notify-send', "새로운 한성공지가 나왔어"])
        f.write(result)
        f.close()