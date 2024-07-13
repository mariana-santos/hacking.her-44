from sqlalchemy.orm import Session
import models
import schemas

# Image CRUD operations
def get_image(db: Session, image_id: int):
  return db.query(models.Image).filter(models.Image.id == image_id).first()

def get_images(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Image).offset(skip).limit(limit).all()

def create_image(db: Session, image: schemas.ImageCreate):
  db_image = models.Image(**image.dict())
  db.add(db_image)
  db.commit()
  db.refresh(db_image)
  return db_image


# QuizType CRUD operations
def get_quiz_type(db: Session, quiz_type_id: int):
  return db.query(models.QuizType).filter(models.QuizType.id == quiz_type_id).first()

def get_quiz_types(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.QuizType).offset(skip).limit(limit).all()

def create_quiz_type(db: Session, quiz_type: schemas.QuizTypeCreate):
  db_quiz_type = models.QuizType(**quiz_type.dict())
  db.add(db_quiz_type)
  db.commit()
  db.refresh(db_quiz_type)
  return db_quiz_type


# Quiz CRUD operations
def get_quiz(db: Session, quiz_id: int):
  return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizzes(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Quiz).offset(skip).limit(limit).all()

def create_quiz(db: Session, quiz: schemas.QuizCreate):
  db_quiz = models.Quiz(**quiz.dict())
  db.add(db_quiz)
  db.commit()
  db.refresh(db_quiz)
  return db_quiz


# Question CRUD operations
def get_question(db: Session, question_id: int):
  return db.query(models.Question).filter(models.Question.id == question_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Question).offset(skip).limit(limit).all()

def create_question(db: Session, question: schemas.QuestionCreate):
  db_question = models.Question(**question.dict())
  db.add(db_question)
  db.commit()
  db.refresh(db_question)
  return db_question


# QuestionOption CRUD operations
def get_question_option(db: Session, question_option_id: int):
  return db.query(models.QuestionOption).filter(models.QuestionOption.id == question_option_id).first()

def get_question_options(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.QuestionOption).offset(skip).limit(limit).all()

def create_question_option(db: Session, question_option: schemas.QuestionOptionCreate):
  db_question_option = models.QuestionOption(**question_option.dict())
  db.add(db_question_option)
  db.commit()
  db.refresh(db_question_option)
  return db_question_option


# CareerOption CRUD operations
def get_career_option(db: Session, career_option_id: int):
  return db.query(models.CareerOption).filter(models.CareerOption.id == career_option_id).first()

def get_career_options(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.CareerOption).offset(skip).limit(limit).all()

def create_career_option(db: Session, career_option: schemas.CareerOptionCreate):
  db_career_option = models.CareerOption(**career_option.dict())
  db.add(db_career_option)
  db.commit()
  db.refresh(db_career_option)
  return db_career_option


# Result CRUD operations
def get_result(db: Session, result_id: int):
  return db.query(models.Result).filter(models.Result.id == result_id).first()

def get_results(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Result).offset(skip).limit(limit).all()

def create_result(db: Session, result: schemas.ResultCreate):
  db_result = models.Result(**result.dict())
  db.add(db_result)
  db.commit()
  db.refresh(db_result)
  return db_result


# Course CRUD operations
def get_course(db: Session, course_id: int):
  return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):
  db_course = models.Course(**course.dict())
  db.add(db_course)
  db.commit()
  db.refresh(db_course)
  return db_course
