from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata = metadata)

#models
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
      
class Houseplan(db.Model, SerializerMixin):
    __tablename__ = 'houseplans'
    
    id = db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(255), nullable=False)
    stories=db.Column(db.Integer, nullable=False)
    baths=db.Column(db.Integer, nullable=False)
    baths=db.Column(db.Integer, nullable=False)
    bedrooms=db.Column(db.Integer, nullable=False)
    length=db.Column(db.Integer, nullable=False)
    width=db.Column(db.Integer, nullable=False)
    style=db.Column(db.String(255), nullable=False)

class Favourite(db.Model, SerializerMixin):
    __tablename__ = 'favourites'
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer , db.ForeignKey)
    houseplan_id=db.Column(db.Integer, db.ForeignKey)
    
class Blog(db.Model, SerializerMixin):
    __tablename__='blogs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    text = Column(Text, nullable=False)
    image = Column(String(255))
    
    