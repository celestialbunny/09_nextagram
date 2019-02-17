from peewee import Model, CharField, DateTimeField, BooleanField, datetime, IntegrityError
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase('name_of_db')

class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=100)
	joined_at = DateTimeField(default=datetime.datetime.now)
	is_admin = BooleanField(default=False)

	class Meta:
		database = db
		# To view all "users" who has signed up
		# the minus sign denotes sort by desc
		order_by = ('-joined_at',)

	# cls instead of user is being used because:
	# If we need to create a 'User' in order to try to validate, it will be absurd as why create an INVALID user in the first place?
	# Hence some other methods needed to be used instead for Verifying purposes
	# CLS = class, so using a test Class to test the logic and it will be destroyed but the CORRECT User object will be created after testing purpose(s)
	@classmethod
	def create_user(cls, username, email, password, admin=False):
		try:
			cls.create(
				username=username,
				email=email,
				password=generate_password_hash(password),
				is_admin=admin
			)
		# Integrity error will be thrown if the username and email are NOT actually unique (duplicated in other words)
		except IntegrityError:
			raise ValueError("Either username and/or email has been taken")

def initialize():
	db.connect()
	db.create_tables([User], safe=True)
	db.close()