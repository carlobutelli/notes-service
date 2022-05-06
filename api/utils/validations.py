#!/usr/bin/env python3
import re
from flask import g

from api.core.logs import log_error_with_transaction_id
from api.exceptions import ValidationError


def validate_data_keys(data: dict, keys: set):
    if not data:
        log_error_with_transaction_id("[VALIDATION]", g.transaction_id, "data not found")
        raise ValidationError("data not found", list(keys))

    # check if all the data is present
    if not keys.issubset(data.keys()):
        log_error_with_transaction_id("[VALIDATION]", g.transaction_id, "incorrect keys on provided dict")
        raise ValidationError("missing fields",
                              list(keys - set(data.keys())))


def validate_content_keys(data: dict, keys: set):
    if not data:
        log_error_with_transaction_id("[VALIDATION]", g.transaction_id, "data not found")
        raise ValidationError("data not found", list(keys))

    # check that all keys are not empty
    for key in keys:
        value = data.get(key)
        if value is None or value is "":
            raise ValidationError("field empty", [key])


def validate_phone(phone: str):
    """
    It evaluates numbers where xx is the country code in the shape of
    - +xx{6, 14}
    - 00xx{6, 14}
    or a NON international number starting with 0
    - 0{6, 14}
    :param phone: phone number to be verified
    :return: True or raise an exception
    """
    regular_expression = "^(?:(?:00|\+)\d{4}|0)[0-9](?:\d{6,14})$"
    if not re.match(regular_expression, phone, flags=0):
        log_error_with_transaction_id("[VALIDATION]", g.transaction_id, f"phone '{phone}' format not valid")
        raise ValidationError(f"phone '{phone}' format not valid")
    return True


def validate_email(email: str):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        raise ValidationError(f"email '{email}' format not valid")
    return True
