import UploadIncident from "../components/UploadIncident";
import IncidentSummary from "../components/IncidentSummary";
import Timeline from "../components/Timeline";
import KnowledgeGraph from "../components/KnowledgeGraph";
import AIAssistant from "../components/AIAssistant";

import { useState } from "react";

export default function Dashboard() {
  const [incident, setIncident] = useState(null);

  return (
    <div
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          fontSize: "48px",
          marginBottom: "10px",
        }}
      >
        🚀 TwinMind Incident Intelligence
      </h1>

      <UploadIncident setIncident={setIncident} />

      {incident && (
        <>
          <IncidentSummary incident={incident} />
          <Timeline incident={incident} />
          <KnowledgeGraph incident={incident} />
          <AIAssistant incident={incident} />
        </>
      )}
    </div>
  );
}