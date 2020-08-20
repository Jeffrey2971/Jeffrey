@echo off&setlocal enabledelayedexpansion
:main
color 0c
if not exist %tmp%\~found md %tmp%\~found||(
cls&echo 文件夹创建失败，按任意键退出。&pause>nul&exit)
echo.>%tmp%\~found\~t.t||(
echo 目录不可用 [ %tmp%\~found\ ] &pause>nul&exit)
set "file=0"&set "s="&set "e="&set "t="&set "k="&set "n="&set "d="&set "y="
:return
set "num=%random%"
if exist %tmp%\~found\found_%num%.log (echo 发现同名文件[found_%num%.log]，正在更换，如长时间未能成功请清理文件夹 [%tmp%\~found] 。&title 发现同名文件[found_%num%.log]，正在更换可用文件。&cls&goto:return)
cls
title 全盘查找。
set "var="
echo.&echo.&echo.&echo.&echo.&echo.&echo.&echo.&echo.
call:_colstr 0f:"要查找的文件 [需添加文件扩展名，如查找同类文件可使用通配符]";\t
echo *.*
echo.
call:_colstr 0e:"禁止输入以下等特殊符号："
echo [ ^| / \^" ^< ^> ? : * ]
echo.
call:_colstr 08:"%num%";0a:"在这里输入需要查找的文件 [输入 /help 获取帮助]："
del /f /s /q %tmp%\~found\~tmp>nul 2>nul
set /p "var="

echo %var%|find /i "*." >nul && set "int=同类" || set "int=指定"
echo %var%|find /i " " >nul && (echo.&echo 值不能为空或输入的字符串内含有空格，输入 [ /help ] 获取帮助。&pause>nul&goto:main)
if "%var%"=="/del*" (goto:_delet) else (if "%var%"=="/help" (goto help) else (if "%var%"=="<" (goto:main) else (if "%var%"==">" (goto:main) else (if "%var%"=="|" (goto:main) else (if "%var%"=="*" (goto:main) else (if "%var%"==":" (goto:main) else (if "%var%"=="/" (goto:main) else (if "%var%"=="\" (goto:main) else (if "%var%"=="?" (goto:main) else (if "%var%"=="/exit" (exit)))))))))))
call:k
color 00
title 正在查找%var%中... ...
set "#time=:::::::::::::::::::: %date% / %time% Start ::::::::::::::::::::"
echo.
color 07&echo 正在全盘查找%int%文件 [ %var% ]，耗时可能较长请耐心等候
echo.
for %%a in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
if exist %%a:\ (
cd /d %%a:\
for /f "delims=" %%b in ('dir /s /a-d /b "%var%" 2^>nul') do (
set /a "file+=1"
if exist "%%b" (
echo %%~zb^|"%%b">>%tmp%\~found\data_%num%.log))))
>"%tmp%\t.t" echo;var list=WSH.StdIn.ReadAll().replace(/^^\s*^|\s*$/g,'').split(/[\r\n]+/);
>>"%tmp%\t.t" echo;list.sort(function(a,b){return Number(b.split('^|')[0])-Number(a.split('^|')[0])});
>>"%tmp%\t.t" echo;for(var i=0;i^<list.length;i++){var line=list[i].split('^|');WSH.echo('文件已找到，大小为['+getsize(Number(line[0]))+'] ['+line[1]+']');}
>>"%tmp%\t.t" echo;function getsize(s){var size='';if(s^>=1073741824){size = (s/1073741824).toFixed(2) + 'GB';}else if(s^>=1048576){size = (s/1048576).toFixed(2) + 'MB';}else if(s^>=1024){size = (s/1024).toFixed(2) + 'KB';}else {size = s + 'B';};return size;}
pushd %tmp%\~found
call:k
set/a D=D2-D1,K=K2-K1
if %K% leq 0 set/a K+=8640000,D-=1
if %D% leq 0 (set "s=%K%0毫秒")else set "s=%D%天%K%0毫秒"
call:writet&(
echo.
echo %#time%
echo.
echo 查找%int%文件 [ %var% ]，共找到 [ %file% ] 个文件，耗时 [ %s% ] 。
echo.
)>found_%num%.log
call:writet&type data_%num%.log|cscript -nologo -e:jscript "%tmp%\t.t">>found_%num%.log
call:writet&echo.>>found_%num%.log

call:writet&find "文件已找到" found_%num%.log >nul||(
echo 没有找到任何文件，输入 [ /help ] 获取帮助。
echo.
)>>found_%num%.log

call:writet&echo ::::::::::::::::::: %date% / %time% Finished :::::::::::::::::::>>found_%num%.log
title 共找到 [ %file% ] 个文件，耗时 [ %s% ] 已生成文本报告。
call:writet&type %tmp%\~found\found_%num%.log&color 0f
echo.
call:_colstr 0e:"正在拷贝路径至粘贴板，请稍后。";\n;&mshta vbscript:clipboarddata.setdata("text","%tmp%\~found\found_%num%.log")(close)
echo.
call:_colstr 查找完毕，共找到;\t;[;\t;0a:"%file%";\t;];\t;个文件，耗时;\t;[;\t;0a:"%s%";\t;];\t;0f:"已生成文本报告，位于：";\n;
echo.
call:_colstr 路径;\t;[ "%tmp%\~found\found_%num%.log" ];\t;0e:"已复制。";\n;
echo.&echo.
call:_colstr \t;\t;\t;\t;\t;\t;\t;\t;\t;\t;\t;\t;\t;\t;J;0b:"e";0e:"ff";0f:"r";0a:"e";0d:"y";06:"2";05:"9";04:"7";03:"1";f8:"@outlook.com";\t;\t;
echo.&echo.&pause>nul
call:_colstr 0e:"正在清理粘贴板，请稍后。";&mshta.exe "javascript:clipboardData.clearData();close();"
popd&goto:main
:help
title 帮助。
cls&echo.
call:_colstr 0e:"正在计算相关数据，请稍后。";\n;
set "cnt=0"&set "f="&set "d="
for /f "delims=" %%i in ('dir/b/a-d "%tmp%\~found\*.log" 2^>nul') do set /a "cnt+=1"
for /f "tokens=3 delims= " %%i in ('dir /s /a /-c "%tmp%\~found" ^|findstr 个文件') do (set f=%%i)
if %f% gtr 1024 (set /a "f>>=10"&set "d=KB"&set "cl=0a")
if %f% gtr 1024 (set /a "f>>=10"&set "d=MB"&set "cl=0e")
if %f% gtr 1024 (set /a "f>>=10"&set "d=GB"&set "cl=0c")
if not defined d (set "d=bytes"&set "cl=0a")
cls
echo.&echo.&echo.
call:_colstr 0e:"禁止输入以下等特殊符号："
echo [ ^| / \^" ^< ^> ? : * ]
echo.
call:_colstr 0f:"查找时输入尽量正确的";0e:"文件名";+;0e:"扩展名";0f:"如";0f:"[";0a:"文件.exe";0f:"]";\n;
echo.
call:_colstr 0f:"如需查找同类文件如图片" [ *.png/*.jpg ] ;0f:"可使用";0e:"通配符" 0f:"["; * ;0f:"]" . ;0f:"[" 文件扩展名 ;0f:"]";\n
echo.
call:_colstr 0f:"共找到";\t;0f:"[";\t;0a:"%cnt%";\t;0f:"]";\t;0f:"个报告文件，总大小约为";\t;0f:"[";\t;%cl%:"%f%%d%";\t;0f:"]";\t; ;0f:"如需删除可在界面输入";\t;/del*;\n
echo.
call:_colstr 0f:"文件大小参考";\t;0f:"[";\t;0a:"bytes---极小";\t;0f:"]";\t;0f:"[";\t;0a:"Kb---小";\t;0f:"]";\t;0f:"[";\t;0e:"Mb---较小";\t;0f:"]";\t;0f:"[";\t;0c:"Gb---较大";\t;0f:"]";\n
echo.
call:_colstr 0e:"正在拷贝路径至粘贴板，请稍后。";\n;&mshta vbscript:clipboarddata.setdata("text","%tmp%\~found")(close)
echo.
call:_colstr 0f:"文件记录位于";\t;0f:"[";\t;%tmp%\~found;\t;0f:"]";\t;0f:"格式为";\t;*.log;\t;0e:"已复制。";\n;
echo.&echo.
call:_colstr 0f:"如需额外帮助请联系邮箱：";J;0b:"e";0e:"ff";0f:"r";0a:"e";0d:"y";06:"2";05:"9";04:"7";03:"1";f8:"@outlook.com";\t;\t;\t;\t;0f:"联系微信：";J;0b:"e";0e:"ff";0f:"r";0a:"e";0d:"y";06:"2";05:"9";04:"7";03:"1";\n;
echo.&echo.&echo.&echo                                按任意键返回。&echo.
echo.&pause>nul
call:_colstr 0e:"正在清理粘贴板，请稍后。";\n;&echo.&mshta.exe "javascript:clipboardData.clearData();close();"
goto:main
rem /*--------- colstr 函数 -------------
rem /*\?"<:>|
:_colstr [^<colorcode^>:"<color str>"^|"<common str>"^|^<escape Char^>];... 
if not exist %tmp%\~found\~tmp md %tmp%\~found\~tmp||(
echo 文件夹创建失败，按任意键退出。&pause>nul&exit
)
pushd %tmp%\~found\~tmp 2>nul||(
echo 目录不可用 [ %tmp%\~found\~tmp\ ] &pause>nul&exit
)
for /f "tokens=1* delims=:" %%a in ("%~1")do (
  if %%a:%%b.==%%a:"%%~b". (set col=%%a
    for %%z in ("LBlue=9";"LGreen=A";"LAqua=B";"LRed=C";"LPurple=D";
                "LYellow=E";"LWhite=F";"Black=0";"Blue=1";"Green=2";
                "Aqua=3";"Red=4";"Purple=5";"Yellow=6";"White=7";"Gray=8";
               )do set col=!col:%%~z!
      if exist "%%~b?" del/a/q "%%~b?"2>nul
      set/p= <nul>"%%~b"2>nul&findstr/a:!col! .* "%%~b?"2>nul 3>&2
    ) else if %1==\n (echo.
    ) else if %1==\b (set/p=<nul
    ) else if %1==\q (set/p=""^"<nul
    ) else if %1==\t (set/p= <nul &rem 注意=后面不是空格，是制表符
    ) else (set/p"=%~1"<nul)
)&(if %2. neq . (shift&endlocal&popd&goto:_colstr))
rem ------------------------------------*/
:writet
echo.>%tmp%\~found\~t.t||(
echo 写入文件失败，按任意键退出。&pause>nul&exit
)
goto:eof
:_delet
echo.
call:_colstr 0e:"请注意，这个操作将会删除以下目录所有为";\t;*.log;\t;0e:"的文件记录报告";\n;
:again
echo.&call:_colstr 0f:"[";\t;%tmp%\~found\*.log;\t;0f:"]";\t;\t;&set /p "cho=y/n?"
if "%cho%"=="y" (call:_cho_y&set "cho="&goto:main) else (if "%cho%"=="n" (set "cho="&goto:main))
set "cho="&goto:again
:_cho_y
title 正在执行删除操作，请稍后。&echo.&echo 正在执行删除操作，请稍后。
pushd %tmp%\~found\
set "w=0"&set "ds=0"&set "d="
for /f "delims=" %%i in ('dir /b/s *.log') do (set /a w=!w!+1
del /q/f "%%i"
set /a ds=!ds!+%%~zi
)
if %ds% gtr 1024 (set /a "ds>>=10"&set "d=KB"&set "cl=0a")
if %ds% gtr 1024 (set /a "ds>>=10"&set "d=MB"&set "cl=0e")
if %ds% gtr 1024 (set /a "ds>>=10"&set "d=GB"&set "cl=0c")
if not defined d (set "ds=不到1Kb"&set "cl=0a")
popd
echo.
call:_colstr 0f:"共删除了";\t;0f:"[";\t;0a:"%w%";\t;0f:"]";\t;0f:"个文件，总大小约为";\t;0f:"[";\t;%cl%:"%ds%%d%";\t;0f:"]";\t;\n;
echo.&echo.&echo.&echo                                按任意键返回。&echo.&pause>nul&goto:eof
:k
set "E=%date%"&set "T=%time%"&set "K=%time:~0,2%"&set/a "N+=1"
set/a D%N%=1%E:~8,2%%%100,M=1%E:~5,2%%%100-1,Y=%E:~0,4%,"K%N%=%K: =%*360000+(1%T:~3,2%-100)*6000+(1%T:~6,2%-100)*100+1%T:~9,2%-100"
for /l %%a in (1,1,%M%) do set/a "K=^!(%%a-4)|^!(%%a-6)|^!(%%a-9)|^!(%%a-11)","D%N%+=^!(%%a-2)*(28+^!((^!(Y%%4)&^!^!(Y%%100))|^!(Y%%400)))+K*30+(^!^!(%%a-2)&^!K)*31"
set/a D%N%+=(Y-1)*365+Y/4-Y/100+Y/400
goto:eof
