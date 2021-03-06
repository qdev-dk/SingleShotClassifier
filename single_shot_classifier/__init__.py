from configparser import ConfigParser
from pathlib import Path
import logging

from ._version import get_versions
from .loading import *
from .fitting import *
from .plotting import *
from .readout import *


__version__ = get_versions()["version"]
del get_versions


import single_shot_classifier
from single_shot_classifier.telemetry import start_telemetry


CONFIG_PATH = (
    Path(Path(single_shot_classifier.__file__).parent) / "conf" / "telemetry.ini"
)

telemetry_config = ConfigParser()
telemetry_config.read(CONFIG_PATH)

if telemetry_config["Telemetry"].getboolean("enabled"):
    start_telemetry()

logger = logging.getLogger(__name__)
logger.info(f"Imported single_shot_classifierversion: {__version__}")

