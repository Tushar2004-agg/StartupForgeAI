"use client";

import { useState } from "react";

export default function Home() {
  const [startupName, setStartupName] = useState("");
  const [industry, setIndustry] = useState("");
  const [budget, setBudget] = useState("");
  const [location, setLocation] = useState("");

  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const generateReport = async () => {
    try {
      setLoading(true);
      setReport("");

      const response = await fetch(
        "http://127.0.0.1:8000/startup",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            startup_name: startupName,
            industry,
            budget,
            location,
          }),
        }
      );

      const data = await response.json();

      setReport(data.final_report);
    } catch (error) {
      console.error(error);
      setReport("Error generating report.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-black text-white flex justify-center items-center p-10">
      <div className="w-full max-w-4xl bg-zinc-900 p-8 rounded-2xl shadow-lg">

        <h1 className="text-5xl font-bold text-center mb-4">
          StartupForge AI 🚀
        </h1>

        <p className="text-center text-gray-400 mb-8">
          Generate AI-powered startup plans using multiple intelligent agents
        </p>

        <div className="space-y-4">

          <input
            type="text"
            placeholder="Startup Name"
            value={startupName}
            onChange={(e) => setStartupName(e.target.value)}
            className="w-full p-3 rounded-lg bg-zinc-800 border border-zinc-700"
          />

          <input
            type="text"
            placeholder="Industry"
            value={industry}
            onChange={(e) => setIndustry(e.target.value)}
            className="w-full p-3 rounded-lg bg-zinc-800 border border-zinc-700"
          />

          <input
            type="number"
            placeholder="Budget"
            value={budget}
            onChange={(e) => setBudget(e.target.value)}
            className="w-full p-3 rounded-lg bg-zinc-800 border border-zinc-700"
          />

          <input
            type="text"
            placeholder="Location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            className="w-full p-3 rounded-lg bg-zinc-800 border border-zinc-700"
          />

          <button
            onClick={generateReport}
            className="w-full bg-blue-600 hover:bg-blue-700 p-3 rounded-lg font-semibold"
          >
            {loading ? "Generating..." : "Generate Startup Plan"}
          </button>

        </div>

        {report && (
          <div className="mt-8 bg-zinc-800 p-6 rounded-lg">
            <h2 className="text-2xl font-bold mb-4">
              AI Startup Report
            </h2>

            <pre className="whitespace-pre-wrap text-sm">
              {report}
            </pre>
          </div>
        )}

      </div>
    </main>
  );
}