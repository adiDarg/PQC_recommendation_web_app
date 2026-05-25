import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from h11 import Response
from pydantic import BaseModel
from typing import List
from app.calculate_matches import calculate_matches, calculate_penalties_coefficients

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://pqc-recommendation-web-app.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestPayload(BaseModel):
    cpuIdle: float
    cpuPeak: float
    tpsAvg: float
    tpsPeak: float
    ramUsage: float
    nistLevel: int
    keyReuse: int
    weightBandwidth: float
    weightCompute: float
    weightMemory: float
    weightSecurity: float
    allowedProblems: List[str]


pipeline = joblib.load("./joblib_files/pipeline.joblib")
knn = joblib.load('./joblib_files/knn_model.joblib')


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204, headers=[])


@app.post("/predict")
def predict_data(data: RequestPayload):
    original_order = ['idle_CPU_usage', 'peak_CPU_usage', 'avg_throughput_TPS', 'peak_throughput_TPS', 'RAM_size_GB']
    x_test = [[data.cpuIdle, data.cpuPeak, data.tpsAvg, data.tpsPeak, data.ramUsage]]
    x_test_df = pd.DataFrame(x_test, columns=original_order)

    x_test_scaled = pipeline.transform(x_test_df)
    x_test_scaled.columns = original_order

    peak_tps_weight = 5.0
    x_test_scaled['peak_throughput_TPS'] = x_test_scaled['peak_throughput_TPS'] * peak_tps_weight

    prediction = knn.predict(x_test_scaled)[0]

    coefficients = calculate_penalties_coefficients(data.keyReuse)

    results = calculate_matches(
        coefficients[0], coefficients[1], coefficients[2], coefficients[3],
        data.nistLevel, data.keyReuse, data.allowedProblems,
        data.weightBandwidth, data.weightCompute,
        data.weightMemory, data.weightSecurity
    )

    return results[prediction]
