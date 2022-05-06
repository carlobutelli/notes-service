#!/usr/bin/env python3
from flask import jsonify


def generate_base_response(status: str, status_code: int, transaction_id: str, message: str = "", data: {} = None):  # pragma: no cover
    meta = {
        "status": status,
        "status_code": status_code,
        "transaction_id": transaction_id,
        "message": message
    }
    if data:
        return jsonify(data=data, meta=meta)
    return jsonify(meta=meta)
