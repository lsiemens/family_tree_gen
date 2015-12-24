
@echo off
@echo Start IPython notebook server
@echo 	press control-c twice, and answer yes(Y) to close

setlocal
set PYTHONPATH=%PYTHONPATH%;%~dp0%
ipython notebook --notebook-dir="%userprofile%\AppData\Local\family_tree_gen\notebook"
endlocal
