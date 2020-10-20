from os import makedirs
from flask import (
    Flask,
)
from settings import config
from app.init import (
    migrate,
    db,
)
from app.packages import index
from app.packages import login
from app.packages import dashboard
from app.packages import auth

def create_app():
    app = Flask(
            import_name=__name__,
            instance_relative_config=True,
        )
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db=db)
    try:
        makedirs(
            app.instance_path,
            exist_ok=True,
        )
    except Exception as e:
        print(e)

    @app.route("/")
    def test():
        return "hI FroM pd!"

    app.register_blueprint(index.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(auth.bp)

    @app.template_filter("telecommnad_display")
    def telecommnad_display_filter(telecommands):
        return [obj.TelecommandName for obj in telecommands]

    return app
