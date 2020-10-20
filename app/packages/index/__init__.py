from flask import (
    Blueprint,
    render_template,
)


bp = Blueprint(
    name="index",
    import_name=__name__,
    url_prefix="/index",
    template_folder="templates",
    static_folder="static",
)


@bp.route("", methods=["GET"])
def index():
    return render_template("index/index.html")
