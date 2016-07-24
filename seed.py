"""Utility file to seed readcoach database from data in seed_data_prod/"""

from sqlalchemy import func

from model import *
from server import app


def load_users():
    """Load coaches from d.coach into database."""

    print "Users"

    User.query.delete()

    for row in open("sample_data/safebot_users.txt"):
        row  = row.rstrip()
        user_data = row.split(",")
        for i in user_data:
            user = User(first_name=first_name, last_name=last_name, contact_num=contact_num)

            db.session.add(user)

    db.session.commit()

    print "Sample Users Seeded"


def load_friends():
    """Load safebot friends into database."""

    print "Safebot Friends"

    for row in open("sample_data/safebot_friends.txt")):
        row = row.rstrip()
        friend_data = row.split(",")
        for i in friend_data:
            friend = Friend(first_name=first_name, last_name=last_name, contact_num=contact_num)

            db.session.add(friend)

    db.session.commit()

    print "Sample Friends Seeded"


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_friends()
