from pydantic import BaseModel
from typing import Optional, List

class ImageBase(BaseModel):
  description: Optional[str] = None
  credit: Optional[str] = None

class ImageCreate(ImageBase):
  content: bytes

class Image(ImageBase):
  id: int
  content: bytes

  class Config:
    orm_mode = True

class QuizTypeBase(BaseModel):
  description: str
  slug: str

class QuizTypeCreate(QuizTypeBase):
  pass

class QuizType(QuizTypeBase):
  id: int

  class Config:
    orm_mode = True

class QuizBase(BaseModel):
  title: str
  description: str
  id_quiz_type: int

class QuizCreate(QuizBase):
  pass

class Quiz(QuizBase):
  id: int
  quiz_type: QuizType

  class Config:
    orm_mode = True

class QuestionBase(BaseModel):
  title: str
  description: str
  id_image: Optional[int] = None
  id_quiz: int

class QuestionCreate(QuestionBase):
  pass

class Question(QuestionBase):
  id: int
  image: Optional[Image] = None
  quiz: Quiz

  class Config:
    orm_mode = True

class QuestionOptionBase(BaseModel):
  description: Optional[str] = None
  points: int
  id_image: Optional[int] = None
  id_question: int

class QuestionOptionCreate(QuestionOptionBase):
  pass

class QuestionOption(QuestionOptionBase):
  id: int
  image: Optional[Image] = None
  question: Question

  class Config:
    orm_mode = True

class CareerOptionBase(BaseModel):
  title: str
  description: str
  id_image: int

class CareerOptionCreate(CareerOptionBase):
  pass

class CareerOption(CareerOptionBase):
  id: int
  image: Image

  class Config:
    orm_mode = True

class ResultBase(BaseModel):
  id_quiz: int
  min_points: int
  max_points: int
  id_career_option: int

class ResultCreate(ResultBase):
  pass

class Result(ResultBase):
  id: int
  quiz: Quiz
  career_option: CareerOption

  class Config:
    orm_mode = True

class CourseBase(BaseModel):
  title: str
  description: str
  link: str
  image: Optional[bytes] = None
  id_career_option: int

class CourseCreate(CourseBase):
  pass

class Course(CourseBase):
  id: int
  career_option: CareerOption

  class Config:
    orm_mode = True
