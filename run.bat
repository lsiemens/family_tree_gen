
@echo off
@echo Start IPython notebook server
@echo 	press control-c twice, and answer yes(Y) to close

setlocal
set PYTHONPATH=%PYTHONPATH%;%~dp0%
ipython notebook --notebook-dir="%userprofile%\AppData\Roaming\family_tree_maker\notebook"
endlocal