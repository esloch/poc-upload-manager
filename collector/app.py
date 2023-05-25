import time
import os
import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loguru import logger


ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

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
        
        # TODO: Fix path root to write into data directory
        logger.info(event.src_path)
        # print(dir(event))
        # breakpoint()
        if event.is_directory:
            file_name = os.path.basename(event.src_path)
            today = datetime.datetime.today()
            year = today.year
            logger.info(f"New file created: {file_name}, {today}, {year}")
            return

if __name__ == '__main__':
    logger.debug(os.getcwd())
    logger.add("file.log", rotation="500 MB")  # Add a file logger with rotation
    observer = Observer()
    observer.schedule(FileHandler(), path=f"{ROOT_DIR}/collector/data/partners")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
