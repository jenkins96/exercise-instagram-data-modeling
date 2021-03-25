import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    type_of_account = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__="follower"
    FollowerID = Column(Integer, primary_key=True)
    # userfromid; usertoid

class Post(Base):
    __tablename__="post"
    PostID = Column(Integer, primary_key=True)
    # userid as FK

class Media(Base):
    __tablename__="media"
    MediaID = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    #postid as FK

class Like(Base):
    __tablename__="like"
    LikeID = Column(Integer, primary_key=True)
    #userid as FK && postid as FK

class Share(Base):
    __tablename__="share"
    ShareID = Column(Integer, primary_key=True)
    #userid as FK && postid as FK

class Comment(Base):
    __tablename__='comment'
     CommentID = Column(Integer, primary_key=True)
     text_comment = Column(String(250), nullable=False)
     # author id == userid as FK && postid as FK

class Save_Post(Base):
    __tablename__="save_post"
     Save_PostID = Column(Integer, primary_key=True)
     #userid as FK && postid as FK

class Products(Base):
    __tablename__="products"
     ProductsID = Column(Integer, primary_key=True)
     prod_name_1 = Column(String(250), nullable=True)
     prod_name_2 = Column(String(250), nullable=True)
     amount = Column(Integer)
     #userid as FK

class Transactions(Base):
    __tablename__="transactions"
    TransactionsID = Column(Integer, primary_key=True)
    


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')