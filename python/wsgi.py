# -*- coding: utf-8 -*-

import socket
import StringIO
import sys
import os
import time

class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )

        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)

        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port

        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connention, client_address = listen_socket.accept()

            # Single-process version
            #self.handle_one_request()
            #self.client_connention.close()
            #time.sleep(60)

            # Multi-process version
            pid = os.fork()
            if pid == 0:
                # child
                # close child copy
                listen_socket.close()
                self.handle_one_request()
                #time.sleep(60)
                os._exit(0)
            else:
                # close parent copy and loop over
                self.client_connention.close()


    def handle_one_request(self):
        self.request_data = request_data = self.client_connention.recv(1024)
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))

        self._parse_request(request_data)

        env = self._get_environ()
        
        # It's the critical part
        result = self.application(env, self._start_response)

        self._finish_response(result)

    def _parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')

        (self.request_method,
         self.path,
         self.request_verion
         ) = request_line.split()

    def _get_environ(self):
        env = {}

        # The following code snippet does not follow PEP8 conventions
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values
        #
        # Required WSGI variables
        env['wsgi.version']         = (1, 0)
        env['wsgi.url_scheme']      = 'http'
        env['wsgi.input']           = StringIO.StringIO(self.request_data)
        env['wsgi.errors']          = sys.stderr
        env['wsgi.multithread']     = False
        env['wsgi.multiprocess']    = False
        env['wsgi.run_once']        = False

        # Required CGI variables
        env['REQUEST_METHOD']       = self.request_method
        env['PATH_INFO']            = self.path
        env['SERVER_NAME']          = self.server_name
        env['SERVER_PORT']          = str(self.server_port)

        return env

    def _start_response(self, status, response_headers, exc_info=None):
        server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        
        self.headers_set = [status, response_headers + server_headers]
        # TODO: `write` callable

    def _finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            self.client_connention.sendall(response)
        finally:
            self.client_connention.close()


SERVER_ADDRESS = (HOST, PORT) = '', 8888

def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()
