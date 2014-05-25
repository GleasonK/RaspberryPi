## Script for Uploading
import dropbox


def upload_file():

    fname = raw_input("Enter the file name: ")
    save_loc = '/' + raw_input("Enter the save location")

    access_token = open('access.txt','r').read()
    client = dropbox.client.DropboxClient(access_token)
    # print 'Account info: ', client.account_info()

    fin = open(fname,'rb')
    response = client.put_file(save_loc, fin)
    print "Uploaded:", response

if __name__ == '__main__':
    upload_file()
