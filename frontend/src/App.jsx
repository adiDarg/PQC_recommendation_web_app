import './styles/App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Input from "./components/Input.jsx";
import ShowRecommendation from "./components/ShowRecommendation.jsx";
import {FormProvider} from "./components/FormContext.jsx";
function App() {
    return (
        <FormProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Input/>}/>
                    <Route path="recommendation" element={<ShowRecommendation/>}/>
                </Routes>
            </BrowserRouter>
        </FormProvider>
    )
}

export default App
