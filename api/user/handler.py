#!/usr/bin/env python3
from flask import g, request
from flask_api import status

from api.core import generate_base_response
from api.core.logs import log_info_with_transaction_id, log_error_with_transaction_id
from api.exceptions import ValidationError
from api.user import User
from api.utils.validations import validate_data_keys, validate_content_keys, validate_phone, validate_email


def create_user():
    log_info_with_transaction_id("[USER]", g.transaction_id, "got new request to create user")

    try:
        data = request.json
        validate_data(data)

        user = User.deserialize(data, True)
        log_info_with_transaction_id("[USER]", g.transaction_id, f"user {user.id} created successfully")

        data = {"user_id": user.id}
        return generate_base_response("CREATED",
                                      201,
                                      g.transaction_id,
                                      "new session successfully created",
                                      data), status.HTTP_201_CREATED
    except ValidationError as e:
        log_error_with_transaction_id("[USER]", g.transaction_id, f"refused, {e}")
        return generate_base_response("ERROR", 400, g.transaction_id, e.message), status.HTTP_400_BAD_REQUEST
    except Exception as e:
        log_error_with_transaction_id("[USER]", g.transaction_id, f"internal server error, {e}")
        return generate_base_response("ERROR",
                                      500,
                                      g.transaction_id,
                                      "internal server error"), status.HTTP_500_INTERNAL_SERVER_ERROR

def validate_data(data: dict):
    keys = {"name", "phone", "email"}
    validate_data_keys(data, keys)
    validate_content_keys(data, keys)
    validate_phone(data.get("phone"))
    validate_email(data.get("email"))
