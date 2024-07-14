"use client"
import { useEffect, useState } from "react";

import { api } from "@/services/api";

import styles from "./page.module.css";
import { useParams } from 'next/navigation'
import Link from "next/link";
import { FaCheckCircle } from "react-icons/fa";
import Button from "@/components/button";


export default function Quiz () {

  const { type } = useParams();

  const [quiz, setQuiz] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [points, setPoints] = useState(0);
  const [answeredQuestions, setAnsweredQuestions] = useState([]);
  const [selectedOption, setSelectedOption] = useState(null);
  const [result, setResult] = useState(null);

  const handleGetQuiz = async () => {
    try {
      const { data } = await api.get(`quizzes/by-type/${type}`)
      setQuiz(data[0]);
      setCurrentQuestion(data[0]?.questions[0]);
      setCurrentQuestionIndex(0);
    } catch (err) {
      console.error(err)
    }
  }

  useEffect(() => {
    handleGetQuiz();
  }, []);

  if (!quiz || !currentQuestion) return;

  const currentQuestionIndicatorLabel = `Questão ${currentQuestionIndex + 1} de ${quiz.questions.length}`;
  const isLastQuestion = currentQuestionIndex === quiz.questions.length - 1;

  const nextQuestion = () => {
    setCurrentQuestion(quiz.questions[currentQuestionIndex + 1]);
    setCurrentQuestionIndex(currentQuestionIndex + 1);
    setSelectedOption(null);
  }

  const sumPoints = (option) => {
    setAnsweredQuestions((prevAnsweredQuestions) => [...prevAnsweredQuestions, currentQuestion]);
    setPoints(prevPoints => prevPoints + option.points);
  }

  const finish = () => {
    const result = quiz.results.find(result => 
      points >= result.min_points && points <= result.max_points
    );

    setResult(result);
  }

  const handleConfirmAnswer = () => {
    if (!selectedOption) return;

    // Se ainda não foi contado os pontos dessa questão, então ele soma os pontos
    if (answeredQuestions.indexOf(currentQuestion) === -1)
      sumPoints(selectedOption);

    if (isLastQuestion) 
      finish();

    // Se ainda tem pergunta restante, vai pra próxima
    if (currentQuestionIndex < quiz.questions.length - 1)
      nextQuestion();
  }

  const isAnsweredQuestion = question => (
    answeredQuestions.indexOf(question) !== -1
  );


  if (result) return (
    <main className={styles.main}>
      <div className={styles.result}>
        <div className={styles.breadcrumb}>
          <Link href={"/quiz"}>Enquetes</Link> {" > "}
          <span>{quiz.title}</span>
        </div>

        <div className={styles.result}>
          <h1>{result.career_option.title}</h1>
          <p>{result.career_option.description}</p>

          <Button 
            path="/quiz" 
            text="Ver enquetes"
            style="secondary" 
          />
        </div>
      </div>

      <section className={styles.courses}>
        <h3> Cursos que combinam com você </h3>
          {result.career_option.courses.map(course => (
            <div className={styles.course}>
              <h4>{course.title}</h4>
              <p>{course.description}</p>
              <a 
                href={course.link} 
                target="_blank"
                className={styles.confirmAnswer}
              >Saiba mais</a>
            </div>
          ))}
      </section>
    </main>
  );

  return (
    <main className={styles.main}>
      {quiz && (
        <div className={styles.quiz}>

          <div className={styles.breadcrumb}>
            <Link href={"/quiz"}>Enquetes</Link> {" > "}
            <span>{quiz.title}</span>
          </div>

          <span className={styles.questionsIndicator}>{currentQuestionIndicatorLabel}</span>

          {currentQuestion && (
            <div className={styles.question}>
              <h1>{currentQuestion.title}</h1>
              <p>{currentQuestion.description}</p>
              <div className={styles.questions}>  
                {currentQuestion.options.map((option, index) => (
                  <button 
                    onClick={() => setSelectedOption(option)}
                    className={styles[selectedOption === option ? "selectedOption" : "option"]}
                  >
                    <span>{index + 1}) </span>
                    {option.description}
                  </button>
                ))}
              </div>

              <button 
                  className={styles.confirmAnswer} 
                  onClick={handleConfirmAnswer}
                >
                  {isLastQuestion ? 'Finalizar' : 'Confirmar escolha'}
              </button>
            </div>
          )}
        </div>
      )}

      <section className={styles.questionsList}>
        <h3> Lista de perguntas </h3>
        <div className={styles.buttons}>
          {quiz.questions.map(question => (
            <button 
              className={
                styles[isAnsweredQuestion(question) ? 'done' : 'todo'] }
            >
                <span>{question.title}</span>
                {isAnsweredQuestion(question) && <FaCheckCircle />}
            </button>
          ))}
        </div>
      </section>
    </main>
  );
}
