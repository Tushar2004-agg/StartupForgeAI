type Props = {
  startupName: string;
  industry: string;
  budget: string;
  location: string;
};

export default function Dashboard({
  startupName,
  industry,
  budget,
  location,
}: Props) {
  if (!startupName) return null;

  return (
    <div className="grid grid-cols-2 gap-4 mb-8">
      <div className="bg-zinc-800 p-4 rounded-xl border border-zinc-700">
        <h3 className="text-gray-400 text-sm">Startup</h3>
        <p className="text-xl font-bold">{startupName}</p>
      </div>

      <div className="bg-zinc-800 p-4 rounded-xl border border-zinc-700">
        <h3 className="text-gray-400 text-sm">Industry</h3>
        <p className="text-xl font-bold">{industry}</p>
      </div>

      <div className="bg-zinc-800 p-4 rounded-xl border border-zinc-700">
        <h3 className="text-gray-400 text-sm">Budget</h3>
        <p className="text-xl font-bold">₹ {budget}</p>
      </div>

      <div className="bg-zinc-800 p-4 rounded-xl border border-zinc-700">
        <h3 className="text-gray-400 text-sm">Location</h3>
        <p className="text-xl font-bold">{location}</p>
      </div>
    </div>
  );
}