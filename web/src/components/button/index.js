import Link from "next/link";
import styles from "./button.module.css";

export default function Button ({ path, text, style = 'primary' }) {
  return (
    <Link 
      href={path}
      className={styles[`${style}Button`]}
    >
      {text}
    </Link>
  );
}