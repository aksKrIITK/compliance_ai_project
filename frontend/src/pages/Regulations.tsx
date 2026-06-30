import RegulationBadge from "../components/RegulationBadge";

/** Browse/search regulation library by country */
export default function Regulations() {
  const regs = [
    { name: "GDPR", jurisdiction: "EU", version: "2016/679" },
    { name: "DPDP Act 2023", jurisdiction: "IN", version: "2023" },
  ];
  return (
    <div className="p-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Regulation Library</h1>
      <div className="flex flex-wrap gap-3">
        {regs.map((r) => (
          <RegulationBadge key={r.name} {...r} />
        ))}
      </div>
    </div>
  );
}
