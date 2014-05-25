# Setup PyBox 
import dropbox



app_key = 'YOUR_APP_KEY'
app_secret = 'YOUR_APP_SECRET'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print authorize_url

code = 'JDwPUd1i6wQAAAAAA....Get code from prev step'.strip()

access_token, user_id = flow.finish(code)
print access_token
fout = open('access','w')
fout.write(access_token)

# Access Token
# JDwPUd1i6wQAAAAA.......
access_token = open('access.txt','r').read()
print access_token

# Connect to dropbox
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()


