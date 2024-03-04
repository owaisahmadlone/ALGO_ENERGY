from fastapi import APIRouter
from models.Models import Asset,PerformanceMetric
from bson import ObjectId
from config.db import conn

from schemas.Schema import AssetEntity,AssetsEntity

asset = APIRouter()

@asset.get('/get-all-assets')
async def find_all_assets():
    return AssetsEntity(conn.asset_management.Assets.find())

@asset.get('/get-asset-by-id/{id}')
async def find_asset_by_id(id):
    return AssetEntity(conn.asset_management.Assets.find_one({"_id": ObjectId(id)}))


@asset.post('/create-asset')
async def create_asset(asset: Asset):
    conn.asset_management.Assets.insert_one(dict(asset))
    return AssetsEntity(conn.asset_management.Assets.find())

@asset.put('/modify-asset/{id}')
async def update_asset(id : str, asset:Asset):
    conn.asset_management.Assets.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(asset)})

    return AssetEntity(conn.asset_management.Assets.find_one({"_id":ObjectId(id)}))

@asset.delete('/delete-asset/{id}')
async def delete_asset(id):
    return conn.asset_management.Assets.find_one_and_delete({"_id":ObjectId(id)})

