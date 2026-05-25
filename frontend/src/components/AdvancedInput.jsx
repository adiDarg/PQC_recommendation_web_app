function AdvancedInput({style, formData, setFormProperty, toggleProblemSelection}) {
    return (
        <div style={style} className="form-container">
            <h3 className="section-title">General Parameters</h3>
            {/* NIST Security Level */}
            <div className="form-group">
                <label htmlFor="nist-level" className="form-label">
                    Minimum NIST Security Level
                </label>
                <select
                    id="nist-level"
                    className="form-input"
                    defaultValue=""
                    value={formData.nistLevel}
                    onChange={(e) => setFormProperty("nistLevel", e.target.value)}>
                    <option value="1">Level 1</option>
                    <option value="3">Level 3</option>
                    <option value="5">Level 5</option>
                </select>
            </div>

            {/* Key Reuse Factor */}
            <div className="form-group">
                <label htmlFor="key-reuse" className="form-label">
                    Key Reuse Factor
                    <span className="label-hint">How many times a key is used before a new exchange</span>
                </label>
                <input
                    id="key-reuse"
                    type="number"
                    min="1"
                    placeholder="1"
                    className="form-input"
                    value={formData.keyReuse}
                    onChange={(e) => setFormProperty("keyReuse", e.target.value)}
                />
            </div>

            <h3 className="section-title">Algorithm Optimization Weights</h3>
            <p className="section-subtitle">Adjust the relative importance of each metric (Default is 1)</p>

            {/* Weights Grid */}
            <div className="form-grid">
                <div className="form-group">
                    <label htmlFor="weight-bandwidth" className="form-label">Bandwidth Impact</label>
                    <input
                        id="weight-bandwidth"
                        type="number" min="0"
                        step="0.1"
                        placeholder="1"
                        className="form-input"
                        value={formData.weightBandwidth}
                        onChange={(e) => setFormProperty("weightBandwidth", e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="weight-compute" className="form-label">Compute Power</label>
                    <input
                        id="weight-compute"
                        type="number"
                        min="0"
                        step="0.1"
                        placeholder="1"
                        className="form-input"
                        value={formData.weightCompute}
                        onChange={(e) => setFormProperty("weightCompute", e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="weight-memory" className="form-label">System Memory</label>
                    <input
                        id="weight-memory"
                        type="number"
                        min="0"
                        step="0.1"
                        placeholder="1"
                        className="form-input"
                        value={formData.weightMemory}
                        onChange={(e) => setFormProperty("weightMemory", e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="weight-security" className="form-label">Security Margin</label>
                    <input
                        id="weight-security"
                        type="number"
                        min="0"
                        step="0.1"
                        placeholder="1"
                        className="form-input"
                        value={formData.weightSecurity}
                        onChange={(e) => setFormProperty("weightSecurity", e.target.value)}
                    />
                </div>

            </div>
            <div className="form-group mathematical-problems-section">
                    <label className="form-label text-center">
                        Allowed Mathematical Problems
                        <span className="label-hint">Select one or more foundational variants</span>
                    </label>
                    <div className="checkbox-row-group">
                        {['Lattice', 'Codes', 'Stateless Hash'].map((problem) => (
                            <label key={problem} className="custom-checkbox-card">
                                <input
                                    type="checkbox"
                                    checked={formData.allowedProblems.includes(problem)}
                                    onChange={() => toggleProblemSelection(problem)}
                                />
                                <span className="checkbox-text">{problem}</span>
                            </label>
                        ))}
                    </div>
                </div>
        </div>
    )
}

export default AdvancedInput