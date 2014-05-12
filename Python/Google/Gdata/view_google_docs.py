import gdata.docs.service

# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.service.DocsService()
# Authenticate using your Google Docs email address and password.
client.ClientLogin('kaagleason@gmail.com', 'Gleason20k')

# Query the server for an Atom feed containing a list of your documents.
documents_feed = client.GetDocumentListFeed()
# Loop through the feed and extract each document entry.
for document_entry in documents_feed.entry:
  # Display the title of the document on the command line.
  print document_entry.title.text

import urllib, urllib2, Cookie
from google.appengine.api import urlfetch
from urlparse import urljoin
import logging