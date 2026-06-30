import RiskScoreGauge from "../components/RiskScoreGauge";
import IssueCard from "../components/IssueCard";
import ScanProgress from "../components/ScanProgress";

/** Risk gauge + issue list + regulation coverage — SSE live */
export default function Dashboard() {
  return (
    <div className="p-8 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Compliance Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <RiskScoreGauge score={78} />
        <ScanProgress step="analysis_complete" />
      </div>
      <IssueCard
        title="Missing data retention policy"
        severity="high"
        regulation="GDPR Art. 5"
        remediation="Define retention periods per data category"
      />
    </div>
  );
}
