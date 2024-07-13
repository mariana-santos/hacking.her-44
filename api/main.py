from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar todas as imagens
@app.get("/images/", response_model = List[schemas.Image])
def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    images = crud.get_images(db, skip = skip, limit = limit)
    return images

# Endpoint para buscar uma imagem pelo ID
@app.get("/images/{image_id}/", response_model = schemas.Image)
def read_image(image_id: int, db: Session = Depends(get_db)):
    db_image = crud.get_image(db, image_id = image_id)
    if db_image is None:
        raise HTTPException(status_code = 404, detail = "Image not found")
    return db_image


# Endpoint para criar um novo tipo de quiz
@app.post("/quiz-types/", response_model = schemas.QuizType)
def create_quiz_type(quiz_type: schemas.QuizTypeCreate, db: Session = Depends(get_db)):
    return crud.create_quiz_type(db = db, quiz_type = quiz_type)

# Endpoint para listar todos os tipos de quiz
@app.get("/quiz-types/", response_model = List[schemas.QuizType])
def read_quiz_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quiz_types = crud.get_quiz_types(db, skip = skip, limit = limit)
    return quiz_types

# Endpoint para buscar um tipo de quiz pelo ID
@app.get("/quiz-types/{quiz_type_id}/", response_model = schemas.QuizType)
def read_quiz_type(quiz_type_id: int, db: Session = Depends(get_db)):
    db_quiz_type = crud.get_quiz_type(db, quiz_type_id = quiz_type_id)
    if db_quiz_type is None:
        raise HTTPException(status_code = 404, detail = "Quiz type not found")
    return db_quiz_type

# Endpoint para criar um novo quiz
@app.post("/quizzes/", response_model = schemas.Quiz)
def create_quiz(quiz: schemas.QuizCreate, db: Session = Depends(get_db)):
    return crud.create_quiz(db = db, quiz = quiz)

# Endpoint para listar todos os quizzes
@app.get("/quizzes/", response_model = List[schemas.Quiz])
def read_quizzes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    quizzes = crud.get_quizzes(db, skip = skip, limit = limit)
    return quizzes


# Endpoint para buscar um quiz pelo ID
@app.get("/quizzes/{quiz_id}/", response_model = schemas.Quiz)
def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
    db_quiz = crud.get_quiz(db, quiz_id = quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code = 404, detail = "Quiz not found")
    return db_quiz


# Endpoint para criar uma nova questão
@app.post("/questions/", response_model = schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db = db, question = question)


# Endpoint para listar todas as questões
@app.get("/questions/", response_model = List[schemas.Question])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip = skip, limit = limit)
    return questions


# Endpoint para buscar uma questão pelo ID
@app.get("/questions/{question_id}/", response_model = schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id = question_id)
    if db_question is None:
        raise HTTPException(status_code = 404, detail = "Question not found")
    return db_question


# Endpoint para criar uma nova opção de questão
@app.post("/question-options/", response_model = schemas.QuestionOption)
def create_question_option(option: schemas.QuestionOptionCreate, db: Session = Depends(get_db)):
    return crud.create_question_option(db = db, question_option = option)


# Endpoint para listar todas as opções de questão
@app.get("/question-options/", response_model = List[schemas.QuestionOption])
def read_question_options(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    options = crud.get_question_options(db, skip = skip, limit = limit)
    return options


# Endpoint para buscar uma opção de questão pelo ID
@app.get("/question-options/{option_id}/", response_model = schemas.QuestionOption)
def read_question_option(option_id: int, db: Session = Depends(get_db)):
    db_option = crud.get_question_option(db, question_option_id = option_id)
    if db_option is None:
        raise HTTPException(status_code = 404, detail = "Question option not found")
    return db_option


# Endpoint para criar uma nova opção de carreira
@app.post("/career-options/", response_model = schemas.CareerOption)
def create_career_option(option: schemas.CareerOptionCreate, db: Session = Depends(get_db)):
    return crud.create_career_option(db = db, career_option = option)


# Endpoint para listar todas as opções de carreira
@app.get("/career-options/", response_model = List[schemas.CareerOption])
def read_career_options(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    options = crud.get_career_options(db, skip = skip, limit = limit)
    return options


# Endpoint para buscar uma opção de carreira pelo ID
@app.get("/career-options/{option_id}/", response_model = schemas.CareerOption)
def read_career_option(option_id: int, db: Session = Depends(get_db)):
    db_option = crud.get_career_option(db, career_option_id = option_id)
    if db_option is None:
        raise HTTPException(status_code = 404, detail = "Career option not found")
    return db_option


# Endpoint para criar um novo resultado
@app.post("/results/", response_model = schemas.Result)
def create_result(result: schemas.ResultCreate, db: Session = Depends(get_db)):
    return crud.create_result(db = db, result = result)


# Endpoint para listar todos os resultados
@app.get("/results/", response_model = List[schemas.Result])
def read_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_results(db, skip = skip, limit = limit)
    return results


# Endpoint para buscar um resultado pelo ID
@app.get("/results/{result_id}/", response_model = schemas.Result)
def read_result(result_id: int, db: Session = Depends(get_db)):
    db_result = crud.get_result(db, result_id = result_id)
    if db_result is None:
        raise HTTPException(status_code = 404, detail = "Result not found")
    return db_result


# Endpoint para criar um novo curso
@app.post("/courses/", response_model = schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db = db, course = course)


# Endpoint para listar todos os cursos
@app.get("/courses/", response_model = List[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip = skip, limit = limit)
    return courses


# Endpoint para buscar um curso pelo ID
@app.get("/courses/{course_id}/", response_model = schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id = course_id)
    if db_course is None:
        raise HTTPException(status_code = 404, detail = "Course not found")
    return db_course
