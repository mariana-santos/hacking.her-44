import Link from "next/link";

export default function Home() {
  return (
    <main>
      <p>Escolha o tipo de enquete que deseja fazer</p>
      <p><Link href={'/quiz/simples'}>Simples</Link></p>
      <p><Link href={'/quiz/avancado'}>Avançado</Link></p>
    </main>
  );
}
