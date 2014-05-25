# Download files from dropbox

import dropbox, os

'''
Need to locate your music files and tweak them accordingly.
Local and dropbox.
'''

def song_query():
    # Log in
    pwd = '/home/pi/Applications/PyBox/'
    access_token = open(pwd + 'access.txt','r').read()
    client = dropbox.client.DropboxClient(access_token)

    # print 'Account info: ', client.account_info()
    
    # Query song and find
    song = raw_input("Enter song query: ")
    search_data = client.search('/Music/', song)
    folder_metadata = client.metadata('/Music/')
    index = 0
    print
    print "Select index to download:"
    print "==================================="
    for item in  search_data:
        print index, item.get("path").replace('/Music/','')
	index+=1
    print "==================================="
    choices = raw_input("Index selection (CSV or 'None'): ")
    choices = choices.replace(' ','').split(',')
    song_titles=[]

    # Choices and download
    for choice in choices:
        if choice.lower() == 'none':
    	    new_query_yn = raw_input("Try new query? (y/n) ")
	    if new_query_yn.lower() == "y":
	        song_query()
        else:
	    fname = search_data[int(choice)].get('path')
	    path,fbase = os.path.split(fname)
            _,ext = os.path.splitext(fbase)
            print "File: " + choice, fname 
	    save_title = raw_input('Enter song save title: ') + ext
	    if save_title == ext:
	        save_title = fbase
            fout = open("/home/pi/Music/PyBox/" + save_title, 'wb')
	    song_titles.append(save_title)
	    try:
	        with client.get_file(fname) as f:
	            fout.write(f.read())
            except:
	        print "Error: File not found"
    return song_titles

# Delete songs after play
def delete_songs(songs):
    yn = raw_input("Delete files? (y/n) ")
    if yn.lower()=="y":
        for song in songs:
            os.system('rm "/home/pi/Music/PyBox/' + song + '"')
    else:
	os.system("python ~/Applications/BashTube/cleanupMP3.py")
	
if __name__ == '__main__':
    song_query()
