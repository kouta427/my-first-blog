git add --all .
set /P USR_INPUT_STR="文字列を入力してください: "
git commit -m %USR_INPUT_STR%
git remote add origin https://github.com/kouta427/my-first-blog.git
git push -u origin master

<<<<<<< HEAD
pause
=======
TIMEOUT /T 10
>>>>>>> 50f87e0d3d7f6dfaaa15beb543b4f17c81c163b7
