from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session,
)
from .forms import LoginForm
from .logics import call_login_api

bp = Blueprint(
        name="login",
        import_name=__name__,
        template_folder="templates",
        url_prefix="/login",
        static_folder="static",
        )

@bp.route("", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        satellite_name = form.satellite_name.data
        server_name = form.server_name.data
        ground_station_name = form.ground_station_name.data
        password = form.password.data
        login_status = call_login_api(
            username,
            satellite_name,
            server_name,
            ground_station_name,
            password, )
        if login_status is None:
            flash(message="User & Password Mixing is Worng.", category="message")
        else:
            session.clear()
            session['user_id'] = login_status['user_id']
            session['role_id'] = login_status['role_id']
            session['username'] = login_status['username']
            return redirect(url_for('dashboard.dashboard'))
    return render_template("login/login.html", form=form, )
