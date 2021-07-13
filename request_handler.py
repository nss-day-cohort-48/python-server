import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal, create_animal


class HandleRequests(BaseHTTPRequestHandler):
    """Handles requests to the server for GET, POST, PUT, and Delete
    """

    def _set_headers(self, status):
        """Sets the headers of the response

        Args:
            status (number): the status code to be returned
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def parse_url(self, path):
        """Parses the url to return the resource and id
        """
        path_params = path.split('/')
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handles the GET requests for the server
        """
        self._set_headers(200)
        print(self.path)

        (resource, id) = self.parse_url(self.path)
        response = f'{[]}'

        if resource == 'animals':
            if id is not None:
                response = f'{get_single_animal(id)}'
            else:
                response = f'{get_all_animals()}'

        self.wfile.write(response.encode())

    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path)

        response = None

        if resource == "animals":
            response = create_animal(post_body)
        if resource == "customers":
            response = {}

        self.wfile.write(f'{response}'.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self.do_POST()


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
