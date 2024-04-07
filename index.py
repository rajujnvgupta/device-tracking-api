###import statement

from fastapi import FastAPI
from routes.device import device_router


##Create app
app = FastAPI()

app.include_router(device_router)

