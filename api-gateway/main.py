from fastapi import FastAPI, HTTPException
import httpx  # для HTTP-запросов к сервисам

app = FastAPI()

# URL микросервисов (в Docker Compose они доступны по именам)
GREETING_SERVICE_URL = "http://greeting-service:8000/greeting"
SUM_SERVICE_URL = "http://sum-service:8000/sum"

@app.get("/greeting")
async def greeting(name: str = "Anonymous"):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{GREETING_SERVICE_URL}?name={name}")
            return response.text
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Greeting service unavailable")

@app.get("/sum")
async def sum_numbers(a: int, b: int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{SUM_SERVICE_URL}?a={a}&b={b}")
            return response.text
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Sum service unavailable")
