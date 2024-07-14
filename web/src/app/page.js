import Button from "@/components/button";
import Card from "@/components/card";

import styles from "./page.module.css";

import mainPicture from "@/assets/main-picture.png";

export default function Home() {
  return (
    <div className={styles.container}>
      <main 
        className={styles.main} 
      >
        <div className={styles.description}>
          <h1>Ei, <span>mulher!</span></h1>

          <p>Já se viu trabalhando de casa, com flexibilidade de horários e ganhando um salário justo?</p>
          <p>Na área de tecnologia, esse pode ser seu futuro!</p>
          <p>Quer saber qual por onde começar e qual área da tecnologia combina mais com você? </p>

          <Button path={"/quiz"} text="Vem com a gente!" />
        </div>

        <div className={styles.mainPicture}>
          <img src={mainPicture.src} className={styles.imageFocused} />
        </div>
      </main>

      <section className={styles.cause} id="cause">
        <div className={styles.cause__content}>
          <h2>Nossa causa</h2>
          <p>As mulheres são maioria da população do Brasil, mas quando olhamos para o mercado de tecnologia, são apenas <strong>7%!</strong> </p>
          <p>Esse é um mercado promissor e que permite boas condições de trabalho e remuneração. </p>
          <p>Nosso propósito é que as mulheres passem ocupar pelo menos metade das mais de <strong>um milhão de vagas disponíveis</strong> no mercado brasileiro nesta área.</p>
        </div>

        <div className={styles.cards}>
          <Card>
            <h3>Realidade</h3>
            <p>As mulheres, embora sejam maioria e com maior nível educacional, ocupam apenas <strong>7% das vagas de tecnologia no Brasil</strong>. </p>
            <p>Isso acontece principalmente pela falta de incentivo para meninas e mulheres a seguirem carreira nessas áreas.</p>
          </Card>
          <Card>
            <h3>Possibilidades</h3>
            <p>Com conhecimento e motivação para tabalhar em tecnologia, as mulheres podem <strong>alavancar suas carreiras</strong> devido às boas condições de trabalho e remuneração da área. </p> 
            <p>A flexibilidade de local e horários também são pontos positivos considerando que grande parte das mulheres costumam assumir mais <strong>responsabilidades</strong> com a família.</p>
          </Card>
          <Card>
            <h3>Objetivos</h3>
            <p>Queremos que as meninas e mulheres se desenvolvam para atingirem cada vez mais espaço no mercado de tecnologia!</p> 
            <p>Para isso, vamos conectá-las com suas aptidões e em seguida com as <strong>ferramentas necessárias</strong> para atingirem seus objetivos.</p>
          </Card>
        </div>
      </section>
    </div>
  );
}
