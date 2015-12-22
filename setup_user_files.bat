@ECHO Setup user files

mkdir %userprofile%\AppData\Roaming\family_tree_maker
mkdir %userprofile%\AppData\Roaming\family_tree_maker\data
mkdir %userprofile%\AppData\Roaming\family_tree_maker\html
mkdir %userprofile%\AppData\Roaming\family_tree_maker\notebook
mkdir %userprofile%\AppData\Roaming\family_tree_maker\template

copy template.html %userprofile%\AppData\Roaming\family_tree_maker\template\template.html
copy family_tree_maker.ipynb %userprofile%\AppData\Roaming\family_tree_maker\notebook\family_tree_maker.ipynb
copy family_tree_maker.lnk %userprofile%\desktop\family_tree_maker.lnk