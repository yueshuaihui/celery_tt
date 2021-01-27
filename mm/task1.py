import time
from mm import app


@app.task
def add(x, y):
    # time.sleep(5)
    return x + y
