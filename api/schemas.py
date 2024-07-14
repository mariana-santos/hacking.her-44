from pydantic import BaseModel
from typing import List, Optional

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
    name: str
    description: str
    slug: str

class QuizTypeCreate(QuizTypeBase):
    pass

class QuizType(QuizTypeBase):
    id: int

    class Config:
        orm_mode = True

class QuestionOptionBase(BaseModel):
    description: Optional[str] = None
    points: int

class QuestionOptionCreate(QuestionOptionBase):
    id_image: Optional[int] = None
    id_question: int

class QuestionOption(QuestionOptionBase):
    id: int
    id_image: Optional[int]
    id_question: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    title: str
    description: Optional[str] = None

class QuestionCreate(QuestionBase):
    id_image: Optional[int] = None
    id_quiz: int

class Question(QuestionBase):
    id: int
    id_image: Optional[int]
    id_quiz: int
    options: List[QuestionOption] = []

    class Config:
        orm_mode = True

class CareerOptionBase(BaseModel):
    title: str
    description: str

class CareerOptionCreate(CareerOptionBase):
    id_image: Optional[int]

class CareerOption(CareerOptionBase):
    id: int
    id_image: Optional[int]
    courses: List['Course'] = []

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str
    link: str

class CourseCreate(CourseBase):
    id_career_option: int

class Course(CourseBase):
    id: int
    id_career_option: int

    class Config:
        orm_mode = True

class ResultBase(BaseModel):
    min_points: int
    max_points: int

class ResultCreate(ResultBase):
    id_quiz: int
    id_career_option: int

class Result(ResultBase):
    id: int
    id_quiz: int
    id_career_option: int
    career_option: CareerOption

    class Config:
        orm_mode = True

class QuizBase(BaseModel):
    title: str
    description: str

class QuizCreate(QuizBase):
    id_quiz_type: int

class Quiz(QuizBase):
    id: int
    id_quiz_type: int
    questions: List[Question] = []
    results: List[Result] = []

    class Config:
        orm_mode = True
