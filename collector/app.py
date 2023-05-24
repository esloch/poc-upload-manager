import time
import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    """
    Class that handles new file events.

    Attributes:
        None

    Methods:
        on_created(event): Method that is called when a new file is created.
    """

    def on_created(self, event) -> None:
        """
        Method that is called when a new file is created.

        Args:
            event: The event that was triggered by the file creation.

        Returns:
            None
        """
        print(event.src_path)
        # print(dir(event))
        # breakpoint()
        if event.is_directory:
            file_name = os.path.basename(event.src_path)
            today = datetime.datetime.today()
            year = today.year
            print(f"New file created: {file_name}, {today}, {year}")
            return

if __name__ == '__main__':
    # print(os.getcwd())
    observer = Observer()
    observer.schedule(FileHandler(), path='/workspace/repos/infodengue/minio-collector/collector/data/partners')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
