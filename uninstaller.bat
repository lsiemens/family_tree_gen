@echo off
@echo Uninstall family_tree_gen: removing family_tree_gen from "%userprofile%\AppData\Local\family_tree_gen"
setlocal
:PROMPT
SET /P AREYOUSURE=Would you like to continue (Y/N)?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

set dir=%userprofile%\AppData\Local\family_tree_gen

rd %dir%\code /s/q
rd %dir%\template /s/q
rd %dir%\html /s/q
rd %dir%\notebook /s/q
del %userprofile%\Desktop\Family_Tree_Gen.lnk

:PROMPT
SET /P AREYOUSUREALL=Would you like to remove all user data and files (Y/N)?
IF /I "%AREYOUSUREALL%" NEQ "Y" GOTO END
rd %dir% /s/q

pause

:END
endlocal
