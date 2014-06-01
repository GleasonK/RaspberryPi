import os, dropbox, dPyBox

'''
Make the PyBox stream a dropbox song via a radio frequency.
Need yo change the sox command mp3 file path to where your music files are
Later in command need to locate pifm file
'''

def PyBoxFM_song_query():
    
    # Select song and frequency
    titles = dPyBox.song_query()
    freq = raw_input("Enter radio frequency: ")

    # Play song on radio
    for title in titles:
        os.system('sox -v .9 -t mp3 "/home/pi/Music/PyBox/' + title + '" -t wav --input-buffer 80000 -r 22050 -c 1 - | sudo ~/Applications/PiFM/pifm - ' + freq)
    
    # Delete songs after play
    dPyBox.delete_songs(titles)

if __name__ == '__main__':
    PyBoxFM_song_query()
