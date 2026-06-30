/** Drag-drop + progress + extraction preview */
export default function DocumentUpload() {
  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Upload Documents</h1>
      <div className="border-2 border-dashed border-slate-600 rounded-lg p-12 text-center">
        <p>Drag & drop PDFs here</p>
        <p className="text-slate-400 text-sm mt-2">PDF → text → chunks → pgvector</p>
      </div>
    </div>
  );
}
