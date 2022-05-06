#!/usr/bin/env python3
from flask import current_app as app


def log_info_with_transaction_id(module: str = None, transaction_id: str = None, message: str = None):  # pragma: no cover
    app.logger.info(f"{module} {transaction_id}: {message}")

def log_error_with_transaction_id(module: str = None, transaction_id: str = None, message:str = None):  # pragma: no cover
    app.logger.error(f"{module} {transaction_id}: {message}")
