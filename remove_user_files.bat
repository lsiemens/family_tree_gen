@echo off
@echo Removing all "family tree maker" user files
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

rd %userprofile%\AppData\Roaming\family_tree_maker /s/q
del %userprofile%\Desktop\family_tree_maker.lnk

:END
endlocal