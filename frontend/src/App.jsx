import "./App.css";
import { useState } from "react";

function App() {
  const [log, setLog] = useState("");
  const [result, setResult] = useState(null);

  const analyzeLog = async () => {
    const response = await fetch("http://localhost:8000/analyze-log", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: log }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="container">
      <div className="background-glow"></div>

      <h1>🚀 DevOps Mentor AI</h1>

      <p className="subtitle">
        AI-powered log analyzer for Docker, Kubernetes and CI/CD systems
      </p>

      <div className="card">
        <textarea
          placeholder="Paste your logs here..."
          value={log}
          onChange={(e) => setLog(e.target.value)}
        />

        <button onClick={analyzeLog}>Analyze Logs</button>

        {result && (
          <div className="result">
            <h2>Analysis Result</h2>

            <p>
              <strong>Problem:</strong> {result.problem}
            </p>

            <p>
              <strong>Root Cause:</strong> {result.root_cause}
            </p>

            <p>
              <strong>Fix:</strong> {result.fix}
            </p>
          </div>
        )}
      </div>

      <div className="terminal">
        <p>$ docker ps</p>
        <p>$ kubectl get pods</p>
        <p>$ terraform apply</p>
        <p>$ helm install monitoring</p>
      </div>
    </div>
  );
}

export default App;
