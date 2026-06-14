type Props = {
  startupName: string;
  setStartupName: (value: string) => void;
  industry: string;
  setIndustry: (value: string) => void;
  budget: string;
  setBudget: (value: string) => void;
  location: string;
  setLocation: (value: string) => void;
  generateReport: () => void;
  loading: boolean;
};

export default function StartupForm({
  startupName,
  setStartupName,
  industry,
  setIndustry,
  budget,
  setBudget,
  location,
  setLocation,
  generateReport,
  loading,
}: Props) {
  return (
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
  );
}