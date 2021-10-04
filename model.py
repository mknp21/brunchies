"""Models for brunch locator app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Columm(db.String(50), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    pw = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.String(10))

    def __repr__(self):
        return f"User name={self.name} email={self.email}"

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)