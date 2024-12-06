from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Base class for our models
Base = declarative_base()

# Subject model
class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String)  # You can store the image URL or file path
    
    # Relationship with Topic
    topics = relationship("Topic", back_populates="subject",cascade="all,delete-orphan")

# Topic model
class Topic(Base):
    __tablename__ = "topics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    
    # Relationship with Subject
    subject = relationship("Subject", back_populates="topics")
    
    # Relationship with Subtopic and ReadingResource
    subtopics = relationship("Subtopic", back_populates="topic",cascade="all,delete-orphan")
    reading_resources = relationship("ReadingResource", back_populates="topic",cascade="all,delete-orphan")

# Subtopic model
class Subtopic(Base):
    __tablename__ = "subtopics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    
    # Relationship with Topic
    topic = relationship("Topic", back_populates="subtopics")

# ReadingResource model
class ReadingResource(Base):
    __tablename__ = "reading_resources"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # Type of resource (e.g., PDF, video)
    url = Column(String)  # URL or file path
    topic_id = Column(Integer, ForeignKey("topics.id"))
    
    # Relationship with Topic
    topic = relationship("Topic", back_populates="reading_resources")