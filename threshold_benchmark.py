import gc
import sys
import time


print(gc.get_threshold())
print(gc.get_count())


class A:
    def __init__(self):
        self.a = self


start = time.perf_counter()

lst = []
for _ in range(5000000):
    lst.append(A())
    # print(gc.get_count())

end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds with enabled gc")


start = time.perf_counter()

gc.set_threshold(50000, 100, 500)

lst = []
for _ in range(5000000):
    lst.append(A())
    # print(gc.get_count())

end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds with extended threshold")


gc.disable()
start = time.perf_counter()

lst = []
for _ in range(5000000):
    lst.append(A())
    # print(gc.get_count())

end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds with disabled gc")

print(gc.get_threshold())
print(gc.get_count())
gc.collect(0)
print(gc.get_count())


gc.set_threshold(50, 10, 5)

print(gc.get_count())# 0 0 0
# 49 0 0
# 0 1 0
# 49 1 0
# 0 2 0
# 49 9 0
# 0 0 1