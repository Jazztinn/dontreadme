from fastapi import FastAPI
from pydantic import BaseModel
# MedTriage: symptom -> urgency classifier for under-resourced clinics
app = FastAPI(title="MedTriage API")

class Symptoms(BaseModel):
    text: str

@app.post("/triage")
def triage(s: Symptoms):
    return {"urgency": "see_doctor_soon"}
