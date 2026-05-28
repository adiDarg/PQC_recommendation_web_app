import React, { createContext, useState } from 'react';

const FormContext = createContext({});
function FormProvider({children}){
    const [formData, setFormData] = useState(
        {
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
        });
    }
    function setFormProperty(property, value) {
        setFormData(prevState => ({
            ...prevState,
            [property]: value
        }));
    }

    return (
        <FormContext value={{ formData, setFormProperty, handleClearForm, toggleProblemSelection }}>
            {children}
        </FormContext>
    );
}

export {FormProvider,FormContext}