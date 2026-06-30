/** Country flag + regulation name + version */
export default function RegulationBadge({
  name,
  jurisdiction,
  version,
}: {
  name: string;
  jurisdiction: string;
  version: string;
}) {
  return (
    <div className="bg-slate-800 rounded-lg px-4 py-2 flex items-center gap-2">
      <span className="text-lg">{jurisdiction === "EU" ? "🇪🇺" : jurisdiction === "IN" ? "🇮🇳" : "🌐"}</span>
      <div>
        <p className="font-medium text-sm">{name}</p>
        <p className="text-xs text-slate-400">v{version}</p>
      </div>
    </div>
  );
}
