import ray
import time

@ray.remote
def hello_world():
    return "hello world"
ray.init()

while True:
    print(ray.get(hello_world.remote()))
    time.sleep(1)
