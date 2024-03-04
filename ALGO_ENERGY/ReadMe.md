# Setup Database

To setup the mongodb database install mongodb commnunity edition@7 on your machine. I have done it on mac brew with the command `brew install mongodb-community@7.0`.
To start the server run `brew services start mongodb-community@7.0` on the terminal.

# Populate and connect to database

 To start updating the database run `mongosh` on a new terminal in the same directory as the file `create_database.js`. once you are on the mongodb console execute the command `load('create_database.js)` to create the database `asset_management` with two collections `Assets` and `PerformanceMetrics`. Each collection will have 10 documents each. On VSCode install `MongoClient` and establish a connection with your database by using the connection string `"mongodb://localhost:27017/asset_management"`, The App is now connected to the database remotely.

 # Run FastAPI App
 To run the Fast API app make sure you've installed `fastapi`, `uvicorn`,`pymongo` on your environment. You can simply pip install them. after doing this run the following command in the same directory as `index.py`:
 `uvicron index:app --reload`. The app is now running at the local url `http://127.0.0.1:8000/docs` where all the functionalities can be tested.