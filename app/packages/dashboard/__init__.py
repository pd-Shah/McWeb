from flask import (
    render_template,
    Blueprint,
    session,
    redirect,
    url_for,
    flash,
    request,
    abort,
)
from app.packages.auth import login_required
from .logics import (
    get_mission_list_api,
    get_telecommands_list_api,
    get_pus_services_list_api,
    get_pus_telecommands_api,
    create_mission_template,
    get_mto_data_source,
)

bp = Blueprint(
    name="dashboard",
    import_name=__name__,
    static_folder="static",
    template_folder="templates",
    url_prefix='/dashboard',
)


@bp.route("", methods=["GET", ])
@login_required
def dashboard():
    return render_template("dashboard/dashboard.html")


@bp.route("/icons", methods=["GET", ])
@login_required
def icons():
    return render_template("dashboard/icons.html")


@bp.route("/maps", methods=["GET", ])
@login_required
def maps():
    return render_template("dashboard/maps.html")


@bp.route("/notifications", methods=["GET", ])
@login_required
def notifications():
    return render_template("dashboard/notifications.html")


@bp.route("/table", methods=["GET", ])
@login_required
def table():
    return render_template("dashboard/table.html")


@bp.route("/template", methods=["GET", ])
@login_required
def template():
    return render_template("dashboard/template.html")


@bp.route("/typography", methods=["GET", ])
@login_required
def typography():
    return render_template("dashboard/typography.html")


@bp.route("/upgrade", methods=["GET", ])
@login_required
def upgrade():
    return render_template("dashboard/upgrade.html")


@bp.route("/user", methods=["GET", ])
@login_required
def user():
    return render_template("dashboard/user.html")


@bp.route("/mission-template", methods=["GET", ])
@login_required
def mission_template():
    missions = get_mission_list_api()
    telecommands = get_telecommands_list_api(
        [mission.SequenceId for mission in missions]
    )
    return render_template(
        "dashboard/mission_template.html",
        missions=missions,
        telecommands=telecommands,
    )


@bp.route("/view-template", methods=["GET", ])
@login_required
def view_template():
    return render_template("dashboard/view_template.html")


@bp.route("/create-template", methods=["GET", "POST"])
@login_required
def create_template():
    pus_list = get_pus_services_list_api()
    pus_telecommand_name_list = get_pus_telecommands_api(pus_list)
    return render_template(
        "dashboard/create_template.html",
        pus_list=pus_list,
        pus_telecommand_name_list=pus_telecommand_name_list
    )


@bp.route("/insert-mission-template", methods=["POST", ])
@login_required
def insert_mission_template():
    if request.method == "POST":
        json_request = request.get_json()
        telecommands = json_request.get("telecommands", None)
        description = json_request.get("description", None)
        mission_name = json_request.get("mission_name", None)
        insert_status = create_mission_template(
            mission_name,
            description,
            telecommands,
        )
        if insert_status["errorStatus"]:
            flash(insert_status["Message"])
            abort(503, insert_status["Message"])
        else:
            return insert_status["Message"], 200


@bp.route("/edit-mission", methods=["GET", ])
@login_required
def edit_mission():
    return render_template("dashboard/edit_mission.html")


@bp.route("/prepared-mission", methods=["GET", ])
@login_required
def Prepared_mission():
    return render_template("dashboard/Prepared_mission.html")


@bp.route("/edit_prepared-mission", methods=["GET", ])
@login_required
def edit_prepared_mission():
    return render_template("dashboard/edit_prepared_mission.html")


@bp.route("/view_prepared-mission", methods=["GET", ])
@login_required
def view_prepared_mission():
    return render_template("dashboard/view_prepared_mission.html")


@bp.route("/scheduled_mission", methods=["GET", ])
@login_required
def scheduled_mission():
    return render_template("dashboard/scheduled_mission.html")


@bp.route("/onlinecommadn", methods=["GET", ])
@login_required
def Online_command():
    return render_template("dashboard/OnlineCommand.html")

@bp.route("/telemetry", methods=["GET", ])
@login_required
def Telemtry():
    return render_template("dashboard/Telemetry.html")

@bp.route("/mto", methods=["GET", ])
@login_required
def Mto():
    data_source = get_mto_data_source()
    if data_source["errorMessage"]:
        flash(data_source["errorMessage"])
        abort(503, data_source["errorMessage"])
    else:
        return render_template(
            "dashboard/mto.html", 
            data_source=data_source["DataSource"],
            current_MTO=data_source["currentMtoTime"],
        )
