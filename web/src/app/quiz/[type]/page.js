'use client'

import { useParams } from 'next/navigation'

export default function QuizByType() {

  const { type } = useParams();

  return (
    <main>
      Enquete {type}
    </main>
  );
}
