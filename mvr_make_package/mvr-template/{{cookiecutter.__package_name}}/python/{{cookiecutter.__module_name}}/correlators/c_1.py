
import typing

from mvr_v2.common.utils import Correlator, PayloadInstance


class MyCorrelator(Correlator):
    def execute(self, data: dict) -> typing.List[PayloadInstance]:
        self.logger.info(data)  # remove this line
        # your correlation logic here
        return []
