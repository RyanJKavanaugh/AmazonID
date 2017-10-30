# Go to the tg weg home page and then check for these get requests and see if you are getting errors back from the requests
# 1. Check if the we can access the console from the main page
# 2. Grab the requests and see if there are any 500 errors

# /Users/ryankavanaugh/Desktop/AmazonID

import requests

r = requests.post('http://crc-prod-mn-wf-elb-2010657139.us-west-2.elb.amazonaws.com/tgevents/api/eventMapFeatures/updateMap')
print r

r2 = requests.get('http://crc-prod-mn-wf-elb-2010657139.us-west-2.elb.amazonaws.com/tgrwis/api/stationReports?bounds=%5B-119.70703121874999%2C34.72063588100332%2C-83.80371090624999%2C58.07697787361718%5D&_=1507921095795')
print r2

r3 = requests.post('http://crc-prod-mn-wf-elb-2010657139.us-west-2.elb.amazonaws.com/tgevents/api/eventMapFeatures/updateMap')
print r3

r4 = requests.post('http://crc-prod-mn-wf-elb-2010657139.us-west-2.elb.amazonaws.com/tgevents/api/eventReports?maxPriority=1&maxBeginDateOffset=7200000&minEndDateOffset=0&eventClassifications%5B%5D=roadReports&eventClassifications%5B%5D=metroTrafficMap&eventClassifications%5B%5D=winterDriving&eventClassifications%5B%5D=voxReports&eventClassifications%5B%5D=flooding&_=1507921095796')
print r4

r5 = requests.get('http://crc-prod-mn-wf-elb-2010657139.us-west-2.elb.amazonaws.com/tgrwis/api')
print r5

if r != 200 or r2 != 200 or r3 != 200 or r4 != 200 or r5 != 200:
    print 'The APIs are not functioning properly'
    #assert False

# prepared = req.prepare()

#links = r.xpath("//a/@href").extract()

