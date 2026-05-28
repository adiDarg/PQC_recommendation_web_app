import { Link, useLocation } from 'react-router-dom';
import '../styles/Recommendation.css'

function ShowRecommendation() {
    const location = useLocation();

    // Default fallback structured to match your new API schema
    const { resultData } = location.state || {
        resultData: {
            KEM: { name: 'N/A', fullName: 'N/A', category: 'N/A', description: 'No recommendation available.' },
            DSA: { name: 'N/A', fullName: 'N/A', category: 'N/A', description: 'No recommendation available.' }
        }
    };

    return (
        <div className="form-container recommendation-container">
            <h2 className="recommendation-title">Cryptographic Recommendations</h2>

            {/* KEM Section */}
            <div className="recommendation-card">
                <span className="recommendation-label">Key Encapsulation Mechanism (KEM)</span>
                <div className="recommendation-value">{resultData.KEM.name}</div>
                <div className="recommendation-full-name">{resultData.KEM.fullName}</div>
                <div className="recommendation-category">Category: {resultData.KEM.category}</div>
                <p className="recommendation-description">{resultData.KEM.description}</p>
            </div>

            {/* DSA Section */}
            <div className="recommendation-card">
                <span className="recommendation-label">Digital Signature Algorithm (DSA)</span>
                <div className="recommendation-value">{resultData.DSA.name}</div>
                <div className="recommendation-full-name">{resultData.DSA.fullName}</div>
                <div className="recommendation-category">Category: {resultData.DSA.category}</div>
                <p className="recommendation-description">{resultData.DSA.description}</p>
            </div>

            <Link to="/" className="back-link">
                ← Go back to input page
            </Link>
        </div>
    );
}

export default ShowRecommendation;
