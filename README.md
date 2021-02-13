
# Aplikacioni per ngarkimin e fajllave ne Google Drive 

Qellimi kryesor i aplikacionit qe e krijuam ne eshte qe perdoruesit te ia mundesoj qe fajllat me ekstension .doc, .docx, .xls, .xlsx t’i ngarkoj ne nje folder te caktuar  ne Google Drive. Aplikacionin e kemi zhvilluar si GUI (graphical user interface) duke perdorur vetem modulin tkinter te Python. Ky aplikacion permban nje menubar me funksionalitetet perkatese te saj .Menubar permban filemenu e cila ka dy komanda Upload dhe Exit  dhe helpmenu e cila ka komanden help .

# 1. Teknologjitë e përdorura

       Editori: PyCharm IDE
       Gjuha programuese: Python 
       Sistemi Operativ: Windows


# 2.Instalimi i package qe nevojiten per zhvillimin e aplikacionit

Si fillim per te zhvilluar kete aplikacion ne kemi instaluar keto package:

![](img/img19.png)
![](img/img20.png)
![](img/img21.png)
# 3.Ekzekutimi i Aplikacionit
![](img/img17.png)

# 4.Testimet

Pas ekzekutimit te aplikacionit do te na shfaqet dritarja e krijuar dhe meny-ja e saj .
![](img/img1.png)
 
Ne momentin qe klikojm ne file menu do na shfaqen dy opsionet e saj Upload dhe Exit
![](img/img2.png)
Kur zgjedhim opsionin Upload shfaqen dy fusha te cilat perdoruesi duhet t’i plotesoj.Ne fushen e pare duhet te vendos access tokenin per qasjen ne Google Drive dhe ne fushen e dyte folderin specifik ku deshiron ta ruaj fajllin qe e zgjedh .
![](img/img3.png)
![](img/img4.png)
Per te marre access tokenin e Google Drive .Perdoruesi duhet te hap linkun https://developers.google.com/oauthplayground/  te selektoj Drive APIv3 dhe te autorizoj API-ne.
![](img/img5.png)

Perdoruesi pas aplikimit te ketyre hapave pranon access tokenin e tij i cili do te vlej per nje kohe te caktuar nga google .
![](img/img6.png)
Per te shenuar folderin ne te cilin perdoruesi deshiron ta ruaj fajllin e zgjedhur duhet qe te merr ID-ne perkatese te atij folderi .
![](img/img7.png)
