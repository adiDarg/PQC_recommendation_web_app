import { Link, useLocation } from 'react-router-dom';
import '../styles/Recommendation.css'

function ShowRecommendation() {
    const location = useLocation();
    const { resultData } = location.state || { resultData: { KEM: 'N/A', DSA: 'N/A' } };

    return (
        <div className="form-container recommendation-container">
            <h2 className="recommendation-title">Cryptographic Recommendations</h2>

            <div className="recommendation-card">
                <span className="recommendation-label">Key Encapsulation Mechanism (KEM)</span>
                <div className="recommendation-value">{resultData.KEM}</div>
            </div>

            <div className="recommendation-card">
                <span className="recommendation-label">Digital Signature Algorithm (DSA)</span>
                <div className="recommendation-value">{resultData.DSA}</div>
            </div>

            <Link to="/" className="back-link">
                ← Go back to input page
            </Link>
        </div>
    );
}

export default ShowRecommendation;