
from mvr_v2.common.utils import MvrInit, MvrWf

from . import correlators, extractions, template_engines


class Main(MvrWf):
    """
    Main Execution Flow. This is where the logic resides.
    """

    def execute(self, _input_obj):
        """
        This method call triggers the execution
        """
        _m = MvrInit()
        input_obj = _m >> _input_obj
        _ = input_obj >> extractions.dx_1.DeviceDetail1(
            device_name="device-name")
        _ = input_obj >> extractions.dx_2.DeviceDetail2(
            device_name="device-name")
        _ = _m >> correlators.c_1.MyCorrelator() >> template_engines.Te1()
        _ = _m >> correlators.c_1.MyCorrelator() >> template_engines.Te2()
        return _m
