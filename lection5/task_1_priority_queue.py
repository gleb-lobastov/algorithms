import heap_optimized as heap

TESTING = True

COMMAND = 0
ARG = 1
INSERT = 'Insert'.lower()
EXTRACT = 'ExtractMax'.lower()


def process(commands):
    priority_queue = heap.Heap()
    results = []
    for command in commands:
        command = command.lower().split()
        if command[COMMAND] == INSERT:
            priority_queue.insert(int(command[ARG]))
        elif command[COMMAND] == EXTRACT:
            results.append(priority_queue.extract_top())
    return results


def main():
    command_count = int(input())
    commands = [input() for _ in range(command_count)]
    for output in process(commands):
        print(output)


def test():
    import timeit
    import random

    assert process(['Insert 200', 'ExtractMax']) == [200]
    assert process(['Insert 200', 'Insert 10', 'ExtractMax', 'Insert 5', 'Insert 500', 'ExtractMax']) == [200, 500]

    timing = timeit.timeit(lambda: process(
        'ExtractMax' if random.random() < 1/3 else
        'Insert {}'.format(random.randint(1, 10 ** 9 - 1))
        for _ in range(99999, 1, -1)
    ), number=1)
    assert timing < 3
    print('tests passed')


if __name__ == "__main__":
    (main if not TESTING else test)()
