from sqlalchemy import Column, Integer, String, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class Image(Base):
  __tablename__ = "image"

  id = Column(Integer, primary_key=True, index=True)
  content = Column(LargeBinary, nullable=False)
  description = Column(String(255), nullable=True)
  credit = Column(String(50), nullable=True)

class QuizType(Base):
  __tablename__ = "quizType"

  id = Column(Integer, primary_key=True, index=True)
  description = Column(String(100), nullable=False)
  slug = Column(String(50), nullable=False)

class Quiz(Base):
  __tablename__ = "quiz"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(String(255), nullable=False)
  id_quiz_type = Column(Integer, ForeignKey("quizType.id"), nullable=False)

  quiz_type = relationship("QuizType")

class Question(Base):
  __tablename__ = "question"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(String(255), nullable=False)
  id_image = Column(Integer, ForeignKey("image.id"), nullable=True)
  id_quiz = Column(Integer, ForeignKey("quiz.id"), nullable=False)

  image = relationship("Image")
  quiz = relationship("Quiz")

class QuestionOption(Base):
  __tablename__ = "question_option"

  id = Column(Integer, primary_key=True, index=True)
  description = Column(String(100), nullable=True)
  points = Column(Integer, nullable=False)
  id_image = Column(Integer, ForeignKey("image.id"), nullable=True)
  id_question = Column(Integer, ForeignKey("question.id"), nullable=False)

  image = relationship("Image")
  question = relationship("Question")

class CareerOption(Base):
  __tablename__ = "career_option"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(100), nullable=False)
  description = Column(Text, nullable=False)
  id_image = Column(Integer, ForeignKey("image.id"), nullable=False)

  image = relationship("Image")

class Result(Base):
  __tablename__ = "result"

  id = Column(Integer, primary_key=True, index=True)
  id_quiz = Column(Integer, ForeignKey("quiz.id"), nullable=False)
  min_points = Column(Integer, nullable=False)
  max_points = Column(Integer, nullable=False)
  id_career_option = Column(Integer, ForeignKey("career_option.id"), nullable=False)

  quiz = relationship("Quiz")
  career_option = relationship("CareerOption")

class Course(Base):
  __tablename__ = "course"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(255), nullable=False)
  description = Column(String(255), nullable=False)
  link = Column(String(255), nullable=False)
  image = Column(LargeBinary, nullable=True)
  id_career_option = Column(Integer, ForeignKey("career_option.id"), nullable=False)

  career_option = relationship("CareerOption")
