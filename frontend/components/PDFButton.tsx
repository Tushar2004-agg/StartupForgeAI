type Props = {
  report: string;
};

export default function PDFButton({ report }: Props) {
  if (!report) return null;

  const downloadPDF = async () => {
    const response = await fetch(
      "https://startupforgeai.onrender.com/download-pdf",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          report,
        }),
      }
    );

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "startup_report.pdf";

    document.body.appendChild(a);
    a.click();
    a.remove();
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