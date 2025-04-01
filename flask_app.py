from app import create_app
from app.models import db
from flask import redirect

app = create_app('ProductionConfig')

app.route("/")
def redirect():
    return redirect("/api/docs")

with app.app_context():
    # db.drop_all()
    db.create_all()

