git add --all .
set /P USR_INPUT_STR="•¶Žš—ñ‚ð“ü—Í‚µ‚Ä‚­‚¾‚³‚¢: "
git commit -m %USR_INPUT_STR%
git remote add origin https://github.com/kouta427/my-first-blog.git
git push -u origin master

pause
