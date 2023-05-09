from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

df = pd.read_csv('./data/smallutilization2019.csv')

@app.get("/")
async def root():
    return {"this is an API service for MN code details"}

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/icd/<value>', methods=["GET"])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/icd/<value>/sex/<value2>')
def icdcode2(value, value2):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)