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
@echo Uninstall family_tree_maker: removing family_tree_maker from "%programfiles(x86)%\family_tree_maker"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

@echo Removing user files
rd %userprofile%\AppData\Roaming\family_tree_maker /s/q
del %userprofile%\Desktop\family_tree_maker.lnk

@echo Uninstalling
del "%programfiles(x86)%\family_tree_maker\LICENSE"
del "%programfiles(x86)%\family_tree_maker\README.md"

del "%programfiles(x86)%\family_tree_maker\efamily.py"
del "%programfiles(x86)%\family_tree_maker\efamily_html.py"
del "%programfiles(x86)%\family_tree_maker\efamily_widget.py"
del "%programfiles(x86)%\family_tree_maker\widget_framework.py"
del "%programfiles(x86)%\family_tree_maker\widget_utils.py"

del "%programfiles(x86)%\family_tree_maker\family_tree_maker.ipynb"
del "%programfiles(x86)%\family_tree_maker\template.html"

del "%programfiles(x86)%\family_tree_maker\Family_Tree_Maker.lnk"
del "%programfiles(x86)%\family_tree_maker\run.bat"
del "%programfiles(x86)%\family_tree_maker\uninstaller.bat"
pause

:END
endlocal