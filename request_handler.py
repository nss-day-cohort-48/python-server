import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from locations import get_all_locations
from employees import get_all_employees, get_single_employee
from customers import get_all_customers, get_single_customer


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
        """Parses the url to return the resource and id as a tuple
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

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_locations()}"
        elif resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"

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

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self._set_headers(204)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            update_animal(id, post_body)
        if resource == "employees":
            pass
        if resource == "customers":
            pass

        self.wfile.write("".encode())

    def do_DELETE(self):
        """
        [summary]
        """
        self._set_headers(204)

        (resource_from_url, id_from_url) = self.parse_url(self.path)

        if resource_from_url == "animals":
            delete_animal(id_from_url)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
