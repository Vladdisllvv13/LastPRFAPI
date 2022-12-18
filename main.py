import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi import FastAPI
import uvicorn
from core.router import set_routers_group
from core.router import set_routers_student
from core import settings

app = FastAPI(title="Sharaga")

@app.on_event("startup")
async def startup():
    set_routers_student(app)
    set_routers_group(app)

@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app",  host = settings.HOST, port = settings.PORT, reload=True)