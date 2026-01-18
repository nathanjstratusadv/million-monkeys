import sys
from time import perf_counter

from dotenv import load_dotenv

load_dotenv()

from app.tasks import solve_user_request


def main():
    start = perf_counter()

    print('Running...')

    if len(sys.argv) < 2:
        print("Usage: python run_workflow.py <user_request>")
        sys.exit(1)


    user_request = ' '.join(sys.argv[1:])

    result = solve_user_request.delay(user_request)

    print(f"Result: {result.get()}")

    end = perf_counter()

    print(f"Took {end - start:.2f} seconds")


if __name__ == '__main__':
    main()
