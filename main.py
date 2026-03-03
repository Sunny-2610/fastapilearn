from fastapi import FastAPI

app = FastAPI()

items = ["item1", "item2", "item3"]

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/items")
def get_items():
    return items    