from pydantic import BaseModel

class Asset(BaseModel):
    assetID: str
    assetName: str
    assetType: str
    location: str
    purchaseDate: str
    initialCost: int
    operationalStatus: str

class PerformanceMetric(BaseModel):
    assetID: str
    uptime: str
    downtime: str
    maintenanceCosts: int
    failureRate: float
    efficiency: float