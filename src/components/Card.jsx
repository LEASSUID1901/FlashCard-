import { useState } from "react";

function Card({ question, answer }) {
  const [showAnswer, setShowAnswer] = useState(false);

  return (
    <div className="card" onClick={() => setShowAnswer(!showAnswer)}>
      <p>{showAnswer ? answer : question}</p>
      <span className="hint">{showAnswer ? "Cliquer pour cacher" : "Cliquer pour voir la réponse"}</span>
    </div>
  );
}

export default Card;
