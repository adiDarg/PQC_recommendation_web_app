import BasicInput from "./BasicInput.jsx";
import {useState} from "react";
import AdvancedInput from "./AdvancedInput.jsx";
import { useNavigate } from 'react-router-dom'

function Input() {
    const navigate = useNavigate()
    const [showAdvanced, setShowAdvanced] = useState(false)
    const [formData, setFormData] = useState({
        cpuIdle: "0",
        cpuPeak: "0",
        tpsAvg: "0",
        tpsPeak: "0",
        ramUsage: "0",
        nistLevel: "1",
        keyReuse: "1",
        weightBandwidth: "1",
        weightCompute: "1",
        weightMemory: "1",
        weightSecurity: "1",
        allowedProblems: ['Lattice', 'Codes', 'Stateless Hash']
    });

    function setFormProperty(property, value) {
        setFormData(prevState => ({
            ...prevState,
            [property]: value
        }));
    }

    function handleSetAdvancedInput() {
        setShowAdvanced(prevState => !prevState)
    }

    function handleClearForm() {
        setFormData({
                cpuIdle: "0",
                cpuPeak: "0",
                tpsAvg: "0",
                tpsPeak: "0",
                ramUsage: "0",
                nistLevel: "1",
                keyReuse: "1",
                weightBandwidth: "1",
                weightCompute: "1",
                weightMemory: "1",
                weightSecurity: "1",
                allowedProblems: ['Lattice', 'Codes', 'Stateless Hash']
            }
        )
    }

    const toggleProblemSelection = (problem) => {
        setFormData((prevState) => {
            const currentList = prevState.allowedProblems;
            const newList = currentList.includes(problem)
                ? currentList.filter((item) => item !== problem)
                : [...currentList, problem];

            return {
                ...prevState,
                allowedProblems: newList
            };
        });
    };

    const handleSubmitData = async (e) => {
    e.preventDefault();

    // Format the payload
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
        console.log("Prediction output from backend:", resultData);

        navigate('/recommendation', {state: {resultData}})

    } catch (error) {
        console.error("Failed to fetch prediction:", error);
    }
};

    return (
        <div>
            <BasicInput formData={formData} setFormProperty={setFormProperty}/>
            <button onClick={handleSetAdvancedInput}>
                {showAdvanced ? "Hide advanced metrics" : "Show advanced metrics"}
            </button>
            <AdvancedInput style={{display: showAdvanced ? 'block' : 'none'}}
                           formData={formData}
                           setFormProperty={setFormProperty}
                           toggleProblemSelection={toggleProblemSelection}/>
            <div style={{display: "flex", marginBottom: "10px"}}>
                <button onClick={handleClearForm} type="button" className="btn-secondary">
                    Clear All Fields
                </button>
                <button onClick={handleSubmitData}>
                    Submit Data
                </button>
            </div>
        </div>
    )
}

export default Input