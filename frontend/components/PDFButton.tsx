type Props = {
  report: string;
};

export default function PDFButton({ report }: Props) {
  if (!report) return null;

  const downloadPDF = () => {
    window.open("http://127.0.0.1:8000/download-pdf", "_blank");
  };

  return (
    <button
      onClick={downloadPDF}
      className="mt-4 bg-green-600 hover:bg-green-700 px-5 py-3 rounded-lg font-semibold"
    >
      Download PDF
    </button>
  );
}