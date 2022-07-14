This is a script to download any Youtube videos when you "CTRL C" the URL of a video
-----------------
How to use it : <br/>
```
pip3 install -r requirements.txt 
cd queue/ 
celery -A main worker --loglevel=info 

      -------------

Open other terminal : 
./YoutubeCopy.py 
```
