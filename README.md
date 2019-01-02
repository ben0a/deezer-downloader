
# this is the download_as_zip branch
1. the music will be downloaded  
2. a zip will be created (enable direcotriy listing for this directory; it is specified in settings.py)  
3. the music dir (mp3s) will be deleted. the zip stays  
----------------------------


# Simple web app writting in flask for downloading songs/albums from deezer.com
- a valid Deezer login credentials are required (free plan)

# Deployment
```
python2 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd app
insert your deezer credentials to app/credentials.py
python app.py
```

# Usage
You can specify the download dir in the settings.py (download_dir). Pressing the download button only downloads the song/album. If you set update_mpd=True in the settings.py the backend will connect to mpd (localhost:6600) and update the music database. Pressing the play button will download the music. If update_mpd=True the mpd database will be updated and the song/album will be added to the playlist. In settings.py music_dir should be the root of the music for mpd. The download_dir is a directory in the music_dir. Both directories should not end with a trailing slash.

# Shortcuts
ctrl-m: focus search bar  
Enter: serach for songs  
Alt+Enter: search for albums  
cbtrl-b: go to / (this is where our ympd is)  

# Disclaimer
I'm not responsible for deezer.py (the actual download code). This is the ugliest code I've ever seen.

# Deployment with ansible (includig mpd and ympd)
https://github.com/kmille/music-ansible

# Screenshot
![Alt text](https://image.ibb.co/cjBC30/screen.png "KISS")
