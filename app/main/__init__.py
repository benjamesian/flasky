from flask import Blueprint
from app.models import Permission

main = Blueprint('main', __name__)

# this after main to avoid circular dep :$
from . import views, errors

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
