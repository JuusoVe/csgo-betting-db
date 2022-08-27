from functools import wraps
from os import getenv
from flask import request, abort

API_KEY = getenv("FLASK_API_KEY")


def require_auth(route_function):
    """
    @param The route function to protect by requiring an Authorization Header.

    @return Auth-protected version of the route function.

    Middleware that checks that request has 'Authorization' header set and ensures it
    matches FLASK_API_KEY env variable.

    Usage: import this function and decorate the handler with @require_auth. Decorator must be
    between the route decorator and handler function.
    """

    @wraps(route_function)
    def route_function_with_auth(*args, **kwargs):
        if (
            request.headers.get("Authorization")
            and request.headers.get("Authorization").split()[1] == API_KEY
        ):
            return route_function(*args, **kwargs)
        else:
            abort(401)

    return route_function_with_auth

