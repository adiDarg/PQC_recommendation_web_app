import './App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Input from "./components/Input.jsx";
import ShowRecommendation from "./components/ShowRecommendation.jsx";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Input/>}/>
                <Route path="recommendation" element={<ShowRecommendation/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App
