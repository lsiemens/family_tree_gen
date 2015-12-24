@echo off
@echo Uninstall family_tree_maker: removing family_tree_maker from "%userprofile%\AppData\Local\family_tree_maker"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

set dir=%userprofile%\AppData\Local\family_tree_maker

@echo Removing user files
rd %dir% /s/q
del %userprofile%\Desktop\family_tree_maker.lnk

@echo Uninstalling
::del "%programfiles(x86)%\family_tree_maker\LICENSE"
::del "%programfiles(x86)%\family_tree_maker\README.md"

::del "%programfiles(x86)%\family_tree_maker\efamily.py"
::del "%programfiles(x86)%\family_tree_maker\efamily_html.py"
::del "%programfiles(x86)%\family_tree_maker\efamily_widget.py"
::del "%programfiles(x86)%\family_tree_maker\widget_framework.py"
::del "%programfiles(x86)%\family_tree_maker\widget_utils.py"

::del "%programfiles(x86)%\family_tree_maker\family_tree_maker.ipynb"
::del "%programfiles(x86)%\family_tree_maker\template.html"

::del "%programfiles(x86)%\family_tree_maker\Family_Tree_Maker.lnk"
::del "%programfiles(x86)%\family_tree_maker\run.bat"
::del "%programfiles(x86)%\family_tree_maker\uninstaller.bat"
pause

:END
endlocal
