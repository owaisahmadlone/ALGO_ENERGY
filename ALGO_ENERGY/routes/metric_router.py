import pymongo
from fastapi import APIRouter
from models.Models import Asset,PerformanceMetric
from bson import ObjectId
from config.db import conn

from schemas.Schema import metricEntity,metricsEntity

metric = APIRouter()

@metric.get('/get-all-metrics')
async def find_all_metrics():
    return metricsEntity(conn.asset_management.PerformanceMetrics.find())

@metric.get('/get-asset-by-id/{id}')
async def find_metric_by_id(id):
    return metricEntity(conn.asset_management.PerformanceMetrics.find_one({"_id": ObjectId(id)}))


@metric.post('/create-metric')
async def create_metric(metric: PerformanceMetric):
    conn.asset_management.PerformanceMetrics.insert_one(dict(metric))
    return metricEntity(conn.asset_management.PerformanceMetrics.find())

@metric.put('/modify-metric/{id}')
async def update_metric(id : str,metric: PerformanceMetric):
    conn.asset_management.PerformanceMetrics.find_one_and_update({"_id":ObjectId(id)},{"$set": dict(metric)})

    return metricEntity(conn.asset_management.PerformanceMetrics.find_one({"_id":ObjectId(id)}))

@metric.delete('/delete-asset/{id}')
async def delete_metric(id):
    return metricEntity(conn.asset_management.PerformanceMetrics.find_one_and_delete({"_id":ObjectId(id)}))

@metric.get('/average-downtime')
async def average_downtime():
    all_metrics = metricsEntity(conn.asset_management.PerformanceMetrics.find())
    leng = len(all_metrics)
    total_downtime = 0
    for item in all_metrics:
        total_downtime += item["downtime"]
    average_downt = total_downtime/leng
    return { "average downtime" : average_downt}

@metric.get('/total-maintenance-costs')
async def total_maintenance_costs():
    sum = 0
    for item in metricsEntity(conn.asset_management.PerformanceMetrics.find()):
        sum += item["maintenanceCosts"]
    return {"total maintenace costs": sum}

@metric.get('/least_reliable_assests')
async def least_reliable_10_assests():
    return metricsEntity(conn.asset_management.PerformanceMetrics.find({ }).sort({"failureRate": -1}).limit(10))

