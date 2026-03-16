import signal
import time


def signal_handler(sig, frame):
    print("\nYou think you can leave my programme? I don’t think so.")


signal.signal(signal.SIGINT, signal_handler)


while True:
    print("Hello, there")
    time.sleep(0.5)
