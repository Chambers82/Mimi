# Offensive Security Software
# SSE Program
# Attack: Cookie Manipulation
# Date: January 31, 2016
# Description:
'''
SessionId's are an HTTP hack that developers use to make up for HTTP being a
stateless protocol.  Session Id's are sent with every request to identify
a client.  They are valid for one session and deleted after logout.

If the SessionId is saved, it's called a cookie.  Cookie's are associated with
every request belonging to a domain (or the host that generated the cookie).

Cookies are now used to track a user by implementing them in adverts to analyze
consumer's behavior.  
'''

import sys
import httplib2

if len(sys.argv) < 3:
    print sys.argv[0] + ": &lt;url&gt; <key> <value>"
    sys.exit(1)

webclient = httplib2.Http()
headers = {'Cookie': sys.argv[2] + '=' + sys.argv[3]}
response, content = webclient.request(sys.argv[1],
                                      'GET',
                                      headers=headers)
print content
