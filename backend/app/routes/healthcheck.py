from flask import Blueprint, jsonify, Response

bp = Blueprint('healthcheck', __name__, url_prefix='/api')

@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status":"ok"})

@bp.route('/sitemap.xml')
def sitemap():
    return Response(open('/app/app/misc/sitemap.xml').read(), mimetype='application/xml')