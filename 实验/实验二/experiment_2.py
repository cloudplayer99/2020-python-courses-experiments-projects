import time
import requests
import re

url = 'http://www.whalebj.com/xzjc/default.aspx?tdsourcetag=s_pctim_aiomsg'
# print(str_html.content)
# re_str = r'[0-9]{4}.[0-9]{2}.[0-9]{2}\s[0-9]{2}.[0-9]{2}.[0-9]{2}'
while True:
    str_html = requests.get(url)
    findall1 = re.findall(r'\d{4}.\d{2}.\d{2}\s\d{2}.\d{2}.\d{2}', str_html.text)
    findall2 = re.findall(r'：\d{2,3}', str_html.text)
    # findall2 = re.findall(r'：(\d{2,3})', str_html.text)
    dict1 = {}
    findall = []
    for i in range(3):
        findall.append(re.sub('：', '', findall2[i]))
    dict1[findall1[0]] = findall
    print(dict1)
    time.sleep(60)

# 2020-10-09 14:05:48
# 238
# 91
# 92
