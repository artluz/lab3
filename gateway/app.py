from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

@app.get("/greeting")
async def greeting(name: str = "Guest"):
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(
                "http://greeting-service:5001/greeting",
                params={"name": name}
            )
            return response.text
        except httpx.ConnectError:
            return "Greeting service unavailable", 503

@app.get("/sum")
async def sum(a: int = 0, b: int = 0):
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(
                "http://sum-service:5002/sum",
                params={"a": a, "b": b}
            )
            return response.text
        except httpx.ConnectError:
            return "Sum service unavailable", 503
