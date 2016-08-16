# Python-tools
目标是Python小工具集，多了以后整合成网页版

| 编号 | 名字 | 用途 | 版本 | TODO |
|------| ---- |------| -----|------|
|1| [Get-SS-Password-by-Python](https://github.com/Jirachiii/Get-SS-Password-by-Python)| 半自动获取ss的密码 |V1.0 |更智能点|
|2| HTML转js| 页面用js拼接生成时的转换 |V1.0 |----|

##2、HTML转js

更新日志:
-20160816:采用文本框复制形式，不需要打开文件了


----------
exe分为缩进版和不缩进版，以下为缩进版效果：
```HTML
<div class="red" id='123' onclick="do()">
	<h1>"哈哈"</h1>
	<a href="1" title="123"></a>
</div>
```
to
```JS
str+="<div class=\"red\" id=\"123\" onclick=\"do()\">";
str+="	<h1>\"哈哈\"</h1>";
str+="	<a href=\"1\" title=\"123\"></a>";
str+="</div>";
```
