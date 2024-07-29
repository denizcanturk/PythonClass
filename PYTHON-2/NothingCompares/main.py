import time

n = 10000000
numbers = list(range(1, n + 1))

start_time = time.perf_counter()

squares = [i * i for i in numbers]

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")

# import time

# n = 10000000
# numbers = list(range(1, n + 1))

# start_time = time.time()

# squares = [i * i for i in numbers]

# end_time = time.time()
# elapsed_time = end_time - start_time

# print(f"Time taken: {elapsed_time} seconds")
