from fastapi import FastAPI

# You have to instantiate the FastAPI class
app = FastAPI()

# Here you define the type of operation, so get, post, put, delete
# You also provide the path for the URL (this is after the .co.uk)
# Decorator is also needed and this is part of the FastAPI documentation
@app.get("/")
async def root():
    # This is where the body of the API can be adapted depending on the operation and needs
    return {"message": "Hello World"}
