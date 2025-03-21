from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from models.database import db

def create_app():
    app = Flask(__name__ , template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    from controllers.controllers import home, login, register, admin_dashboard, user_dashboard
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
