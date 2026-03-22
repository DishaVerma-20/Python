# Exponential Backoff

# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# jb baar baar koi insaan password daalta hai and requests for otp vgera toh vo wait krata hai, ye wait dheere dheere bdta jaata haii, exponentially bdta hai, isey he exponentially backoff strategy bolte hai 

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1