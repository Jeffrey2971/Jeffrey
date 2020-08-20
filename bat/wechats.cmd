@Echo off&color 0f&title 微信多开。
rem Jeffrey2971@outlook.com WeChat Jeffrey2971
:main
Echo.&Echo.&Echo 执行中...
if not exist %tmp%\wxdata md %tmp%\wxdata
pushd %tmp%\wxdata
echo %date% - %time% started.>>data.log
del /f /s /q cpu_safe.cmd stop started wait>nul 2>nul
tasklist | find /i "WeChat.exe">nul 2>nul&&(
Echo.&Echo.&Echo 异常：已经有一个或多个微信正在运行,请关闭并稍后按任意键重试。
pause>nul
goto:main
)
if exist WeChat_int.ini (
set /p file=<"%tmp%\wxdata\WeChat_int.ini"&&goto:_found
)
Echo.&Echo.&Echo 正在你的系统中查找微信 (WeChat.exe) 首次运行可能需要较长时间,请稍后。
for %%a in (A B C D E F G H I J K L M N) do (
if exist %%a:\ (
cd /d %%a:\
for /f "delims=" %%b in ('dir /s /a-d /b WeChat.exe 2^>nul') do (
if exist "%%b" (
Echo %%b>%tmp%\wxdata\WeChat_int.ini||goto:error
set file=%%b
if "%fix%"=="y" goto:eof
goto:_found
))))
if not defined file (Echo.&Echo.&Echo 异常：你的系统好像没有安装微信,无法继续,任意键退出。&pause>nul&exit)
:_found
mode con cols=80 lines=25
Taskkill /f /im WeChat.exe >nul 2>nul
set "num="
set "ed="
set fix=n
cls
Echo.&Echo.
set /p num=微信路径已找到,在这里输入需要打开多少个微信：
if not defined num set "num=null"
echo %date% - %time% enter:%num% >>data.log
if "%num%"=="/data" start /wait "" "%tmp%\wxdata\data.log"&goto:_found
if "%num%"=="/help" call:help&goto:_found
if "%num%"=="/exit" echo %date% - %time% exit.>>data.log&exit
Echo %num%|findstr /v "[^0-9]"||(
Echo.&Echo.
Echo 异常：输入不能为空且只能为数字,如需帮助请输入 /help 任意键继续。
pause>nul
goto:_found
)
if %num% equ 0 goto:_found
if %num% geq 5 (
Echo.&Echo.&Echo 打开过多的微信可能没有效果且造成系统卡顿甚至死机,是否继续?
call:again
)
:open
pushd %tmp%\wxdata
Echo.
Echo.
Echo 正在启用内存保护组件,请稍后...&call:cpu_safe
for /l %%i in (1,1,%num%) do (
if exist wait call:wait_kill
start "" "%file%"||(
Echo %date% - %time% error:start WeChat.exe no success.>>data.log
goto:error
)
set /a "ed+=1"
)
del /f /s /q started>nul 2>nul
Echo stop>stop
Echo.&Echo.&Echo 已尝试打开 %ed% 个微信,如果未达到预期数量请在界面输入 /help 获取帮助,任意键返回。&set "num="&pause>nul&goto:main
:again
Echo.&Echo.
set /p stop=y/n ？
if "%stop%"=="y" set "stop="&goto:open
if "%stop%"=="n" set "stop="&goto:_found
set "stop="&goto:again
:wait_kill
Echo.
Echo.
Echo 程序暂停,当前已经打开 %ed% 个微信,请稍后。
:wait_kill_
if not exist wait (Echo .&Echo.&Echo 正在执行。&goto:eof) else (goto:wait_kill_)
:error
pushd %tmp%\wxdata
mode con cols=80 lines=35&title 文件修复。
cls
Echo.&Echo.&Echo                               操作异常,正在修复。
Echo %date% - %time% Abnormal operation,attempting to repair:>>data.log
Echo Test>%systemroot%\system32\Test_usa||(
Echo.&Echo.&Echo 正在调用管理员权限,请允许。
call:usa
)
del /f /s /q %systemroot%\system32\Test_usa >nul 2>nul
Echo stop>stop
Echo.&Echo.
Echo %time% --- 尝试修复配置文件。
Echo Y|cacls "WeChat_int.ini" /p everyone:F >nul 2>nul||(
Echo %date% - %time% error:cacls WeChat_int.ini no success.>>data.log
Echo.&Echo.&Echo %time% --- 异常：修复配置文件失败,任意键退出。&pause>nul&exit
)
Echo.&Echo.&Echo %time% --- 配置文件修复成功！
Echo.&Echo.
Echo %time% --- 尝试更新配置文件。
del /f /s /q WeChat_int.ini >nul 2>nul||(
Echo %date% - %time% error:Delet WeChat_int.ini no success.>>data.log
Echo.&Echo.&Echo %time% --- 异常：更新配置文件失败,任意键退出。&pause>nul&exit
)
Echo.&Echo.&Echo %time% --- 配置文件更新成功！
Echo.&Echo.
Echo %time% --- 尝试重新获取文件路径。
set fix=y
set "file="
call:main
set /p file=<"%tmp%\wxdata\WeChat_int.ini"
if not defined file (
Echo %date% - %time% error:no WeChat.exe var.>>data.log
Echo.&Echo.&Echo %time% --- 尝试重新获取文件路径失败,任意键退出。&pause>nul&exit
)
Echo.&Echo.&Echo %time% --- 路径获取成功！
Echo.&Echo.
Echo %time% --- 正在检查权限问题。
Echo Y|cacls "%file%" /p everyone:F >nul 2>nul||(
Echo %date% - %time% error:cacls WeChat.exe no success.>>data.log
Echo.&Echo.&Echo %time% --- 授权失败,任意键退出。&pause>nul&exit
)
Echo.&Echo.
Echo %time% --- 文件修复成功,将在5秒后返回。
Echo %date% - %time% _fix success.>>%tmp%\wxdata\data.log
ping 127.0.0.1 -n 6 >nul
title 微信多开。
goto:main
:usa
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
:cpu_safe
Echo.
Echo.
Echo 正在添加组件,请稍后...
Echo rem test>>cpu_safe.cmd||(
Echo erro:write the cpu_safe.cmd no success.>>data.log
Echo.
Echo.
Echo 添加组件失败,将继续执行。
goto:eof
)
Echo Echo %%date%% - %%time%% open cpu_safe.^>^>%%tmp%%\wxdata\data.log>>cpu_safe.cmd 
Echo if ^"%%1^"==^"h^" goto begin>>cpu_safe.cmd
Echo start mshta vbscript:createobject(^"wscript.shell^").run(^"^"^"%%~nx0^"^" h^",0)(window.close)^&^&exit>>cpu_safe.cmd
Echo :begin>>cpu_safe.cmd
Echo Set ^"strlen=95^">>cpu_safe.cmd
Echo Set ^"num=7^">>cpu_safe.cmd
Echo set ^"cpu=0^">>cpu_safe.cmd
Echo set ^"new=0^">>cpu_safe.cmd
Echo set ^"cl=10^">>cpu_safe.cmd
Echo :again>>cpu_safe.cmd
Echo for /f ^"tokens=2 delims==^" %%%%a in ('wmic path Win32_PerfFormattedData_PerfOS_Processor get PercentProcessorTime /value^^^|findstr ^"PercentProcessorTime^"') do (>>cpu_safe.cmd
Echo Set ^"UseCPU=%%%%a^">>cpu_safe.cmd
Echo )>>cpu_safe.cmd
Echo Echo started^>started>>cpu_safe.cmd
Echo If exist %%tmp%%\wxdata\stop (>>cpu_safe.cmd
Echo Echo %%date%% - %%time%% exit cpu_safe.^>^>%%tmp%%\wxdata\data.log>>cpu_safe.cmd 
Echo exit>>cpu_safe.cmd
Echo )>>cpu_safe.cmd
Echo if %%new%% equ %%cl%% Set ^"cpu=0^">>cpu_safe.cmd
Echo If %%UseCPU%% geq %%strlen%% (Set /a ^"cpu+=1^" ^& Goto nat) else (Set ^"new+=1^" ^& Goto again)>>cpu_safe.cmd>>cpu_safe.cmd
Echo :nat>>cpu_safe.cmd
Echo If %%cpu%% gtr %%num%% (Echo %%date%% - %%time%% cpu_safe:CPU overload,Terminate wechat:^>^>data.log^&Echo wait^>wait ^& Taskkill /f /im WeChat.exe^>^>%%tmp%%\wxdata\data.log ^& del /f /s /q wait ^& set "cpu=0" ^& goto:again) else (Goto again)>>cpu_safe.cmd>>cpu_safe.cmd
Echo.
Echo.
Echo 添加成功,正在启动组件。
start cpu_safe.cmd||(
Echo %date% - %time% error:start the cpu_safe.cmd no success.>>data.log
Echo.
Echo.
Echo 启动组件失败,将返回继续执行。
goto:eof
)
Echo.
Echo.
Echo 启动成功,正在等待程序响应。
:wait
if not exist started goto:wait
Echo.
Echo.
Echo 运行成功,正在打开微信。
goto:eof
:help
cls
Echo.&Echo.
Echo                                   多开帮助
Echo.
Echo 1、关于文件修复：如使用多开的过程中发生异常,本程序会自动修复基本问题,需授权请允许,如问题还未修复请尝试重新下载安装或联系微信官方（关于自助修复：多开只会找到第一个微信并设置为默认,这可能不是一个有效的微信,如知真实有效的微信路径可尝试修改位于 %%tmp%%\wxdata\ 目录下的 WeChat_int.ini 配置文件首行的微信路径为真实有效的微信打开路径,路径内不可含有双引号。）
Echo.
Echo 2、关于内存保护：当打开过多的微信并造成系统严重卡顿无法继续正常操作时将会触发内存保护,这会关闭过多的微信确保CPU达到正常状态,这可能将无法达到预期输入的效果。
Echo.
Echo 3、关于无法打开预期的微信数量：如打开的微信数量未达到你预期输入的标准,可在原有的基础上适当添加例如：当需要打开3个微信可输入5。
Echo.
Echo 4、本程序属于合法程序不会对你的微信号造成任何影响。
Echo.
Echo 5、日志：/data   帮助：/help   退出：/exit
Echo.
Echo 6、额外帮助可联系 E-Mail：Jeffrey2971@outlook.com  WeChat：Jeffrey2971
Echo.
Echo 任意键返回界面。
pause>nul&goto:eof
