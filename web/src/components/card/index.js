import styles from "./card.module.css";

export default function Card ({ icon, children }) {
  return (
    <div className={styles.card}>
      {icon}
      {children}
    </div>
  );
}