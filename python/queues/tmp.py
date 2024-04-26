import queue
import threading

# Define a list to store processed messages
# processed_messages = []


def consumer(q, processed_messages):
    while True:
        # Get a message from the queue (blocks until available)
        message = q.get()
        # Check for termination signal (optional)
        if message == "END":
            break
        # Process the message and add it to the list
        processed_messages.append(message)
        # Signal the queue that processing is done
        q.task_done()

    return processed_messages


# Create the queue and consumer thread
proc = []
q = queue.Queue()
consumer_thread = threading.Thread(target=consumer, args=(q, proc))
consumer_thread.start()


# Loop to add messages
def queue_prod(q):
    for i in range(5):
        message = f"Message {i+1}"
        # Add message to the queue
        q.put(message)

    # Add termination signal to the queue
    q.put("END")


queue_prod(q)

# # Loop to add messages
# for i in range(5):
#     message = f"Message {i+1}"
#     # Add message to the queue
#     q.put(message)

# # Add termination signal to the queue
# q.put("END")

# Wait for consumer thread to finish
consumer_thread.join()
# output = consumer_thread.

print(proc)
# Print the processed messages
# print("Processed Messages:", processed_messages)
