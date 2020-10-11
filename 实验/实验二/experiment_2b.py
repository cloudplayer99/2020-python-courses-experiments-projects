import requests
import re
import os

if __name__ == '__main__':

    # https://jdxy.cumtb.edu.cn/szdw/zjzcjs.htm
    # https://jdxy.cumtb.edu.cn/szdw/fgzcjs.htm
    # https://jdxy.cumtb.edu.cn/szdw/zgzcjs.htm
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    URL = dict()
    URL['zjzc'] = 'https://jdxy.cumtb.edu.cn/szdw/zjzcjs.htm'
    URL['fgzc'] = 'https://jdxy.cumtb.edu.cn/szdw/fgzcjs.htm'
    URL['zgzc'] = 'https://jdxy.cumtb.edu.cn/szdw/zgzcjs.htm'
    url = "https://jdxy.cumtb.edu.cn"
    # print(URL)
    path = "E:\\爬虫实验\\Data_1a\\cumtb机电学院网页源码\\"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    dict_zjzc = dict()
    dict_fgzc = dict()
    dict_zgzc = dict()
    teacher_url_pattern = '<A href="..(/info/.+?)" target="_blank" title=".+?">'
    teacher_name_pattern = '<A href="../info/.+?" target="_blank" title="(.+?)">'
    # <A href="../info/1014/2207.htm" target="_blank" title="张鹏宁-讲师">
    # <A href="../../info/1014/1381.htm" target="_blank" title="蒋磊-讲师">
    teacher_url_pattern_next = '<A href="../..(/info/.+?)" target="_blank" title=".+?">'
    teacher_name_pattern_next = '<A href="../../info/.+?" target="_blank" title="(.+?)">'
    for key, value in URL.items():
        html = requests.get(value, headers)
        html.encoding = 'utf-8'
        my_html = html.text
        with open("E:\\爬虫实验\\Data_1a\\cumtb机电学院网页源码\\" + key + ".txt", 'w', encoding='utf-8') as f:
            f.write(my_html)
        find_url = re.findall(teacher_url_pattern, my_html)
        find_name = re.findall(teacher_name_pattern, my_html)
        # for i in range(len(find_name)):
        #     find_name[i] = re.sub(r"[\s\-]+", '', find_name[i])
        #     if key == 'zjzc':
        #         dict_zjzc[find_name[i]] = url + find_url[i]
        #     elif key == 'fgzc':
        #         dict_fgzc[find_name[i]] = url + find_url[i]
        #     elif key == 'zgzc':
        #         dict_zgzc[find_name[i]] = url + find_url[i]
    # print(find_url)
    # print(find_name)
    # print(dict_zjzc)
    # print(dict_fgzc)
    # print(dict_zgzc)
        next_page_pattern = '<a href="' + key + 'js/([1-2].htm)" class="Next">下页</a>'
        next_page_disable_pattern = '</a><span class="(NextDisabled)">下页</span>'
        next_page_pattern2 = '<a href="([1-2].htm)" class="Next">下页</a>'
        # <a href="zjzcjs/1.htm" class="Next">下页</a>
        # <span class="NextDisabled">下页</span>
        # <a href="1.htm" class="Next">下页</a>
        # https://jdxy.cumtb.edu.cn/szdw/
        jdxy = "https://jdxy.cumtb.edu.cn/szdw/" + key + "js/"
        while True:
            next_page_suffix = re.findall(next_page_pattern, my_html)
            if next_page_suffix:
                # print(next_page_suffix)
                pass
            else:
                next_page_suffix = re.findall(next_page_pattern2, my_html)
                if next_page_suffix:
                    # print(next_page_suffix)
                    pass
                else:
                    next_page_suffix = re.findall(next_page_disable_pattern, my_html)
                    # print(next_page_suffix)
                    # break
                    if next_page_suffix[0] == "NextDisabled":
                        for i in range(len(find_name)):
                            find_name[i] = re.sub(r"[\s\-]+", '', find_name[i])
                            if key == 'zjzc':
                                dict_zjzc[find_name[i]] = url + find_url[i]
                            elif key == 'fgzc':
                                dict_fgzc[find_name[i]] = url + find_url[i]
                            elif key == 'zgzc':
                                dict_zgzc[find_name[i]] = url + find_url[i]
                        break
            next_page = jdxy + next_page_suffix[0]
            # print(next_page)
            html_next = requests.get(next_page, headers)
            html_next.encoding = 'utf-8'
            my_html = html_next.text
            with open("E:\\爬虫实验\\Data_1a\\cumtb机电学院网页源码\\" + key + next_page_suffix[0][-5] + ".txt", 'w', encoding='utf-8') as f:
                f.write(my_html)
            find_url += re.findall(teacher_url_pattern_next, my_html)
            find_name += re.findall(teacher_name_pattern_next, my_html)
            # for i in range(len(find_name)):
            #     find_name[i] = re.sub(r"[\s\-]+", '', find_name[i])
            #     if key == 'zjzc':
            #         dict_zjzc[find_name[i]] = url + find_url[i]
            #     elif key == 'fgzc':
            #         dict_fgzc[find_name[i]] = url + find_url[i]
            #     elif key == 'zgzc':
            #         dict_zgzc[find_name[i]] = url + find_url[i]
    # print(len(dict_zjzc), dict_zjzc)
    # print(len(dict_fgzc), dict_fgzc)
    # print(len(dict_zgzc), dict_zgzc)
    dict_list = [dict_zjzc, dict_fgzc, dict_zgzc]
    pic_1 = 'img src="(/__local.+?)"'
    pic_2 = 'src="(/__local.+?)"'
    for d in dict_list:
        for key, value in d.items():
            T_html = requests.get(value, headers)
            T_html.encoding = 'utf-8'
            teacher_html = T_html.text
            teacher_path = "E:\\爬虫实验\\Data_1a\\" + key + "\\"
            is_Exists = os.path.exists(teacher_path)
            if not is_Exists:
                os.mkdir(teacher_path)
            find_1 = re.findall(pic_1, teacher_html)
            if find_1:
                find_str = url + find_1[0]
                # print(find_str)
            else:
                find_2 = re.findall(pic_2, teacher_html)
                if find_2:
                    find_str = url + find_2[0]
                    # print(find_str)
                else:
                    continue
            if find_str[-4:][0] != '.':
                find_str_suffix = '.' + find_str[-4:]
            else:
                find_str_suffix = find_str[-4:]
            file = requests.get(find_str, headers).content
            with open("E:\\爬虫实验\\Data_1a\\" + key + "\\" + key + find_str_suffix, 'wb') as f:
                f.write(file)
            # .jpg .gif .png .jpeg .pdf
            # 每个老师的照片放在以其名字命名的文件夹中


