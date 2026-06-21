import { useState } from "react";
import Card from "./components/Card";
import ProgressBar from "./components/ProgressBar";
import "./App.css";

function App() {
  const [cards, setCards] = useState([]);
  const [index, setIndex] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [started, setStarted] = useState(false);
  const [category, setCategory] = useState("histoire");
  const [difficulty, setDifficulty] = useState("easy");

  const fetchCards = async () => {
    setLoading(true);
    setError(null);
    setStarted(false);
    try {
      const res = await fetch(
        `http://localhost:8000/questions?category=${category}&difficulty=${difficulty}`
      );
      const data = await res.json();
      if (!data || data.length === 0) {
        setError("Aucune question trouvée. Change la catégorie ou la difficulté.");
        setLoading(false);
        return;
      }
      const formatted = data.map((item, i) => ({
        id: i,
        question: item.question,
        answer: item.answer,
      }));
      setCards(formatted);
      setIndex(0);
      setStarted(true);
    } catch (err) {
      setError("Erreur réseau. Vérifie ta connexion.");
    } finally {
      setLoading(false);
    }
  };

  const prev = () => setIndex(i => Math.max(0, i - 1));
  const next = () => setIndex(i => Math.min(cards.length - 1, i + 1));

  if (loading) {
    return (
      <div className="app">
        <h1>Flash <span>Cards</span></h1>
        <div className="setup-card">
          <p className="loading">Chargement des questions...</p>
        </div>
      </div>
    );
  }

  if (!started) {
    return (
      <div className="app">
        <h1>Flash <span>Cards</span></h1>
        <div className="setup-card">
          <h2>Configure ta session</h2>
          <div className="field">
            <label>Catégorie</label>
            <select value={category} onChange={e => setCategory(e.target.value)}>
              <option value="histoire">Histoire</option>
              <option value="sciences">Sciences</option>
              <option value="géographie">Géographie</option>
              <option value="sport">Sport</option>
              <option value="cinéma">Cinéma</option>
            </select>
          </div>
          <div className="field">
            <label>Difficulté</label>
            <select value={difficulty} onChange={e => setDifficulty(e.target.value)}>
              <option value="easy">Facile</option>
              <option value="medium">Moyen</option>
              <option value="hard">Difficile</option>
            </select>
          </div>
          <button className="start-btn" onClick={fetchCards}>
            Lancer la session →
          </button>
          {error && <p className="error">{error}</p>}
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      <h1>Flash <span>Cards</span></h1>
      <ProgressBar current={index + 1} total={cards.length} />
      <Card
        question={cards[index].question}
        answer={cards[index].answer}
      />
      <div className="nav">
        <button onClick={prev} disabled={index === 0}>‹ Précédent</button>
        <button onClick={next} disabled={index === cards.length - 1}>Suivant ›</button>
      </div>
      <button className="reset-btn" onClick={() => setStarted(false)}>
        ↺ Nouvelle session
      </button>
    </div>
  );
}

export default App;