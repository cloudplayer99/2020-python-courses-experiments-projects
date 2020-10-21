import requests
import re

if __name__ == '__main__':

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    URL = 'https://jdxy.cumtb.edu.cn/info/'
    num = 1012
    NUM = 1000
    T = 0
    Max = 2000
    while True:
        url = URL + str(num) + '/' + str(NUM) + '.htm'
        html = requests.get(url, headers)
        html.encoding = 'utf-8'
        my_html = html.text
        # with open("E:\\爬虫实验\\Data\\" + "example_" + str(num) + str(NUM) + ".txt", 'w', encoding='utf-8') as f:
        #     f.write(my_html)
        # print(my_html)
        jdxy_cumtb = 'https://jdxy.cumtb.edu.cn'
        pic_1 = 'img src="(/__local.+?)"'
        pic_2 = 'src="(/__local.+?)"'
        find_1 = re.findall(pic_1, my_html)
        if find_1:
            find_str = find_1[0]
        else:
            find_2 = re.findall(pic_2, my_html)
            if find_2:
                find_str = find_2[0]
            else:
                NUM += 1
                T += 1
                print("第 {} 次搜索，搜索失败".format(T))
                if T >= Max:
                    break
                continue
        my_find = jdxy_cumtb + find_str
        # print(my_find)
        with open("E:\\爬虫实验\\Data\\" + "example_" + str(num) + str(NUM) + ".txt", 'w', encoding='utf-8') as f:
            f.write(my_html)
        if my_find[-4:] == ".pdf":
            pdf = requests.get(my_find, headers).content
            with open("E:\\爬虫实验\\Data\\" + str(num) + str(NUM) + '.pdf', 'wb') as f:
                f.write(pdf)
        else:
            jpg = requests.get(my_find, headers).content
            with open("E:\\爬虫实验\\Data\\" + str(num) + str(NUM) + '.jpg', 'wb') as f:
                f.write(jpg)
        NUM += 1
        T += 1
        print("第 {} 次搜索，搜索成功".format(T))
        if T >= Max:
            break

    # img src="/__local/E/A1/1E/25FAF24FA4F8D62CFFF5E52F5E7_6453BDD1_3C29.jpg"
    # img src="/__local/1/D8/75/C9787E4B3A79D5F1C4E13D0DE8F_338F38FE_229B8.jpg"
    # src="/__local/B/91/E5/31512AD08F7A1B9F6DA17F79482_9C954063_9E5E6.jpg"
    # src = "/__local/C/02/16/E9C736790E6D27D212CC9123948_9C03BC75_53D4E.pdf?e=.pdf"
