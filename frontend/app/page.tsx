"use client";

import { useState } from "react";
import StartupForm from "../components/StartupForm";
import ReportCard from "../components/ReportCard";
import Dashboard from "../components/Dashboard";
import LoadingSpinner from "../components/LoadingSpinner";
import StartupChat from "../components/StartupChat";

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

      const response = await fetch("https://startupforgeai.onrender.com/startup", {
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
      });

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

        <StartupForm
          startupName={startupName}
          setStartupName={setStartupName}
          industry={industry}
          setIndustry={setIndustry}
          budget={budget}
          setBudget={setBudget}
          location={location}
          setLocation={setLocation}
          generateReport={generateReport}
          loading={loading}
        />

        <Dashboard
          startupName={startupName}
          industry={industry}
          budget={budget}
          location={location}
        />

        {loading && <LoadingSpinner />}

        <ReportCard report={report} />
        <StartupChat report={report} />
      </div>
    </main>
  );
}