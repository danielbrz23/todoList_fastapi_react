from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # make cross-origin requests (requests from a different 
# protocol/ IP address/ domain name

app = FastAPI()

origins = [
    'http://localhost:5173',
    'localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/', tags=['root'])
async def read_root() -> dict:
    return {"message": 'Welcome to your todolist'}