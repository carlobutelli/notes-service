#!/usr/bin/env python3
from flasgger import swag_from
from flask import Blueprint, request

from api.user.handler import create_user

user = Blueprint("user", __name__, url_prefix="/user")


@user.route('', methods=['POST'])
@swag_from("/api/docs/user.yml")
def user_create_route():
    if request.method == "POST":
        return create_user()
