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
    # Relationship
    like = relationship("Like")
    user_from_id_follower  = relationship("Follower")
    user_to_id_follower = relationship("Follower")
    post = relationship("Post")
    share = relationship("Share")
    comment = relationship("Comment")
    save_post = relationship("Save_Post")
    products = relationship("Products")
    
   

class Follower(Base):
    __tablename__ = "follower"
    FollowerID = Column(Integer, primary_key=True)
    # Relationships
    user_from_id = relationship("User")
    user_to_id = relationship("User")
    

class Post(Base):
    __tablename__ = "post"
    PostID = Column(Integer, primary_key=True)
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("User.UserID"))
    # Relationship
    like_post = relationship("Like")
    post_id_media = relationship("Media")
    post_id_comment = relationship("Comment")
    post_id_save_post = relationship("Save_Post")
    

class Media(Base):
    __tablename__ = "media"
    MediaID = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    # Foreign Key
    post_id = Column(Integer, ForeignKey("Post.PostID"))
    

class Like(Base):
    __tablename__ = "like"
    LikeID = Column(Integer, primary_key=True)
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("User.UserID"))
    post_id = Column(Integer, ForeignKey("Post.PostID"))
    user_id = Column(Integer, ForeignKey("User.UserID"))
    #userid as FK && postid as FK

class Share(Base):
    __tablename__ = "share"
    ShareID = Column(Integer, primary_key=True)
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("User.UserID"))
    #userid as FK && postid as FK

class Comment(Base):
    __tablename__ = 'comment'
    CommentID = Column(Integer, primary_key=True)
    text_comment = Column(String(250), nullable=False)
    # Foreign Keys
    author_id = Column(Integer, ForeignKey("User.UserID"))
    post_id = Column(Integer, ForeignKey("Post.PostID"))

class Save_Post(Base):
    __tablename__ = "save_post"
    Save_PostID = Column(Integer, primary_key=True)
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("User.UserID"))
    post_id = Column(Integer, ForeignKey("Post.PostID"))
    #userid as FK && postid as FK

class Products(Base):
    __tablename__ = "products"
    ProductsID = Column(Integer, primary_key=True)
    prod_name_1 = Column(String(250), nullable=True)
    prod_name_2 = Column(String(250), nullable=True)
    amount = Column(Integer)
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("User.UserID"))
    #userid as FK

class Transactions(Base):
    __tablename__ = "transactions"
    TransactionsID = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')