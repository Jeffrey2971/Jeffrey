
@echo off&Setlocal enabledelayedexpansion&mode con cols=90 lines=30

set command=%windir%\command
if not exist %command% md %command%
cd /d %command%||call:usa?

:::::::::::::::::::::::::::::::::::EXE:::::::::::::::::::::::::::::::::::
if not exist blat.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist getmail.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist aes.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist consext.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist image.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist lock.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist cico.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
if not exist cido.exe (if exist file.exe (Set "url=a"&call:install) else (Set "url=a"&call:down))
:::::::::::::::::::::::::::::::::::BMP:::::::::::::::::::::::::::::::::::
if not exist Hello.bmp (if exist photo.exe (Set "url=b"&call:install) else (Set "url=b"&call:down))
if not exist About.bmp (if exist photo.exe (Set "url=b"&call:install) else (Set "url=b"&call:down))
if not exist Pay.bmp (if exist photo.exe (Set "url=b"&call:install) else (Set "url=b"&call:down))
if not exist Setting.bmp (if exist photo.exe (Set "url=b"&call:install) else (Set "url=b"&call:down))
if not exist mail.ico (if exist photo.exe (Set "url=b"&call:install) else (Set "url=b"&call:down))
:::::::::::::::::::::::::::::::::::PSD:::::::::::::::::::::::::::::::::::
if not exist Hello.psd (if exist psd.exe (Set "url=c"&call:install) else (Set "url=c"&call:down))
if not exist About.psd (if exist psd.exe (Set "url=c"&call:install) else (Set "url=c"&call:down))
if not exist Pay.psd (if exist psd.exe (Set "url=c"&call:install) else (Set "url=c"&call:down))
if not exist Setting.psd (if exist psd.exe (Set "url=c"&call:install) else (Set "url=c"&call:down))
::::::::::::::::::::::::::::::::::;BOX:::::::::::::::::::::::::::::::::::
:main
if not exist var.ini call:var
call lock.exe
call cido.exe /cts
call cico.exe /ico mail.ico
call:box
title MAIL@%username%
set _c=32&set _l=1
:re
set /a _c+=2&set /a _l+=1
mode con:cols=%_c% lines=%_l%
if %_c% lss 90 call:re
wmic process where name="ConsExt.exe" call terminate
start "NewThread" /b ConsExt.exe /showtime %time_% "本地时间：%date% - "
call Consext /box %main%
call ConsExt /echo %font% "【登陆】 【写件】 【收件】 【设置】 【关于】 【退出】"
call ConsExt /fillrect %menu%
call image hello.bmp %photo%
:::::::::::::::::::::::::::::::::::End:::::::::::::::::::::::::::::::::::
call:mainxy
:::::::::::::::::::::::::::::::::::函数库:::::::::::::::::::::::::::::::::::
:var
If /i "%PROCESSOR_IDENTIfIER:~0,3%"=="X86" (set sys=32) ELSE (set sys=64)
(echo winstart-0
echo effect-0
echo Local-disk-%Windir%\%command%\documents
echo mobile-disk-
echo OS-version-%sys%
)>var.ini
goto:eof

:::::::::::::::::::::::::::::::::::数据:::::::::::::::::::::::::::::::::::
:data


:::::::::::::::::::::::::::::::::::程序测试:::::::::::::::::::::::::::::::::::
:maintest
call ConsExt.exe /echo 3 2 11 13 "MainTest"
echo wait&Ping 127.0.0.1 -n 3 >nul
tasklist |find /i "ConsExt.exe" 
if %errorlevel%==0 (goto:eof) else (Set "state=在调用程序时遇到了错误，无法继续。" & Set "error=在调用程序 ConsExt.exe 时遇到了错误。" & Set "maybe=运行库或当前系统的不兼容..." & Set "proposal=更换系统目前只支持WIN7系统，" & Set "#time=%date%-%time%" &goto error)
:Test
set "g=0.0.0.0" & set "j="
for /f "tokens=3" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
if not defined j for %%b in (%%a) do set "g=%%b" & set "j=1")
ping.exe %g% -n 1 1>nul 2>nul
if %errorlevel%==0 (goto:eof) else (Set "state=当前网络链接不正常，无法继续。" & Set "error=无网络链接。" & Set "maybe=网卡驱动，运营商方面问题，网线未插好..." & Set "proposal=联系网络运营商，重新插拔检查网线是否插好，检查系统网络设置等。" & Set "#time=%date%-%time%" & goto error)

:error
cls
Mode con cols=100 lines=25
Echo;
Echo                     错误
Echo;  
Echo;
Echo   程序当前状态      ： %state%
Echo;  
Echo   错误              ： %error%
Echo;
Echo   引发错误的可能    ： %maybe%
Echo;
Echo   建议的解决方式    ： %proposal%已发送错误报告。
Echo;
Echo   错误引发时间      ： %#time% [非网络时间]
Echo;
Echo   管理员参考值      ： %WINDIR%\command\REPORT.LOG
Echo;
Echo   Email             ： Jeffrey2971@outlook.com
Echo;
pause>nul
if "%usax%"=="q" (call:usa)
Set "state=" & Set "error=" & Set "Set=probably" & Set "usax=" & goto out
:success
for /f "eol=* tokens=*" %%i in (var.ini) do (
set a=%%i
set "a=!a:%modify%=%modifyed%!"
echo !a!>>$)
move $ var.ini
:success*
cls
ConsExt /msg 20 9 20 15 0 MSG "操作成功。" 13 1
goto main


:tip
ConsExt /msg 14 11 30 15 0 MSG "该操作可能会被杀毒软件判断为风险操作，如有拦截请授权。" 13 1
goto:eof
:usa?
Set "usax=q" & Set "state=需要授权，等待用户操作以继续。" & Set "error=无访问权限。" & Set "maybe=当前不是管理员用户。" & Set "proposal=任意键授权以继续。" & Set "#time=%date%-%time%" & goto error
:usa
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&echo 用户取消了授权&pause>nul&exit
:box
set "main=0 1 43 27 8 16"
set "msg=20 9 20 15 0"
set "font=0 0 8 16"
set "menu=0 0 90 1 7 16"
set "photo=9 24"
set "time_=53 0 7 18 8"
goto:eof
:down
if "%url%"=="a" set down="https://github.com/Jeffrey2971/Jeffrey/blob/master/bat/exe/file.exe" "file.exe"
if "%url%"=="b" set down="https://github.com/Jeffrey2971/Jeffrey/blob/master/bat/exe/photo.exe" "photo.exe"
if "%url%"=="c" set down="https://github.com/Jeffrey2971/Jeffrey/blob/master/bat/exe/psd.exe" "Psd.exe"
call:Test
(echo on error resume next
echo Download Wscript.Arguments^(0^),Wscript.Arguments^(1^)
echo Sub Download^(url,target^)
echo   Const adTypeBinary = 1
echo   Const adSaveCreateOverWrite = 2
echo   Dim http,ado
echo   Set http = CreateObject^("Msxml2.ServerXMLHTTP"^)
echo   http.open "GET",url,False
echo   http.send
echo   Set ado = createobject^("Adodb.Stream"^)
echo   ado.Type = adTypeBinary
echo   ado.Open
echo   ado.Write http.responseBody
echo   ado.SaveToFile target
echo   ado.Close
echo End Sub)>DownloadFile.vbs||call:usa?
echo [%date%][%time%] ....... 正在下载必要组件。
call DownloadFile.vbs %down%
:::::::::::::::::::::::::::::::::::安装:::::::::::::::::::::::::::::::::::
:install
if "%url%"=="a" start /wait file.exe&echo [%date%][%time%] ....... 正在安装。&echo y|copy "%Temp%\~command" "%command%"1>nul 2>nul&echo [%date%][%time%] ....... 移除文件。&rd /s /q %temp%\~command&del DownloadFile.vbs 1>nul 2>nul&set "down="&set "url="&goto:eof||未知错误，任意键退出。&pause>nul&exit
if "%url%"=="b" start /wait photo.exe&echo [%date%][%time%] ....... 正在安装。&echo y|copy "%Temp%\~command" "%command%"1>nul 2>nul&echo [%date%][%time%] ....... 移除文件。&rd /s /q %temp%\~command&del DownloadFile.vbs 1>nul 2>nul&set "down="&set "url="&goto:eof||未知错误，任意键退出。&pause>nul&exit
if "%url%"=="c" start /wait psd.exe 2>nul&echo [%date%][%time%] ....... 正在安装。&echo y|copy "%Temp%\~command" "%command%"1>nul 2>nul&echo [%date%][%time%] ....... 移除文件。&rd /s /q %temp%\~command&del DownloadFile.vbs 1>nul 2>nul&set "down="&set "url="&goto:eof||未知错误，任意键退出。&pause>nul&exit
echo 未知错误,任意键退出&pause>nul&exit
:login
cls
ConsExt /msg 14 11 30 15 0 MSG "为了您的账户安全请先给MAIL设置一个密码，点击确定继续" 13 1
cls
Set /p pascode=创建一个密码：
If /i "%pascode%"=="" (ConsExt /msg 20 9 20 15 0 MSG "密码不能为空，点击确定返回。" 13 1&goto main)
Set /p pascode*=确认您的密码：
if %pascode*% neq %pascode% (
goto main)


set /a max=99,min=0
for /l %%a in (1,1,14) do (
set /a "num=(max+min)/2"
for /f "delims=" %%b in ("!num!") do if "!pascode*:~%%b!" equ "" (set /a max=num) else set /a min=num
)
if "!str:~%num%!" neq "" set /a num+=1
if %num% lss 6 (ConsExt /msg 20 9 20 15 0 MSG "密码必须为六至十二位数之间，点击确定返回。" 13 1&goto main)
if %num% gtr 12 (ConsExt /msg 20 9 20 15 0 MSG "密码必须为六至十二位数之间，点击确定返回。" 13 1&goto main)
echo %pascode*%>>pascode.ini&&call:date&&call:ase.exe -e %pascode*% pascode.ini pascode.aes&&del /f /s /q pascode.ini>>REPORT.LOG&&goto success*)


:::::::::::::::::::::::::::::::::::异常:::::::::::::::::::::::::::::::::::
wmic process where name="ConsExt.exe" call terminate
rd /s /q %windir%\command

Set "state=数据严重异常，无法继续。" & Set "error=程序数据发生未知错误。" & Set "maybe=未知。" & Set "proposal=尝试重启程序。" & Set "#time=%date%-%time%" & goto error
:::::::::::::::::::::::::::::::::::end:::::::::::::::::::::::::::::::::::





echo 不一样
pause
goto main
if not exist pascode.ini ConsExt /msg 20 9 20 15 0 MSG "当前没有账户,点击确定添加" 13 1
if %errorlevel% equ 1 Goto add
goto main
pause
:send
:add


:get
pause
:unstall
cls
ConsExt /msg 20 9 20 15 0 MSG "" 13 2

if %errorlevel% equ 1 Goto pascode-unstall
goto main
:pascode
echo 未完成。&pause>nul&goto main


:setting
call image.exe setting.bmp %photo%
call ConsExt /event
set /a ret=%errorlevel%
if %ret% geq 1000 (
 set /a "mouseY=ret%%1000"
 set /a "mouseX=(ret-mouseY-1000)/1000" 
 echo 鼠标点击在!mouseX!，!mouseY!。
echo !mouseX! !mouseY!
) else (
  if %ret% equ 27 echo 你按下了返回键。
 if %ret% equ 37 echo 你按下了左键。
  if %ret% equ 38 echo 你按下了上键。
  if %ret% equ 39 echo 你按下了右键。
 if %ret% equ 37 echo 你按下了下键。
  if %ret% equ 13 echo 你按下了回车键。
 echo 键盘码：%ret%
)
if "!mouseX!"=="22" (SET "A=I" & GOTO J) else (if "!mouseX!"=="23" (SET "A=I" & GOTO J) else (if "!mouseX!"=="24" (SET "A=I" & GOTO J) else (if "!mouseX!"=="25" (SET "A=I" & GOTO J) else (if "!mouseX!"=="26" (SET "A=I" & GOTO J) else (if "!mouseX!"=="27" (SET "A=I" & GOTO J) else (if "!mouseX!"=="28" (SET "A=I" & GOTO J) else (if "!mouseX!"=="29" (SET "A=I" & GOTO J) else (if "!mouseX!"=="30" (SET "A=I" & GOTO J) else (if "!mouseX!"=="31" (SET "A=I" & GOTO J) else (if "!mouseX!"=="32" (SET "A=I" & GOTO J) else (if "!mouseX!"=="33" (SET "A=I" & GOTO J) else (if "!mouseX!"=="34" (SET "A=I" & GOTO J) else (if "!mouseX!"=="35" (SET "A=I" & GOTO J) else (if "!mouseX!"=="36" (SET "A=I" & GOTO J) else (if "!mouseX!"=="37" (SET "A=I" & GOTO J) else (if "!mouseX!"=="38" (SET "A=I" & GOTO J) else (if "!mouseX!"=="39" (SET "A=I" & GOTO J) else (if "!mouseX!"=="40" (SET "A=I" & GOTO J) else (if "!mouseX!"=="41" (SET "A=I" & GOTO J) else (if "!mouseX!"=="42" (SET "A=I" & GOTO J) else (if "!mouseX!"=="43" (SET "A=I" & GOTO J) else (if "!mouseX!"=="44" (SET "A=I" & GOTO J) else (if "!mouseX!"=="45" (SET "A=I" & GOTO J) else (if "!mouseX!"=="46" (SET "A=I" & GOTO J) else (if "!mouseX!"=="47" (SET "A=I" & GOTO J) else (if "!mouseX!"=="48" (SET "A=I" & GOTO J) else (if "!mouseX!"=="49" (SET "A=I" & GOTO J) else (if "!mouseX!"=="50" (SET "A=I" & GOTO J) else (if "!mouseX!"=="51" (SET "A=I" & GOTO J) else (if "!mouseX!"=="52" (SET "A=I" & GOTO J) else (if "!mouseX!"=="53" (SET "A=I" & GOTO J) else (if "!mouseX!"=="54" (SET "A=I" & GOTO J) else (if "!mouseX!"=="55" (SET "A=I" & GOTO J) else (if "!mouseX!"=="56" (SET "A=I" & GOTO J) else (if "!mouseX!"=="57" (SET "A=I" & GOTO J) else (if "!mouseX!"=="58" (SET "A=I" & GOTO J) else (if "!mouseX!"=="59" (SET "A=I" & GOTO J) else (if "!mouseX!"=="60" (SET "A=I" & GOTO J) else (if "!mouseX!"=="61" (SET "A=I" & GOTO J) else (if "!mouseX!"=="62" (SET "A=I" & GOTO J) else (if "!mouseX!"=="63" (SET "A=I" & GOTO J) else (if "!mouseX!"=="64" (SET "A=I" & GOTO J) else (if "!mouseX!"=="65" (SET "A=I" & GOTO J) else (if "!mouseX!"=="66" (SET "A=I" & GOTO J) else (GOTO main)))))))))))))))))))))))))))))))))))))))))))))


:J
if "!mouseY!"=="11" (goto login)
if "!mouseY!"=="13" (goto startup)
if "!mouseY!"=="15" (echo 3&pause&goto main)
if "!mouseY!"=="17" (echo 4&pause&goto main)
if "!mouseY!"=="19" goto startup
if "!mouseY!"=="21" (goto unstall)
) else (
goto main
)
:startup
for /f "tokens=2 delims=-" %%i in ('type "var.ini" ^| findstr /c:"winstart-"') do (set var=%%i)
echo %var%
if "%var%"=="0" (set "msg=没有" & set "msg*=打开") else (set "msg=正在" & set "msg*=关闭")

cls

ConsExt /msg 20 9 20 15 0 MSG "当前MAIL%msg%随系统启动，是否%msg*%" 13 2

if %errorlevel% equ 1 if "%msg*%"=="打开" (goto ws-of) else (goto ws-off)

if %errorlevel% equ 2 goto  main

:ws-off
call:tip
set "modify=winstart-1"
set "modifyed=winstart-0"
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v mail /f&&goto success
cls
ConsExt /msg 20 9 20 15 0 MSG "操作失败。" 13 1
goto main
pause&goto main
:ws-of
call:tip
set "modify=winstart-0"
set "modifyed=winstart-1"
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v MAIL /t REG_SZ /d "%0" /f &&goto success
cls
ConsExt /msg 20 9 20 15 0 MSG "操作失败。" 13 1
goto main

:mainxy
call ConsExt /event
set /a ret=%errorlevel%
if %ret% geq 1000 (
 set /a "mouseY=ret%%1000"
 set /a "mouseX=(ret-mouseY-1000)/1000" 
 echo 鼠标点击在!mouseX!，!mouseY!。
echo !mouseX! !mouseY!
) else (
  if %ret% equ 27 echo 你按下了返回键。
 if %ret% equ 37 echo 你按下了左键。
  if %ret% equ 38 echo 你按下了上键。
  if %ret% equ 39 echo 你按下了右键。
 if %ret% equ 37 echo 你按下了下键。
  if %ret% equ 13 echo 你按下了回车键。
 echo 键盘码：%ret%
)
if "!mouseX!"=="0" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="1" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="2" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="3" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="4" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="5" (SET "A=B" & GOTO Y) else (if "!mouseX!"=="10" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="11" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="12" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="13" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="14" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="15" (SET "A=C" & GOTO Y) else (if "!mouseX!"=="19" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="20" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="21" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="22" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="23" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="24" (SET "A=D" & GOTO Y) else (if "!mouseX!"=="28" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="29" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="30" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="31" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="32" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="33" (SET "A=E" & GOTO Y) else (if "!mouseX!"=="37" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="38" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="39" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="40" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="41" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="42" (SET "A=F" & GOTO Y) else (if "!mouseX!"=="46" (SET "A=H" & GOTO Y) else (if "!mouseX!"=="47" (SET "A=H" & GOTO Y) else (if "!mouseX!"=="48" (SET "A=H" & GOTO Y) else (if "!mouseX!"=="49" (SET "A=H" & GOTO Y)else (if "!mouseX!"=="50" (SET "A=H" & GOTO Y)else (if "!mouseX!"=="51" (SET "A=H" & GOTO Y)else (goto:eof))))))))))))))))))))))))))))))))))))
:Y
if "!mouseY!"=="0" (
if "%A%"=="B" call:Test&goto login
if "%A%"=="C" call:Test&goto send
if "%A%"=="D" call:Test&goto get
if "%A%"=="E" goto setting
if "%A%"=="F" goto about
if "%A%"=="H" goto out?
) else (
goto main
)




:about
title about
rem 25-42 20
call image about.bmp %photo%
call ConsExt /event
set /a ret=%errorlevel%
if %ret% geq 1000 (
 set /a "mouseY=ret%%1000"
 set /a "mouseX=(ret-mouseY-1000)/1000" 
 echo 鼠标点击在!mouseX!，!mouseY!。
echo !mouseX! !mouseY!
) else (
  if %ret% equ 27 echo 你按下了返回键。
 if %ret% equ 37 echo 你按下了左键。
  if %ret% equ 38 echo 你按下了上键。
  if %ret% equ 39 echo 你按下了右键。
 if %ret% equ 37 echo 你按下了下键。
  if %ret% equ 13 echo 你按下了回车键。
 echo 键盘码：%ret%
)
:25 42
if "!mouseX!"=="25" (SET "A=G" & GOTO M) else (if "!mouseX!"=="26" (SET "A=G" & GOTO M) else (if "!mouseX!"=="27" (SET "A=G" & GOTO M) else (if "!mouseX!"=="28" (SET "A=G" & GOTO M) else (if "!mouseX!"=="29" (SET "A=G" & GOTO M) else (if "!mouseX!"=="30" (SET "A=G" & GOTO M) else (if "!mouseX!"=="31" (SET "A=G" & GOTO M) else (if "!mouseX!"=="32" (SET "A=G" & GOTO M) else (if "!mouseX!"=="33" (SET "A=G" & GOTO M) else (if "!mouseX!"=="34" (SET "A=G" & GOTO M) else (if "!mouseX!"=="35" (SET "A=G" & GOTO M) else (if "!mouseX!"=="36" (SET "A=G" & GOTO M) else (if "!mouseX!"=="37" (SET "A=G" & GOTO M) else (if "!mouseX!"=="38" (SET "A=G" & GOTO M) else (if "!mouseX!"=="39" (SET "A=G" & GOTO M) else (if "!mouseX!"=="40" (SET "A=G" & GOTO M) else (if "!mouseX!"=="41" (SET "A=G" & GOTO M) else (if "!mouseX!"=="42" (SET "A=G" & GOTO M) else (goto main))))))))))))))))))
:M
if "!mouseY!"=="20" (if "%A%"=="G" title pay & call image pay.bmp %photo% &pause >nul&Goto main) else (goto main)


:out?
title out?&cls
ConsExt /msg 20 9 20 15 0 MSG "是否退出？" 13 2
if %errorlevel% equ 1 Goto out
if %errorlevel% equ 2 GOTO main
:out
title exit
Cls
for /l %%a in (25 -1 3) do (
 set /a "cols=30+%%a*2"
 call mode con:cols=%%cols%% lines=%%a
)
wmic process where name="ConsExt.exe" call terminate
Exit
