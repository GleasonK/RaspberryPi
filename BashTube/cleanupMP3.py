import os

# echo $(($(( $(date +%s)-$(date +%s --date=\"$(stat * | grep -m2 Access | sed '1d' | sed 's/Access: //g')\")))/60))

# Clean old files
def clean_files(path):
    files = os.popen("ls " + path).read().rsplit('\n')
    files.__delitem__(len(files)-1)
    print files
    for fname in files:
        if int(os.popen("echo $(($(( $(date +%s)-$(date +%s --date=\"$(stat \""+path+fname+"\" | grep -m2 Access | sed '1d' | sed 's/Access: //g')\")))/86400))").read()) > 5:
            os.system('rm "'+path+fname+'"')


if __name__ == '__main__':
    # Set paths
    paths = ["/home/pi/Music/YTDL/", "/home/pi/Music/PyBox/"]
    
    # Clean paths
    for path in paths:
        clean_files(path)
