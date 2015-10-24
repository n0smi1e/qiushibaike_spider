import urllib.request
import urllib.parse
import http.cookiejar
import re
#获取cookie
#cookie = http.cookiejar.CookieJar()
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#response = opener.open('http://www.123.com')
#for item in cookie:
#    print('Name = '+item.name)
#    print('Value = '+item.value)

#获得输入


#header验证
page = 1
url = 'http://www.qiushibaike.com/text/page/' + str(page)
user_agent = 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
headers = { 'User-Agent' : user_agent }


#获取网页数据
req = urllib.request.Request(url, None, headers)

try:
    res = urllib.request.urlopen(req)
except urllib.request.HTTPError as e:
    print(e.code)
except urllib.request.URLError as e:
    print(e.reason)
else:
    print("OK")


#正则匹配
content = res.read().decode('utf-8')
pattern = re.compile('<div class="article block untagged mb15" id=\'.*?\'>\n\n<div class="author">\n<a href=.*?" target="_blank">\n<img src=".*?" />\n.*?\n</a>\n</div>\n\n\n<div class="content">\n\n.*?\n<!--.*?-->\n\n</div>', re.S)
content_temp = re.findall(pattern,content)
#print(content_temp)


#函数 Regular是正则，conten_1,2是要处理的list，item_number处理后的list
def handle(Regular, which, content_1 = content_temp):
    
    pattern_temp = re.compile(Regular, re.S)
    pattern_temp2 = re.compile('\d+', re.S)
#    pattern_temp3 = re.compile('^[\u0391-\uFFE5].*[\u0391-\uFFE5]$', re.S)
    
    content_2 = []
    item = []
    sentence_temp = []

    
    if which == 'num' or which == 'author':
        for s in range(len(content_1)):
            content_2.append(re.findall(pattern_temp, content_1[s]))
#       print(content_2)


        for s1 in range(len(content_2)):
            item.append(re.findall(pattern_temp2, str(content_2[s1]))) 
#       print(item)

    elif which == 'sentence':
        for s2 in range(len(content_1)):
            content_2.append(re.findall(pattern_temp, content_1[s2]))
#        print(content_2[4])

        for s3 in range(len(content_2)):
            content_3 = list(str(content_2[s3]))
            content_3_1 = content_3[27:]
            content_3_2 = content_3_1[:-31]
            str_temp = "".join(content_3_2)
            item.append(str_temp)
#        print(sentence_temp[3])

    
    return item
    

#段子编号  item_number
sentence_num = handle('qiushi_tag_\d*', 'num')
    
#作者编号
author = handle('/users/\d*', 'author')

#段子
sentence = handle('<div class="content">\n\n.*?\n.*?\n\n</div>', 'sentence')


#print(sentence_num, author, sentence)

for i in range(len(content_temp)):
    print('    段子编号', sentence_num[i],'作者编号', author[i])
    print('    ',sentence[i])
    print()
