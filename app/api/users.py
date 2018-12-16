from sanic.response import json
from sanic import Blueprint

bp = Blueprint("users")


@bp.route("/")
async def hello(request) -> json:
    return json({"hello": "world"})
