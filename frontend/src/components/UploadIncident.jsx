import { useState } from "react";
import axios from "axios";

export default function UploadIncident({ setIncident }) {
  const [document, setDocument] = useState(null);
  const [image, setImage] = useState(null);
  const [audio, setAudio] = useState(null);

  const handleAnalyze = async () => {
    const formData = new FormData();

    if (document) formData.append("document", document);
    if (image) formData.append("image", image);
    if (audio) formData.append("audio", audio);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/process",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setIncident(response.data);
    } catch (err) {
      console.error(err);
      alert("Backend connection failed");
    }
  };

  return (
    <div
      style={{
        background: "#1e293b",
        padding: 25,
        borderRadius: 12,
        marginBottom: 30,
      }}
    >
      <h2>Upload Incident</h2>

      <p>Incident Report</p>
      <input
        type="file"
        onChange={(e) => setDocument(e.target.files[0])}
      />

      <br />
      <br />

      <p>Image Metadata</p>
      <input
        type="file"
        onChange={(e) => setImage(e.target.files[0])}
      />

      <br />
      <br />

      <p>Meeting Transcript</p>
      <input
        type="file"
        onChange={(e) => setAudio(e.target.files[0])}
      />

      <br />
      <br />

      <button
        onClick={handleAnalyze}
        style={{
          padding: "12px 24px",
          fontSize: 18,
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
        }}
      >
        Analyze Incident
      </button>
    </div>
  );
}