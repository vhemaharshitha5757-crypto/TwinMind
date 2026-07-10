import { useState } from "react";

export default function AIAssistant({ incident }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {
    if (!question.trim()) return;

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question,
          incident,
        }),
      });

      const data = await response.json();
      setAnswer(data.answer);
    } catch (err) {
      console.error(err);
      setAnswer("Failed to contact AI.");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        background: "#1e293b",
        padding: 25,
        borderRadius: 12,
      }}
    >
      <h2>AI Assistant</h2>

      <input
        type="text"
        value={question}
        placeholder="Ask about this incident..."
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") askAI();
        }}
        style={{
          width: "100%",
          padding: 12,
          borderRadius: 8,
        }}
      />

      <button
        onClick={askAI}
        style={{
          marginTop: 15,
          padding: "10px 20px",
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
        }}
      >
        Ask AI
      </button>

      {loading && (
        <p style={{ marginTop: 20 }}>Thinking...</p>
      )}

      {answer && (
        <div
          style={{
            marginTop: 20,
            padding: 15,
            background: "#334155",
            borderRadius: 8,
          }}
        >
          <strong>AI Answer</strong>

          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}