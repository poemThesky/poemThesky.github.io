 <?php
    show_source(__FILE__);
    class test{
    public $test;
    function __wakeup(){
        $fp = fopen("shell.php","w") ;
        fwrite($fp,$this->test);
        fclose($fp);
        }
    }
    $class2 = $_GET['ser'];
    print_r($class2);
    echo "</br>";
    $class2_unser = unserialize($class2);
    @require "shell.php";
?> 