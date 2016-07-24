"""Models and database functions for Safebot project"""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """Safebot User details"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    contact_num = db.Column(db.Integer, nullable=True)
    nvmd_code = db.Column(db.String(3), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s first_name=%s last_name=%s contact_num=%s>" % (self.user_id, self.first_name, self.last_name, self.contact_num)


class Friend(db.Model):
    """Friend of Safebot User"""

    __tablename__ = "friends"

    friend_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    contact_num = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationships
    user = db.relationship('User')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Friend friend_id=%s first_name=%s last_name=%s contact_num=%s>" % (
            self.friend_id, self.first_name, self.last_name, self.contact_num)


class Unsafe(db.Model):
    """Unsafe calls"""

    __tablename__ = "unsafes"

    unsafe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    datetime = db.Column(db.DateTime)
    geo_location = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sms_sent = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Unsafe unsafe_id=%s datetime=%s geo_location=%s sms_sent=%s user_id=%s>" % (self.location_id, self.datetime, self.geo_location, self.sms_sent, self.user_id)


##############################################################################

def connect_to_db(app, db_uri="postgresql:///safebots"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    print "Connected to DB."

    # db.create_all()
