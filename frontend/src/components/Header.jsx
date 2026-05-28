
import React from 'react';
import '../styles/Header.css'
function Header() {
  return (
    <div className="pqc-container">
      {/* Main Title */}
      <h1 className="pqc-title">
        Post-Quantum Cryptography (PQC) Recommendation Engine
      </h1>

      {/* Subtitle */}
      <p className="pqc-subtitle">
        Tailored Cryptographic Migration for Banking &amp; Financial Infrastructure
      </p>

      <hr className="pqc-divider" />

      {/* Description */}
      <p className="pqc-description">
        Evaluate your financial application's operational constraints to determine the optimal post-quantum algorithms for your infrastructure.
      </p>

      {/* How it works section */}
      <h2 className="pqc-section-heading">
        How It Works
      </h2>

      <ol className="pqc-steps-list">
        <li className="pqc-step-item">
          <strong className="pqc-step-title">
            1. Input System Parameters
          </strong>
          <span className="pqc-step-text">
            Define your application's unique constraints, including latency thresholds, network throughput, and hardware limitations.
          </span>
        </li>
        <li className="pqc-step-item">
          <strong className="pqc-step-title">
            2. Receive Optimized Blueprint
          </strong>
          <span className="pqc-step-text">
            The engine maps your parameters against PQC performance profiles to recommend a dual-component cryptographic blueprint:
          </span>
          <ul className="pqc-sub-list">
            <li className="pqc-sub-list-item">
              <strong className="pqc-highlight">Key Encapsulation Mechanism (KEM):</strong> Optimized for secure key exchange and forward secrecy.
            </li>
            <li className="pqc-sub-list-item">
              <strong className="pqc-highlight">Digital Signature Algorithm (DSA):</strong> Tailored for high-integrity identity verification and non-repudiation.
            </li>
          </ul>
        </li>
      </ol>
    </div>
  );
}

export default Header