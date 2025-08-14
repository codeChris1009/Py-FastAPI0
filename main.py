from fastapi import FastAPI

from datetime import date

app = FastAPI()


@app.get("/")
def read_root():
    today = date.today()
    week = today.strftime("%A")
    return {"welcomeMessage": f"{week}, Happy Book, Code, Cookie With Padi~"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)