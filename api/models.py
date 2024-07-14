from sqlalchemy import Column, Integer, String, ForeignKey, Text, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class Image(Base):
  __tablename__ = 'image'
  id = Column(Integer, primary_key=True, index=True)
  content = Column(LargeBinary, nullable=False)
  description = Column(String(255))
  credit = Column(String(50))

class QuizType(Base):
  __tablename__ = 'quiztype'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  description = Column(String(255), nullable=False)
  slug = Column(String(50), nullable=False)

  quizzes = relationship('Quiz', back_populates='quiz_type')

class Quiz(Base):
  __tablename__ = 'quiz'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(String(255), nullable=False)
  id_quiz_type = Column(Integer, ForeignKey('quiztype.id'), nullable=False)

  quiz_type = relationship('QuizType', back_populates='quizzes')
  questions = relationship('Question', back_populates='quiz')
  results = relationship('Result', back_populates='quiz')

class Question(Base):
  __tablename__ = 'question'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(String(255), nullable=False)
  id_image = Column(Integer, ForeignKey('image.id'))
  id_quiz = Column(Integer, ForeignKey('quiz.id'), nullable=False)

  quiz = relationship('Quiz', back_populates='questions')
  image = relationship('Image')
  options = relationship('QuestionOption', back_populates='question')

class QuestionOption(Base):
  __tablename__ = 'question_option'
  id = Column(Integer, primary_key=True, index=True)
  description = Column(String(100))
  points = Column(Integer, nullable=False)
  id_image = Column(Integer, ForeignKey('image.id'))
  id_question = Column(Integer, ForeignKey('question.id'), nullable=False)

  question = relationship('Question', back_populates='options')
  image = relationship('Image')

class CareerOption(Base):
  __tablename__ = 'career_option'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(Text, nullable=False)
  id_image = Column(Integer, ForeignKey('image.id'), nullable=True)

  image = relationship('Image')
  results = relationship('Result', back_populates='career_option')
  courses = relationship('Course', back_populates='career_option')

class Result(Base):
  __tablename__ = 'result'
  id = Column(Integer, primary_key=True, index=True)
  id_quiz = Column(Integer, ForeignKey('quiz.id'), nullable=False)
  min_points = Column(Integer, nullable=False)
  max_points = Column(Integer, nullable=False)
  id_career_option = Column(Integer, ForeignKey('career_option.id'), nullable=False)

  career_option = relationship('CareerOption', back_populates='results')
  quiz = relationship('Quiz')

class Course(Base):
  __tablename__ = 'course'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(255), nullable=False)
  description = Column(String(255), nullable=False)
  link = Column(String(255), nullable=False)
  image = Column(LargeBinary)
  id_career_option = Column(Integer, ForeignKey('career_option.id'), nullable=False)

  career_option = relationship('CareerOption')
