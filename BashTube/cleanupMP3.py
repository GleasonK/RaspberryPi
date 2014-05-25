import os

# echo $(($(( $(date +%s)-$(date +%s --date=\"$(stat * | grep -m2 Access | sed '1d' | sed 's/Access: //g')\")))/60))
path = "~/Music/YTDL/"
files = os.popen("ls \'" + path + "'").read().rsplit()
for fname in files:
	# time = int(os.popen("echo $(($(( $(date +%s)-$(date +%s --date=\"$(stat "+fname+" | grep -m2 Access | sed '1d' | sed 's/Access: //g')\")))/60))").read())
	if int(os.popen("echo $(($(( $(date +%s)-$(date +%s --date=\"$(stat \'"+path+fname+"\' | grep -m2 Access | sed '1d' | sed 's/Access: //g')\")))/86400))").read()) > 5:
		os.system('rm '+path+fname)
