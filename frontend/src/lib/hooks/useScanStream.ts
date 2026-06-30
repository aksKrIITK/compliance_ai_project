import { useState } from "react";

export function useScanStream() {
  const [step, setStep] = useState("idle");
  const start = () => setStep("research_complete");
  return { step, start };
}
