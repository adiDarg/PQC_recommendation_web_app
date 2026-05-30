import BasicInput from "./BasicInput.jsx";
import React, {useContext, useState} from "react";
import AdvancedInput from "./AdvancedInput.jsx";
import { useNavigate } from 'react-router-dom';
import Header from "./Header.jsx";
import '../styles/App.css';
import {FormContext} from "./FormContext.jsx";
import LoadingOverlay from "./LoadingOverlay.jsx";

function Input() {
    const navigate = useNavigate();
    const [showAdvanced, setShowAdvanced] = useState(false);
    const [loading, setLoading] = useState(false)
    const { formData, setFormProperty, handleClearForm, toggleProblemSelection } = useContext(FormContext)

    function handleSetAdvancedInput() {
        setShowAdvanced(prevState => !prevState);
    }

    const handleSubmitData = async (e) => {
        e.preventDefault();
        //Only add loading screen if user has been waiting for over a second
        let loadingTimer = setTimeout(() => {
            setLoading(true);
        }, 1000);

        const payload = {
            cpuIdle: parseFloat(formData.cpuIdle) || 0.0,
            cpuPeak: parseFloat(formData.cpuPeak) || 0.0,
            tpsAvg: parseFloat(formData.tpsAvg) || 0.0,
            tpsPeak: parseFloat(formData.tpsPeak) || 0.0,
            ramUsage: parseFloat(formData.ramUsage) || 0.0,
            nistLevel: parseInt(formData.nistLevel) || 1.0,
            keyReuse: parseInt(formData.keyReuse) || 1,
            weightBandwidth: parseFloat(formData.weightBandwidth) || 1.0,
            weightCompute: parseFloat(formData.weightCompute) || 1.0,
            weightMemory: parseFloat(formData.weightMemory) || 1.0,
            weightSecurity: parseFloat(formData.weightSecurity) || 1.0,
            allowedProblems: formData.allowedProblems
        };

        try {
            const response = await fetch("https://pqc-recommendation-web-app-backend.vercel.app/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            });

            if (!response.ok) {
                throw new Error(`Server responded with status: ${response.status}`);
            }

            const resultData = await response.json();

            clearTimeout(loadingTimer);

            navigate('/recommendation', {state: {resultData}});

        } catch (error) {
            console.error("Failed to fetch prediction:", error);
            clearTimeout(loadingTimer);
            setLoading(false)
        }
    };

    return (
        <div className="app-container">
            {loading && <LoadingOverlay/>}
            <Header/>
            <BasicInput formData={formData} setFormProperty={setFormProperty}/>

            <button onClick={handleSetAdvancedInput}>
                {showAdvanced ? "Hide advanced metrics" : "Show advanced metrics"}
            </button>

            <AdvancedInput style={{display: showAdvanced ? 'block' : 'none'}}
                           formData={formData}
                           setFormProperty={setFormProperty}
                           toggleProblemSelection={toggleProblemSelection}/>

            <div className="form-actions-group">
                <button onClick={handleClearForm} type="button">
                    Clear All Fields
                </button>
                <button onClick={handleSubmitData}>
                    Submit Data
                </button>
            </div>
        </div>
    );
}

export default Input;