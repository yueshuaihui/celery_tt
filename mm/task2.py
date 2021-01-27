import time
from mm import app


@app.task(bind=True, name="aaa")
def add2(self, x, y):
    time.sleep(10)
    return x + y
