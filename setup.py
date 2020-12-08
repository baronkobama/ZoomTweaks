# Zoom Tweaks BETA - Setup Container

# Standard Libraries
from os import getcwd, system
import json
# Constants
from bin.constants import (scheduler_config_file)
# ZoomTweaks-PY Functions
from bin.utils import (cache_check, check_reg_key, add_to_startup)


try:
    if cache_check():
        print("Files & dirs created successfully")
    print("Starting startup registry key integrity check")
    with open(scheduler_config_file, "r") as f:
        config = json.load(f)
        if config["startup"] == "0":
            print("No reg key detected, creating key")
            add_to_startup()
            if not type(None) == check_reg_key():
                print("Updating config")
                config.update({"startup": "1"})
        elif config["startup"] == "1":
            if not type(None) == check_reg_key():
                print("Reg key detected, passing")
                pass
            elif type(None) == check_reg_key():
                print("No reg key detected, creating key")
                add_to_startup()
        else:
            print("Unknown value set for startup")
    print("Setup file complete, pushing control to main file")
    system(fr"CMD /c python {getcwd()}\main.py")
    exit(0)
except Exception as exc:
    new_exc = str(exc).split(']')[0].strip('[')
    print("")
    print(f"Caught {new_exc} in setup.py")
    print("Please report this issue on the github")
    print("Link: https://github.com/baronkobama/ZoomTweaks/issues")
    print("Check traceback for more info:")
    print("")
    raise
except KeyboardInterrupt:
    pass
