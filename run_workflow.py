import sys
from time import perf_counter

from dotenv import load_dotenv

load_dotenv()

from app.tasks import solve_user_request


def main():
    start = perf_counter()

    if len(sys.argv) < 2:
        print("Usage: python run_workflow.py <user_request>")
        sys.exit(1)

    user_request = ' '.join(sys.argv[1:])

    result = solve_user_request.delay(user_request)
    end = perf_counter()

    print(f"Result: {result.get()}")

    print(f"Time taken: {end - start:.2f} seconds")


if __name__ == '__main__':
    main()
