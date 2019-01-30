rm db.sqlite3.bu
mv db.sqlite3 db.sqlite3.bu

rsync  -avz -e ssh * root@geilenkotten.homeunix.org:/home/kaam/affinity/.


mv db.sqlite3.bu db.sqlite3

