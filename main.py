from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

df = pd.read_csv('./data/smallutilization2019.csv')

@app.get("/")
async def root():
    return {"this is an API service for MN code details"}

@app.get('/preview', methods=["GET"])
async def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/icd/<value>', methods=['GET'])
async def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.get('/icd/<value>/sex/<value2>')
async def icdcode2(value, value2):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)