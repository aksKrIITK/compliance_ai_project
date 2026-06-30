import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import DocumentUpload from "./pages/DocumentUpload";
import AgentChat from "./pages/AgentChat";
import Regulations from "./pages/Regulations";
import Settings from "./pages/Settings";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/upload" element={<DocumentUpload />} />
        <Route path="/chat" element={<AgentChat />} />
        <Route path="/regulations" element={<Regulations />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
