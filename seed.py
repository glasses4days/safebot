
from model import connect_to_db, db, User, Friend
from flask_sqlalchemy import SQLAlchemy
from server import app


def sample_data():
	"""create sample data"""

	# In case this is run more than once, dump existing data
	db.drop_all()
	db.create_all()

	# Add sample Uers
	user1 = User(first_name='pablo', last_name='penguin', contact_num='5109266821', nvmd_code='123')

	db.session.add_all([user1])
	db.session.commit()

	pablo_id = User.query.filter_by(first_name='pablo').first().user_id

	# Add sample friends
	friend1 = Friendfirst_name='pablo', last_name='penguin', contact_num='5109266821')

	db.session.add_all([friend1])
	db.session.commit()

connect_to_db(app)
print "Connected to DB."

sample_data()

print "Sample Data created"
