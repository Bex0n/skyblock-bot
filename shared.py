import threading

running_event = threading.Event()
stop_event = threading.Event()

def is_running():
    return running_event.is_set() and not stop_event.is_set()
