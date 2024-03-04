from fastapi import FastAPI
from routes.asset_router import asset
from routes.metric_router import metric

app = FastAPI()

# Include routers
app.include_router(asset, prefix="/assets")
app.include_router(metric, prefix="/metrics")







