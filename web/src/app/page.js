import styles from "./page.module.css";
import Link from "next/link";

export default function Home() {
  return (
    <main className={styles.main}>
      Home
      <Link href={"/quiz"}>Escolher a enquete</Link>
    </main>
  );
}
