import argparse
import httplib2
import os
import sys
import time
import re
import RPi.GPIO as GPIO

from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

# Parser for command-line arguments.
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])


# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret. You can see the Client ID
# and Client secret on the APIs page in the Cloud Console:
# <https://cloud.google.com/console#/project/945454513678/apiui>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
  scope=[
      'https://www.googleapis.com/auth/analytics',
      'https://www.googleapis.com/auth/analytics.edit',
      'https://www.googleapis.com/auth/analytics.manage.users',
      'https://www.googleapis.com/auth/analytics.readonly',
    ],
    message=tools.message_if_missing(CLIENT_SECRETS))

def blink(loops, GPIOpin):
   for x in range(loops):
    GPIO.output(GPIOpin, False)
    time.sleep(.2)
    GPIO.output(GPIOpin, True)
    time.sleep(.2)

def main(argv):
  # Parse the command-line flags.
  flags = parser.parse_args(argv[1:])

  # If the credentials don't exist or are invalid run through the native client
  # flow. The Storage object will ensure that if successful the good
  # credentials will get written back to the file.
  storage = file.Storage('sample.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(FLOW, storage, flags)

  # Create an httplib2.Http object to handle our HTTP requests and authorize it
  # with our good Credentials.
  http = httplib2.Http()
  http = credentials.authorize(http)


  ## CONSTRUCT SERVICE OBJECT
  # Construct the service object for the interacting with the Google Analytics API.
  service = discovery.build('analytics', 'v3', http=http)


  ## JUST NEED TO CREATE SERCIVE OBJECT. 

  # 1. Create and Execute a Real Time Report
  # An application can request real-time data by calling the get method on the Analytics service object.
  # The method requires an ids parameter which specifies from which view (profile) to retrieve data.
  # For example, the following code requests real-time data for view (profile) ID 56789.
  
  ## GPIO Pin Setup ##
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(7, GPIO.OUT)  ## Torch
  GPIO.setup(8, GPIO.OUT)  ## 617
  GPIO.setup(11, GPIO.OUT) ## Resume

  ## Loop Variables
  char = 1
  x=1

  while (char):
    try:
      siteStatistics617 = service.data().realtime().get(
        ids='ga:80728025', 
        metrics='ga:activeVisitors',
        dimensions='ga:medium').execute()
        
      siteStatisticsKGR = service.data().realtime().get(
        ids='ga:82545724', 
        metrics='ga:activeVisitors',
        dimensions='ga:medium').execute()

      siteStatisticsTorch = service.data().realtime().get(
        ids='ga:77098906', 
        metrics='ga:activeVisitors',
        dimensions='ga:medium').execute()

      print str(x) + ":"
      active1 = re.search("(?<=activeVisitors': u\')[0-9]+", str(siteStatistics617))
      print "  | 617 Active Viewers:    " + active1.group(0)
      active2 = re.search("(?<=activeVisitors': u\')[0-9]+", str(siteStatisticsKGR))
      print "  | Resume Active Viewers: " + active2.group(0)
      active3 = re.search("(?<=activeVisitors': u\')[0-9]+", str(siteStatisticsTorch))
      print "  | Torch Active Viewers:  " + active3.group(0)

      a1g = int(active1.group(0))
      a2g = int(active2.group(0))
      a3g = int(active3.group(0))

      ## Set up GPIO, need to use pin 7, 8, and 11
      if a3g > 0:  #Torch
        GPIO.output(7, True)
        blink(a3g, 7)
      else:
        GPIO.output(7, False)
        
      if a1g > 0:  #617
        GPIO.output(8, True)
        blink(a1g, 8)
      else:
        GPIO.output(8, False)

      if a2g > 0:  #Resume
        GPIO.output(11, True)
        blink(a2g, 11)
      else:
        GPIO.output(11, False)

      

    except TypeError, error:
      # Handle errors in constructing a query.
      print ('There was an error in constructing your query : %s' % error)

    except http.HttpError, error:
      # Handle API errors.
      print ('Arg, there was an API error : %s : %s' %
        (error.resp.status, error._get_reason()))
    time.sleep(5)
    x+=1



    # 2. Print out the Real-Time Data
    # The components of the report can be printed out as follows:

  # def print_realtime_report(results):
  #   print '**Real-Time Report Response**' 
  #   print_report_info(results)
  #   print_query_info(results.get('query'))
  #   print_profile_info(results.get('profileInfo'))
  #   print_column_headers(results.get('columnHeaders'))
  #   print_data_table(results)
  #   print_totals_for_all_results(results)

  # def print_data_table(results):
  #   print 'Data Table:'
  #   # Print headers.
  #   output = []
  #   for header in results.get('columnHeaders'):
  #     output.append('%30s' % header.get('name'))
  #   print ''.join(output)
  #   # Print rows.
  #   if results.get('rows', []):
  #     for row in results.get('rows'):
  #       output = []
  #       for cell in row:
  #         output.append('%30s' % cell)
  #       print ''.join(output)
  #   else:
  #     print 'No Results Found'

  # def print_column_headers(headers):
  #   print 'Column Headers:'
  #   for header in headers:
  #     print 'Column name           = %s' % header.get('name')
  #     print 'Column Type           = %s' % header.get('columnType')
  #     print 'Column Data Type      = %s' % header.get('dataType')

  # def print_query_info(query):
  #   if query:
  #     print 'Query Info:'
  #     print 'Ids                   = %s' % query.get('ids')
  #     print 'Metrics:              = %s' % query.get('metrics')
  #     print 'Dimensions            = %s' % query.get('dimensions')
  #     print 'Sort                  = %s' % query.get('sort')
  #     print 'Filters               = %s' % query.get('filters')
  #     print 'Max results           = %s' % query.get('max-results')

  # def print_profile_info(profile_info):
  #   if profile_info:
  #     print 'Profile Info:'
  #     print 'Account ID            = %s' % profile_info.get('accountId')
  #     print 'Web Property ID       = %s' % profile_info.get('webPropertyId')
  #     print 'Profile ID            = %s' % profile_info.get('profileId')
  #     print 'Profile Name          = %s' % profile_info.get('profileName')
  #     print 'Table Id              = %s' % profile_info.get('tableId')

  # def print_report_info(results):
  #   print 'Kind                    = %s' % results.get('kind')
  #   print 'ID                      = %s' % results.get('id')
  #   print 'Self Link               = %s' % results.get('selfLink')
  #   print 'Total Results           = %s' % results.get('totalResults')

  # def print_totals_for_all_results(results):
  #   totals = results.get('totalsForAllResults')
  #   for metric_name, metric_total in totals.iteritems():
  #     print 'Metric Name  = %s' % metric_name
  #     print 'Metric Total = %s' % metric_total


if __name__ == '__main__':
  main(sys.argv)
