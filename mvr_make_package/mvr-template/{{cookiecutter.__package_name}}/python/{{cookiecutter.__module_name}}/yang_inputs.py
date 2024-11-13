
from mvr_v2.common.utils import YangInput


class Main(YangInput):
    def yang_inputs(self, _input):
        self.input = {
            "device-name": _input.inputs.device
        }

    def devices_to_be_synced(self, _p):
        return _p.device_name
