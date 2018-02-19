from config.db import db
import datetime

class TaskModel(db.Model):
    """This class creates the models for a user object"""

    __tablename__ = 'tasks'

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100))
    author = db.Column('author', db.String(100))
    body = db.Column('body', db.Text)
    create_date = db.Column('create_date', db.TIMESTAMP, default=db.func.current_timestamp)
    active = db.Column('active', db.Boolean(), default=True)

    def __init__(self, new_task):
        #this method is used to initialize task objects
        self.title = new_task['title']
        self.author = new_task['author']
        self.body = new_task['body']
        self.create_date = datetime.datetime.now
        self.active = True

    def __repr__(self):
        """This method returns a string representation of the user object"""

        return 'TaskModel %r' % self.id

    def json(self):
        """This method returns a json representation of the user object"""

        # parse date object as datetime string
        if self.create_date:
            str_create_date = self.create_date.strftime('%B %d, %Y at %I:%M%p')
        else:
            str_create_date = None

        return {'id': self.id, 'title' : self.title, 'author': self.author, 'body': self.body, 
                'create_date': str_create_date, 'active': self.active }

    def save_to_db(self):
        """This methods saves the changes made to a task object and commits those changes to the database"""

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """This methods deletes a user object and commits those changes to the database"""

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        """This method is used to find a task by the given task id"""
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_author(cls, author):
        """This method is used to find a task by the given task author"""
        return cls.query.filter_by(author=author).all()    

db.create_all()
db.session.commit()
