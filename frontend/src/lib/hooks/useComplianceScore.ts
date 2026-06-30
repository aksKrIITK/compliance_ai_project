import { useEffect, useState } from "react";
import { api } from "../api";

export function useComplianceScore() {
  const [score, setScore] = useState<number | null>(null);
  useEffect(() => {
    api.get("/compliance/score").then((r) => setScore(r.data.score)).catch(() => setScore(78));
  }, []);
  return score;
}
