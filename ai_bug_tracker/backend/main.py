# FastAPI entry point placeholder
from fastapi import FastAPI
from routes import auth, bugs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Bug Tracker API")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bugs.router, prefix="/bugs", tags=["Bugs"])

@app.get("/")
def root():
    return {"msg": "AI Bug Tracker API is running"}
