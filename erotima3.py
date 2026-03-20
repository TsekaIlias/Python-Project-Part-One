import time
from erotima1 import generate_random_text, inject_multiplications, compute

if __name__ == "__main__":
    start_time = time.time()
    random_text = generate_random_text(1000000)
    step1_time = time.time() - start_time

    start_time = time.time()
    resulting_text = inject_multiplications(random_text, 100000)
    step2_time = time.time() - start_time

    start_time = time.time()
    total = compute(resulting_text)
    step3_time = time.time() - start_time

    total_time = step1_time + step2_time + step3_time

    print(f"\nSum of products: {total}")
    print(f"\nTime for step 1 (generate_random_text): {step1_time:.5f} seconds")
    print(f"Time for step 2 (inject_multiplications): {step2_time:.5f} seconds")
    print(f"Time for step 3 (compute): {step3_time:.5f} seconds")
    print(f"The total time for everything is: {total_time:.2f}")