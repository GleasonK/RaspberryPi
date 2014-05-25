## Download files from dropbox

import dropbox, dPyBox, os

# Different players for different filetypes
def playExtension(path, title):
    _,ext = os.path.splitext(title)
    if ext in [".mp3"]:
    	os.system('mpg321 "' + path + title + '"')
    elif ext in [".wav", ".au"]:
        os.system('aplay "' + path + title + '"')
    else:
	os.system('omxplayer "' + path + title + '"')
	

def play_PyBox():
    # Download and get title
    titles = dPyBox.song_query()

    # Play from Unix
    path = "/home/pi/Music/PyBox/"
    for title in titles:
        playExtension(path, title)
    
    # Delete files?
    dPyBox.delete_songs(titles)

if __name__ == "__main__":
    play_PyBox()
