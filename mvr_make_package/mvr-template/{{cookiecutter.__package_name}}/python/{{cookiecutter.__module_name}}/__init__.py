
import importlib
import os
import sys
from pathlib import Path

import ncs

_pkg_dir = Path(__file__).parent.parent.parent.parent
_mvr_path = os.path.join(_pkg_dir, "mvr-v2", "python")
if _mvr_path not in sys.path:
    sys.path.append(_mvr_path)


class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')
        _e = importlib.import_module(".execution", package="mvr_v2")
        self.register_action("{{cookiecutter.__package_name}}-ap", _e.MvrActionCb)

    def teardown(self):
        self.log.info('Main FINISHED')
