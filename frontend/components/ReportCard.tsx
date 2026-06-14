import ReactMarkdown from "react-markdown";
import PDFButton from "./PDFButton";

type Props = {
  report: string;
};

export default function ReportCard({ report }: Props) {
  if (!report) return null;

  return (
    <div className="mt-8 bg-zinc-800 p-8 rounded-2xl border border-zinc-700 shadow-xl">
      <h2 className="text-3xl font-bold mb-6 text-blue-400">
        AI Startup Report
      </h2>

      <article className="prose prose-invert max-w-none">
        <ReactMarkdown>{report}</ReactMarkdown>
      </article>

      <PDFButton report={report} />

    </div>
  );
}