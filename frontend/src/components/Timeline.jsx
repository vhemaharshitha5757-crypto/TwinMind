export default function Timeline({ incident }) {
  if (!incident || !incident.timeline) return null;

  return (
    <div
      style={{
        background: "#1e293b",
        padding: 25,
        borderRadius: 12,
        marginBottom: 30,
      }}
    >
      <h2>Timeline</h2>

      <ul>
        {incident.timeline.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}