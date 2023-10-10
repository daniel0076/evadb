from datetime import datetime

class StopWatch:
    def __init__(self, title=""):
        self.title = title

    def __enter__(self):
        self.start_time = datetime.now()
        print(f"{self.title}-start: {self.start_time.strftime('%H:%M:%S.%f')}")

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.now()
        elapsed_time = self.end_time - self.start_time
        print(f"{self.title}-end:   {self.end_time.strftime('%H:%M:%S.%f')}, elapsed time(us): {elapsed_time}")

