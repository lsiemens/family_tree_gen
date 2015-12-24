@echo off
@echo Install family_tree_gen: this software will be installed into "%userprofile%\AppData\Local\family_tree_gen"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

set dir="%userprofile%\AppData\Local\family_tree_gen"

mkdir %dir%
mkdir %dir%\code
mkdir %dir%\data
mkdir %dir%\html
mkdir %dir%\notebook
mkdir %dir%\template

copy "%~dp0LICENSE.txt" %dir%\
copy "%~dp0CC_BY_4.0.txt" %dir%\
copy "%~dp0README.md" %dir%\

copy "%~dp0efamily.py" %dir%\code
copy "%~dp0efamily_html.py" %dir%\code
copy "%~dp0efamily_widget.py" %dir%\code
copy "%~dp0widget_framework.py" %dir%\code
copy "%~dp0widget_utils.py" %dir%\code

copy "%~dp0uninstaller.bat" %dir%
copy "%~dp0run.bat" %dir%\code
copy "%~dp0green_tree.ico" %dir%\code

copy "%~dp0family_tree_gen.ipynb" %dir%\notebook\
copy "%~dp0template.html" %dir%\template

::Create shortcuts
@echo off
echo Set oWS = WScript.CreateObject("WScript.Shell") > %~dp0CreateShortcut.vbs
echo sLinkFile = "%userprofile%\Desktop\Family_Tree_Gen.lnk" >> %~dp0CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %~dp0CreateShortcut.vbs
echo oLink.TargetPath = "%userprofile%\AppData\Local\family_tree_gen\code\run.bat" >> %~dp0CreateShortcut.vbs
echo oLink.IconLocation = "%userprofile%\AppData\Local\family_tree_gen\code\green_tree.ico, 0" >> %~dp0CreateShortcut.vbs
echo oLink.Save >> %~dp0CreateShortcut.vbs
cscript %~dp0CreateShortcut.vbs
del %~dp0CreateShortcut.vbs
pause

:END
endlocal
