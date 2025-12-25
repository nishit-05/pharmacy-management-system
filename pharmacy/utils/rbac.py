from functools import wraps
from flask import request, abort

def require_roles(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            role = request.headers.get("X-ROLE")
            if role not in allowed_roles:
                abort(403, description="Access denied")
            return fn(*args, **kwargs)
        return wrapper
    return decorator
