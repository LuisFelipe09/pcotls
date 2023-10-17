from fastapi import FastAPI
import ssl

app = FastAPI()


@app.get("/")
async def root():
    return {"message": ssl.OPENSSL_VERSION}
