import uvicorn


def run():
    # ToDO: Remove when we have the proper Makefile or Maskfile as task runner
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    run()
