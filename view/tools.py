from functools import wraps
from flask import session as flask_session, flash, redirect, url_for


def login_required(default_page):
    def decorator(route):
        @wraps(route)
        def wrapper(*args, **kwargs):
            if 'username' in flask_session:
                return route(*args, **kwargs)
            flash('Du måste vara inloggad för att visa denna sidan')
            return redirect(url_for(default_page))
        return wrapper
    return decorator


def sign_in_status():
    return 'username' in flask_session




