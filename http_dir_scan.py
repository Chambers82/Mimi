# Offensive Security Software
# SSE Program
# Attack: HTTP Directory Scanner
# Date: January 31, 2016
# Description:  Web servers typically have a directory available that's
# more or less hidden from site visitors.  With a dictionary attack
# combined with a directory traversal attack, we can attempt to discover
# hidden files and directories.


import sys
import getopt
import httplib2

#Get URL from server
def surf(url, query):
    print "GET " + query
    try:
        response, content = web_client.request(url)
        if response.status == 200:
            print "FOUND " + query
    except httplib2.ServerNotFoundError:
        print "Got error for " + url + \
              ": Server not found"
        sys.exit(1)


#Dictionary file
query_file = "http_dir_scan.rec"

# Target http server and port
host = "localhost"
port = 80

#Run in file mode?
file_mode = False

#Parsing parameter
try:
    cmd_opts = "f:Fh:p:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    print sys.argv[0] + """
    -f <query_file>
    -F (file_mode)
    -h <host>
    -p <port> """
    sys.exit(0)

for opt in opts:
    if opt[0] == "-f":
        query_file = opt[1]
    elif opt[0] == "-F":
        file_mode = True
    elif opt[0] == "-h":
        host = opt[1]
    elif opt[0] == "-p":
        port = opt[1]

if port == 443:
    url = "http://" + host
elif port != 80:
    url = "http://" + host + ":" + port
else:
    url = "http://" + host


#Pattern will be added to each query
salts = ('~', '~1', '.back', '.bak', '.old', '.orig', '_backup')

#Get the webbrowser object
web_client = httplib2.Http()

#Read dictionary and handle each query
for query in open(query_file):
    query = query.strip("\n")

    #Try dictionary traversal
    for dir_sep in ['/', '//', '/test/../']:
        url += dir_sep + query

        if file_mode:
            for salt in salts:
                url += salt
                surf(url,
                     dir_sep + query + salt)
        else:
            surf(url, dir_sep, query)
            
