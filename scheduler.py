# Zoom Tweaks - Scheduler Container

# Standard Libraries
import time
# External Libraries
import schedule
# Constants
from bin.utils import (class_amount_file, class_time_file, class_link_file,
                       scheduler_config_file)
# ZoomTweaks-PY Functions
from bin.utils import (config_file_check, job)

schedule.every().monday.at('07:19').do(job)
schedule.every().tuesday.at('07:19').do(job)
schedule.every().wednesday.at('07:19').do(job)
schedule.every().thursday.at('07:19').do(job)
schedule.every().friday.at('07:19').do(job)

try:
    if not config_file_check(class_amount_file) and not config_file_check(class_time_file) and not config_file_check(class_link_file) and not config_file_check(scheduler_config_file):
        print("Found no issues with files, running scheduler")
        while True:
            schedule.run_pending()
            time.sleep(1)
except FileNotFoundError:
    print("Missing files, running job")
    job()
except KeyboardInterrupt:
    print("Exiting...")
    pass
