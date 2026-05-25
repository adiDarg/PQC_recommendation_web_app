import {Link, useLocation} from 'react-router-dom';

function ShowRecommendation() {
    const location = useLocation();
    const {resultData} = location.state || {};
        return (
        <div>
            <h3>KEM recommendation: {resultData.KEM}</h3>
            <h3>DSA recommendation: {resultData.DSA}</h3>
            <Link to="/">Go back to input page</Link>
        </div>
    )
}

export default ShowRecommendation