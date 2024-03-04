def AssetEntity(item) -> dict:
    return {
        "assetID":item["assetID"],
        "assetName": item["assetName"],
        "assetType": item["assetType"],
        "location": item["location"],
        "purchaseDate": str(item["purchaseDate"]),
        "initialCost": str(item["initialCost"]),
        "operationalStatus": item["operationalStatus"]
    }

def AssetsEntity(entity)-> list:
    return [AssetEntity(item) for item in entity]


def metricEntity(item) -> dict:
    return {
        "assetID": item["assetID"],
        "uptime": item["uptime"],
        "downtime": item["downtime"],
        "maintenanceCosts": item["maintenanceCosts"],
        "failureRate": item["failureRate"],
        "efficiency": item["efficiency"]
    }

def metricsEntity(entity) -> list:
    return [metricEntity(item) for item in entity]
