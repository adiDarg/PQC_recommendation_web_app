import '../styles/FormLayouts.css';

function BasicInput({formData, setFormProperty}) {
    return (
        <div className="form-container">
            <h3 className="section-title">System Load & Performance Metrics</h3>
            <p className="section-subtitle">Provide current utilization metrics for accurate analysis.</p>

            <div className="form-grid">
                <div className="form-group">
                    <label htmlFor="cpu-idle" className="form-label">
                        Idle CPU Usage
                        <span className="label-hint">Value between 0 and 1 (e.g., 0.50 = 50%)</span>
                    </label>
                    <input
                        id="cpu-idle"
                        type="number"
                        min="0"
                        max="1"
                        step="0.01"
                        className="form-input"
                        value={formData.cpuIdle}
                        onChange={(e) => setFormProperty("cpuIdle", e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="cpu-peak" className="form-label">
                        Peak CPU Usage
                        <span className="label-hint">Value between 0 and 1 (e.g., 0.90 = 90%)</span>
                    </label>
                    <input
                        id="cpu-peak"
                        type="number"
                        min="0"
                        max="1"
                        step="0.01"
                        className="form-input"
                        value={formData.cpuPeak}
                        onChange={(e) => setFormProperty("cpuPeak", e.target.value)}
                    />
                </div>
            </div>

            <div className="form-grid mt-4">
                <div className="form-group">
                    <label htmlFor="tps-avg" className="form-label">Average Throughout</label>
                    <div className="input-with-unit">
                        <input
                            id="tps-avg"
                            type="number"
                            min="0"
                            className="form-input"
                            value={formData.tpsAvg}
                            onChange={(e) => setFormProperty("tpsAvg", e.target.value)}
                        />
                        <span className="unit-tag">TPS</span>
                    </div>
                </div>

                <div className="form-group">
                    <label htmlFor="tps-peak" className="form-label">Peak Throughput</label>
                    <div className="input-with-unit">
                        <input
                            id="tps-peak"
                            type="number"
                            min="0"
                            className="form-input"
                            value={formData.tpsPeak}
                            onChange={(e) => setFormProperty("tpsPeak", e.target.value)}
                        />
                        <span className="unit-tag">TPS</span>
                    </div>
                </div>
            </div>

            <div className="form-group mt-4">
                <label htmlFor="ram-usage" className="form-label">Typical RAM Memory Available</label>
                <div className="input-with-unit">
                    <input
                        id="ram-usage"
                        type="number"
                        min="0"
                        step="0.1"
                        className="form-input"
                        value={formData.ramUsage}
                        onChange={(e) => setFormProperty("ramUsage", e.target.value)}
                    />
                    <span className="unit-tag">GB RAM</span>
                </div>
            </div>
        </div>
    );
}

export default BasicInput;