export default function IncidentSummary({ incident }) {
  if (!incident) return null;

  return (
    <div
      style={{
        background: "#1e293b",
        padding: 25,
        borderRadius: 12,
        marginBottom: 30,
      }}
    >
      <h2>Incident Summary</h2>

      <table style={{ width: "100%", color: "white" }}>
        <tbody>
          <tr>
            <td><b>Incident ID</b></td>
            <td>{incident.incident_id}</td>
          </tr>

          <tr>
            <td><b>Title</b></td>
            <td>{incident.title}</td>
          </tr>

          <tr>
            <td><b>Severity</b></td>
            <td>{incident.severity}</td>
          </tr>

          <tr>
            <td><b>Confidence</b></td>
            <td>{incident.confidence}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}