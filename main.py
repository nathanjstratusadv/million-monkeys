from time import perf_counter

from app.tasks import add


def main():
    start = perf_counter()
    result = add.delay(1, 3)
    print(f'Task sent in {perf_counter() - start} seconds')
    print(result.get())
    print(f'Task result retrieved in {perf_counter() - start} seconds')


if __name__ == '__main__':
    main()
