1.编译
    g++ -g  test.c -o test  (-g生成调试信息)
2.调试
    gdb test
3.设置断点
    break/b lineNumber
4.运行
    run/r
5.继续运行(到下一个断点或程序结束)
    continue/c
6.单步进入
     next/n(当遇到用户自定义的函数的时候不会进入函数)
     step/s(当遇到用户自定义的函数的时候会进入函数)
7.设定变量的值
     set varible=value;
8.查看变量的值
     print/p varible

    
