use('asset_management')
db.createCollection("Assets")
db.createCollection("PerformanceMetrics")

// Insert 10 assets
for (let i = 1; i <= 10; i++) {
    db.Assets.insertOne({
        "assetID": "A00" + i,
        "assetName": "Machine " + i,
        "assetType": "Machine",
        "location": "Factory " + String.fromCharCode(65 + (i % 5)),
        "purchaseDate": new Date(2023, i % 12, (i % 28) + 1),
        "initialCost": Math.floor(Math.random() * 100000) + 1000,
        "operationalStatus": i % 2 === 0 ? "Operational" : "Under Maintenance"
    });
}

// Insert performance metrics for each asset
for (let i = 1; i <= 10; i++) {
    db.PerformanceMetrics.insertOne({
        "assetID": "A00" + i,
        "uptime": parseFloat((Math.random() * 100).toFixed(2)),
        "downtime": parseFloat((Math.random() * 10).toFixed(2)),
        "maintenanceCosts": Math.floor(Math.random() * 1000) + 100,
        "failureRate": parseFloat((Math.random() * 0.1).toFixed(4)),
        "efficiency": parseFloat((Math.random() * 100).toFixed(2))
    });
}





