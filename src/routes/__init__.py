from flask import Blueprint

bp = Blueprint('routes', __name__)

from .campers import *
from .activities import *
from .signups import *