<?php
	show_source(__FILE__);
	$KEY = "test";
	$str = $_GET['str'];
	if (unserialize($str) === "$KEY")
	{
		eval('phpinfo();');
	}
	else 
		echo 'try it again';
?>