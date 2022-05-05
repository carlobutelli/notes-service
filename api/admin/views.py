from flasgger import swag_from
from flask import Blueprint, jsonify, g

from flask import current_app as app

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/ping")
@swag_from("/api/docs/admin.yml")
def ping():
    transaction_id = g.transaction_id
    app.logger.info("[PING] {}: got new request to ping app".format(transaction_id))
    return jsonify("pong"), 200
