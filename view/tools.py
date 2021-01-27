from functools import wraps
from flask import session as flask_session, flash, redirect, url_for
import html


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


def unescape_dict(d):
    return {k: html.unescape(v) for k, v in d.items()}

class GameInit:
    def __init__(self, category, no):
        self.category = category
        self.no = no

    def no(self):
        return self.no

    def category(self):
        return self.category



