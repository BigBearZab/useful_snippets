import queue
import threading


def _queue_get(q: queue.Queue, output: list) -> list:
    """
    Helper consumer for testing queue producer funcs.
    """

    while True:
        val = q.get()
        if val == "END":
            break
        output.extend(val)
        q.task_done()

    return output


def queue_prod(q):
    for i in range(5):
        q.put(f"Message {i+1}")

    q.put("END")


def test_simple_producer():
    q = queue.Queue()
    out = []
    consumer_thread = threading.Thread(target=_queue_get, args=(q, out))
    consumer_thread.start()
    queue_prod(q)

    consumer_thread.join()

    assert out == ["Message 1", "Message 2", "Message 3", "Message 4", "Message 5"]


if __name__ == "__main__":
    q = queue.Queue()
    out = []
    consumer_thread = threading.Thread(target=_queue_get, args=(q, out))
    consumer_thread.start()
    queue_prod(q)

    consumer_thread.join()
    print(out)
