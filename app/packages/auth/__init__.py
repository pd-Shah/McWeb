import functools
from flask import (
    Blueprint,
    session,
    redirect,
    url_for,
)

bp = Blueprint(
    name='auth',
    import_name=__name__,
    url_prefix='/auth',
    )

@bp.route('/logout', methods=["GET", ])
def logout():
    session.clear()
    return redirect(url_for('index.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id', default=None) is None:
            return redirect(url_for('login.login'))
        return view(**kwargs)
    return wrapped_view
