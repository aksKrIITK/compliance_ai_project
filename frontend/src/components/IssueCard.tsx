/** Severity badge + regulation citation + remediation steps */
export default function IssueCard({
  title,
  severity,
  regulation,
  remediation,
}: {
  title: string;
  severity: string;
  regulation: string;
  remediation: string;
}) {
  const colors: Record<string, string> = { high: "bg-red-500", medium: "bg-yellow-500", low: "bg-green-500" };
  return (
    <div className="bg-slate-900 rounded-lg p-4 mt-4">
      <div className="flex items-center gap-2 mb-2">
        <span className={`${colors[severity] || "bg-slate-500"} text-xs px-2 py-0.5 rounded uppercase`}>{severity}</span>
        <span className="text-slate-400 text-sm">{regulation}</span>
      </div>
      <h3 className="font-semibold">{title}</h3>
      <p className="text-slate-400 text-sm mt-1">{remediation}</p>
    </div>
  );
}
