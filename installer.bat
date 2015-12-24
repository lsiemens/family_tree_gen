@echo off
@echo Install family_tree_maker: this software will be installed into "%userprofile%\AppData\Local\family_tree_maker"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

set dir="%userprofile%\AppData\Local\family_tree_maker"
echo %dir%

mkdir %dir%
mkdir %dir%\data
mkdir %dir%\html
mkdir %dir%\notebook
mkdir %dir%\template

copy "%~dp0LICENSE" %dir%\
copy "%~dp0README.md" %dir%\

copy "%~dp0efamily.py" %dir%\
copy "%~dp0efamily_html.py" %dir%\
copy "%~dp0efamily_widget.py" %dir%\
copy "%~dp0widget_framework.py" %dir%\
copy "%~dp0widget_utils.py" %dir%\

copy "%~dp0uninstaller.bat" %dir%\
copy "%~dp0run.bat" %dir%\
copy "%~dp0Family_Tree_Maker.lnk" %userprofile%\desktop\family_tree_maker.lnk

copy "%~dp0family_tree_maker.ipynb" %dir%\notebook\
copy "%~dp0template.html" %dir%\template

::Create shortcuts
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > %~dp0CreateShortcut.vbs
echo sLinkFile = "%userprofile%\Desktop\Family_Tree_Maker.lnk" >> %~dp0CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %~dp0CreateShortcut.vbs
echo oLink.TargetPath = "%userprofile%\AppData\Local\family_tree_maker\run.bat" >> %~dp0CreateShortcut.vbs
echo oLink.Save >> %~dp0CreateShortcut.vbs
cscript %~dp0CreateShortcut.vbs
del %~dp0CreateShortcut.vbs

pause

:END
endlocal
