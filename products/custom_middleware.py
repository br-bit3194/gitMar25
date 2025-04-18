class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Do something before the request
        print("First middleware before request")

        # Create some JSON data
        data = {
            "user": "john_doe",
            "role": "admin"
        }

        # modify and pass to second middleware
        request.my_json_data = data

        # Call the next middleware or get_
        response = self.get_response(request)

        # Do something after the request
        print("First middleware after request")

        return response

class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # modify and pass to second middleware
        data = getattr(request, 'my_json_data', None)
        print(f"second middleware: {data}")

        # Call the next middleware or get_
        response = self.get_response(request)

        return response