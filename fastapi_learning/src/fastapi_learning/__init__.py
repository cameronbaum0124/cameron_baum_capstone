import uvicorn


if __name__ == "__init__":
    uvicorn.run(app="app.app:app", host="0.0.0.0", port=8000, reload=True)