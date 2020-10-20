from app.init import db
from app import create_app

app = create_app()
with app.app_context():
    print("WARNING...")
    print("DEEEP RESTART IS RUNNING...")
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("EVERTYTHINGS IS REMOVED...")
    print("POWERED BY @pd")
