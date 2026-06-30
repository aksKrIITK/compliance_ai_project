/** Animated gauge: 0–100 compliance score */
export default function RiskScoreGauge({ score }: { score: number }) {
  return (
    <div className="bg-slate-900 rounded-xl p-6 text-center">
      <p className="text-slate-400 text-sm mb-2">Compliance Score</p>
      <p className="text-5xl font-bold text-emerald-400">{score}</p>
      <div className="mt-3 h-2 bg-slate-700 rounded-full">
        <div className="h-2 bg-emerald-500 rounded-full" style={{ width: `${score}%` }} />
      </div>
    </div>
  );
}
