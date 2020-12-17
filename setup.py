# Zoom Tweaks - Setup Container

# Standard Libraries
from os import getcwd, system
import json
# Constants
from bin.utils import scheduler_config_file
# ZoomTweaks-PY Functions
from bin.utils import (cache_check, check_startup_file, add_to_startup,
                       lfile, proc_init)
from bin.logger import log


try:
    proc_init()
    log.debug("Entering setup.py")
    if cache_check():
        log.debug("Files & dirs created successfully")
    log.debug("Starting startup integrity check")
    with open(scheduler_config_file, "r") as f:
        config = json.load(f)
        if config["startup"] == "0":
            log.debug("Startup file not detected, creating")
            add_to_startup()
            if not type(None) == check_startup_file():
                log.debug("Updating config")
                config["startup"] = "1"
                with open(scheduler_config_file, "w") as file:
                    json.dump(config, file)
                log.debug("Updated config and wrote startup file")
        elif config["startup"] == "1":
            if not type(None) == check_startup_file():
                log.debug("Startup file detected, passing")
                pass
            elif type(None) == check_startup_file():
                log.debug("Startup file not detected, creating")
                add_to_startup()
        else:
            log.debug("Unknown value set for startup")
    log.debug("Setup file complete, pushing control to main file")
    cwd = '"' + getcwd() + '"'
    system(fr"CMD /c python {cwd}\main.py")
    exit(0)
except Exception as exc:
    new_exc = str(exc).split(']')[0].strip('[')
    log.debug(f"Caught {new_exc} in setup.py")
    log.debug("Please report this issue on the github")
    log.debug("Link: https://github.com/baronkobama/ZoomTweaks/issues")
    log.debug("Check console traceback for more info:")
    print(f"Check {lfile} for more info (debug log)")
    raise
except KeyboardInterrupt:
    pass
