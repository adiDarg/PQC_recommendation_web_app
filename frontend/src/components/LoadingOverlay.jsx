import React from 'react';
import '../styles/LoadingOverlay.css';

export default function LoadingOverlay() {
    return (
        <div className="loading-overlay">
            <div className="loading-modal">
                <div className="spinner"></div>
                <h3 className="section-title" style={{ marginTop: '16px' }}>
                    Loading recommendation...
                </h3>
                <p className="section-subtitle">
                    Evaluating parameters against NIST algorithms.
                </p>
            </div>
        </div>
    );
}