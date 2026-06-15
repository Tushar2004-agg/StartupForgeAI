"use client";

import { useState } from "react";

type Props = {
  report: string;
};

export default function StartupChat({ report }: Props) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  if (!report) return null;

  const askAI = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "https://startupforgeai.onrender.com/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            report,
            question,
          }),
        }
      );

      const data = await response.json();

      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Error getting answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mt-8 bg-zinc-800 p-6 rounded-2xl border border-zinc-700">
      <h2 className="text-2xl font-bold mb-4 text-green-400">
        Chat With Your Startup 🚀
      </h2>

      <input
        type="text"
        placeholder="Ask anything about your startup..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full p-3 rounded-lg bg-zinc-900 border border-zinc-700"
      />

      <button
        onClick={askAI}
        className="mt-4 bg-green-600 hover:bg-green-700 px-5 py-3 rounded-lg font-semibold"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      {answer && (
        <div className="mt-6 bg-zinc-900 p-4 rounded-lg">
          {answer}
        </div>
      )}
    </div>
  );
}