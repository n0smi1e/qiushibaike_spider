__author__ = "n0smi1e"

import urllib.request
import urllib.parse
import http.cookiejar
import re


#header
page = 1
url = 'http://www.qiushibaike.com/text/page/' + str(page)
user_agent = 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
headers = { 'User-Agent' : user_agent }


#获取网页源码
req = urllib.request.Request(url, None, headers)


#容错
try:
    res = urllib.request.urlopen(req)
except urllib.request.HTTPError as e:
    print(e.code)
except urllib.request.URLError as e:
    print(e.reason)
else:
    #print("OK")
    pass



#正则匹配
end = []
#获取源代码
content = res.read().decode('utf-8')
#正则表达式
pattern = re.compile('<div class="article block untagged mb15" id=\'qiushi_tag_\d+\'>\s\s<div class="author clearfix">\s<a href="/users/\d+?" target="_blank" rel="nofollow">\s<img src=".*?" alt=".*?/>\s</a>\s<a href="/users/\d+" target="_blank" title=".*?">\s<h2>.*?</h2>\s</a>\s</div>\s\s\s<div class="content">\s\s.*?\s<!--\d+-->', re.S)
pattern_1 = re.compile('<div class="article block untagged mb15" id=\'qiushi_tag_(\d+)\'>\s\s<div class="author clearfix">\s<a href="/users/(\d+?)" target="_blank" rel="nofollow">\s<img src=".*?" alt=".*?/>\s</a>\s<a href="/users/\d+" target="_blank" title=".*?">\s<h2>(.*?)</h2>\s</a>\s</div>\s\s\s<div class="content">\s\s(.*?)\s<!--\d+-->', re.S)
pattern_2 = re.compile('((<br/>)|\s)*')
#获取段子代码模块
content_temp = re.findall(pattern, content)
#获取段子编号，作者编号，作者名称，段子内容。每一个段子的所有数据为一个tuple
for i in range(len(content_temp)):
    content_temp_1 = re.search(pattern_1, content_temp[i])
    end.append(list(content_temp_1.group(1,2,3,4)))
#处理<br/>和空格
    end[i][3] = re.sub(pattern_2, "", content_temp_1.group(4))
#print(end)



#简单整理输出
for n in range(len(end)):
    print("——————————————————————————————————————————————————————————————————————————————")
    print('    段子编号：', end[n][0],'作者编号：', end[n][1])
    print('    作者：', end[n][2])
    print('    段子：', end[n][3])
    print()


