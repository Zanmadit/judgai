import { useState } from "react";
import ReactMarkdown from "react-markdown";
import "./index.css";

function App() {
  const [team, setTeam] = useState("");
  const [github, setGithub] = useState("");
  const [video, setVideo] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("team_name", team);
    formData.append("github_url", github);
    formData.append("video", video);

    try {
      const res = await fetch("http://127.0.0.1:8000/submit", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Error submitting project");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🤖 AI Hackathon Judge</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Team name
          <input
            type="text"
            value={team}
            onChange={(e) => setTeam(e.target.value)}
            required
          />
        </label>

        <label>
          GitHub URL
          <input
            type="url"
            value={github}
            onChange={(e) => setGithub(e.target.value)}
            required
          />
        </label>

        <label>
          Demo video
          <input
            type="file"
            onChange={(e) => setVideo(e.target.files[0])}
            accept="video/*"
            required
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Evaluating..." : "Evaluate Project"}
        </button>
      </form>

      {result && (
        <div className="result">
          <h2>Team: {result.team}</h2>
          <h3>Files checked:</h3>
          <ul>
            {result.files_checked.map((f) => (
              <li key={f}>{f}</li>
            ))}
          </ul>
          <h3>Verdict:</h3>
          <ReactMarkdown>{result.verdict}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;
