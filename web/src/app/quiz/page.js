"use client"

import { useEffect, useState } from "react";

import { api } from "@/services/api";

import styles from "./page.module.css";
import Card from "@/components/card";
import Button from "@/components/button";

export default function QuizChoice () {

  const [quizTypes, setQuizTypes] = useState([]);

  const handleGetQuizTypes = async () => {
    try {
      const { data } = await api.get(`quiz-types/`)
      setQuizTypes(data);
    } catch (err) {
      console.error(err)
    }
}

useEffect(() => {
  handleGetQuizTypes();
}, []);

  return (
    <main className={styles.main}>
      <div className={styles.topBlob}>
        <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
          <path fill="#ffeaf7" d="M28.5,-36.1C42.2,-29.3,62.3,-28,69.1,-19.5C76,-11,69.7,4.8,64.4,20.8C59,36.8,54.6,52.9,44,57C33.5,61,16.7,52.8,3.3,48.2C-10.1,43.6,-20.1,42.6,-26.1,37.1C-32.1,31.6,-34,21.6,-39.5,11.3C-44.9,1,-54,-9.8,-56.5,-23.5C-59.1,-37.2,-55.3,-54,-44.8,-61.9C-34.3,-69.7,-17.1,-68.7,-4.9,-62C7.4,-55.4,14.8,-43,28.5,-36.1Z" transform="translate(100 100)" />
        </svg>
      </div>
      <Card>
        <h1>Por onde eu começo?</h1>
        <p className={styles.description}>Escolha o tipo de teste que mais faça sentido com o seu momento na carreira.</p>

        <div className={styles.row}>
          {quizTypes.map(quizType => (
            <div className={styles.quizType}>
              <h2>{quizType.name}</h2>
              <p>{quizType.description}</p>
              <Button 
                path={`/quiz/${quizType.slug}`} 
                text={`Fazer o teste ${quizType.name?.toLowerCase()}`}
                style="secondary"
              />
            </div>
          ))}
        </div>
      </Card>

      <div className={styles.bottomBlob}>
      <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <path fill="#ffeaf7" d="M32.7,-43.3C45,-36,59.4,-30,60.7,-20.9C61.9,-11.9,50,0.2,45.2,14.6C40.4,29,42.8,45.6,36.5,51.5C30.1,57.3,15.1,52.5,1.2,50.9C-12.7,49.3,-25.5,51,-39.3,47.5C-53.1,44,-67.9,35.5,-73.9,22.7C-79.9,9.9,-77.1,-7.1,-68.4,-18.6C-59.7,-30.2,-45.2,-36.2,-32.8,-43.5C-20.5,-50.7,-10.2,-59.2,0,-59.1C10.2,-59.1,20.4,-50.6,32.7,-43.3Z" transform="translate(100 100)" />
      </svg>
      </div>
    </main>
  );
}
