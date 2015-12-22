:::::::::::::::::::::::::::::::::::::::::
:: Automatically check & get admin rights
:::::::::::::::::::::::::::::::::::::::::
@echo off

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)

setlocal DisableDelayedExpansion
set "batchPath=%~0"
setlocal EnableDelayedExpansion
ECHO Set UAC = CreateObject^("Shell.Application"^) > "%temp%\OEgetPrivileges.vbs"
ECHO args = "ELEV " >> "%temp%\OEgetPrivileges.vbs"
ECHO For Each strArg in WScript.Arguments >> "%temp%\OEgetPrivileges.vbs"
ECHO args = args ^& strArg ^& " "  >> "%temp%\OEgetPrivileges.vbs"
ECHO Next >> "%temp%\OEgetPrivileges.vbs"
ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%temp%\OEgetPrivileges.vbs"
"%SystemRoot%\System32\WScript.exe" "%temp%\OEgetPrivileges.vbs" %*
exit /B

:gotPrivileges
if '%1'=='ELEV' shift /1
setlocal & pushd .
cd /d %~dp0

::::::::::::::::::::::::::::
::START
::::::::::::::::::::::::::::

@echo off
@echo Install family_tree_maker: this software will be installed into "%programfiles(x86)%\family_tree_maker"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

mkdir "%programfiles(x86)%\family_tree_maker"
copy "%~dp0LICENSE" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0README.md" "%programfiles(x86)%\family_tree_maker\"

copy "%~dp0efamily.py" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0efamily_html.py" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0efamily_widget.py" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0widget_framework.py" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0widget_utils.py" "%programfiles(x86)%\family_tree_maker\"

copy "%~dp0uninstaller.bat" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0run.bat" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0Family_Tree_Maker.lnk" "%programfiles(x86)%\family_tree_maker\"

copy "%~dp0family_tree_maker.ipynb" "%programfiles(x86)%\family_tree_maker\"
copy "%~dp0template.html" "%programfiles(x86)%\family_tree_maker\"

@echo Setup user files
mkdir %userprofile%\AppData\Roaming\family_tree_maker
mkdir %userprofile%\AppData\Roaming\family_tree_maker\data
mkdir %userprofile%\AppData\Roaming\family_tree_maker\html
mkdir %userprofile%\AppData\Roaming\family_tree_maker\notebook
mkdir %userprofile%\AppData\Roaming\family_tree_maker\template

copy "%programfiles(x86)%\family_tree_maker\template.html" %userprofile%\AppData\Roaming\family_tree_maker\template\template.html
copy "%programfiles(x86)%\family_tree_maker\family_tree_maker.ipynb" %userprofile%\AppData\Roaming\family_tree_maker\notebook\family_tree_maker.ipynb
copy "%programfiles(x86)%\family_tree_maker\family_tree_maker.lnk" %userprofile%\desktop\family_tree_maker.lnk
pause

:END
endlocal