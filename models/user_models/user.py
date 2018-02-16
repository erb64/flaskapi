from config.db import db

class UserModel(db.Model):
    """This class creates the models for a user object"""

    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))
    username = db.Column('username',db.String(30))
    password = db.Column('password', db.String(100))
    register_date = db.Column('register_date', db.TIMESTAMP, default=db.func.current_timestamp)
 
    def __init__(self, new_user):
        #this method is used to initialize user objects

        self.name = new_user['name']
        self.email = new_user['email']
        self.username = new_user['username']
        self.password = new_user['password']
        self.register_date = new_user['register_date']

    def __repr__(self):
        """This method returns a string representation of the user object"""

        return 'UserModel %r' % self.username

    def json(self):
        """This method returns a json representation of the user object"""

        # parse date object as datetime string
        if self.register_date:
            str_register_date = self.register_date.strftime('%B %d, %Y at %I:%M%p')
        else:
            str_register_date = None

        return {'id': self.id, 'name': self.name, 'email': self.email, 'username': self.username,
                'password': self.password, 'register_date': str_register_date
                }

    def save_to_db(self):
        """This methods saves the changes made to a user object and commits those changes to the database"""

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """This methods deletes a user object and commits those changes to the database"""

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        """This method is used to find a user by the given id"""
        return cls.query.filter_by(username=username).first()
    

db.create_all()
db.session.commit()
