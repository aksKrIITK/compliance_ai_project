/** Real-time agent step progress via SSE */
export default function ScanProgress({ step }: { step: string }) {
  return (
    <div className="bg-slate-900 rounded-xl p-6">
      <p className="text-slate-400 text-sm mb-2">Scan Progress</p>
      <p className="font-mono text-emerald-400">{step}</p>
    </div>
  );
}
