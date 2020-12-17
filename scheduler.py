# Zoom Tweaks - Scheduler Container

# Standard Libraries
import time
# External Libraries
import schedule
# Constants
from bin.utils import (class_amount_file, class_time_file, class_link_file,
                       scheduler_config_file)
# ZoomTweaks-PY Functions
from bin.utils import (config_file_check, job, proc_init)
from bin.logger import log

proc_init()
log.debug("Entering scheduler.py")
schedule.every().monday.at('07:19').do(job)
schedule.every().tuesday.at('07:19').do(job)
schedule.every().wednesday.at('07:19').do(job)
schedule.every().thursday.at('07:19').do(job)
schedule.every().friday.at('07:19').do(job)
log.debug("Scheduled jobs")

try:
    if not config_file_check(class_amount_file) and not config_file_check(class_time_file) and not config_file_check(class_link_file) and not config_file_check(scheduler_config_file):
        log.debug("Found no issues with files, running scheduler")
        print("Entering sleep mode")
        while True:
            schedule.run_pending()
            time.sleep(1)
except FileNotFoundError:
    log.debug("Missing files, running job")
    job()
except KeyboardInterrupt:
    print("Exiting...")
    pass
