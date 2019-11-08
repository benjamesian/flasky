from flask import Blueprint

main = Blueprint('main', __name__)

# this after main to avoid circular dep :$
from . import views, errors
