"""
The ``geoist`` package contains subpackages for different geophysical methods
and other utilities.

See the API reference for each subpackage for a list of all functions and
classes defined by it.
"""

# Set up data directory
import appdirs
import os
from ._version import get_versions as _get_versions

# Get the version number through versioneer
__version__ = _get_versions()["version"]
__commit__ = _get_versions()["full-revisionid"]

USER_DATA_PATH = appdirs.user_data_dir('geoist')
try:
    os.makedirs(USER_DATA_PATH)
except FileExistsError as error:
    print(error)

EXAMPLES_PATH = os.path.join(USER_DATA_PATH, 'examples')
try:
    os.makedirs(EXAMPLES_PATH)
except FileExistsError as error:
    print(error)
	
TEMP_PATH = os.path.join(USER_DATA_PATH, 'temp')
try:
    os.makedirs(TEMP_PATH)
except FileExistsError as error:
    print(error)

DATA_PATH = os.path.join(USER_DATA_PATH, 'data')
try:
    os.makedirs(DATA_PATH)
except FileExistsError as error:
    print(error)
	
# Set a parameter to control default print format for floats
FLOAT_FORMAT = "{:.3e}"

# Set where figures are saved
FIGURE_PATH = None

def get_ext(filename):
    """Extract the extension of the filename."""
    ext = os.path.splitext(filename)[1].lower()
    return ext

from geoist import _logger as log
from geoist import _version as ver

log.info('import')
