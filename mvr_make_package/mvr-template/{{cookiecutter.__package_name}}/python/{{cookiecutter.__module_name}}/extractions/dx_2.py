
import typing

from mvr_v2.common.utils import Dict2, Dx, XQuery


class DeviceDetail2(Dx):
    def data_source(self, device_name: str) -> XQuery:
        self.q.xpath = f"/devices/device[name='{device_name}']"
        self.q.params = {
            "ip": "address",
            "port": "port",
            "ned-id": "device-type/cli/ned-id",
            "state": "state/admin-state",
            "ssh-algo": "ssh-algorithms/public-key"
        }
        return self.q

    def compute_vars(self, _p: Dict2) -> typing.Union[dict, Dict2]:
        _p["device-vendor"] = "xr" if "xr" in _p["ned-id"] else "unknown"
        return _p

    def devices_to_be_synced(self, _p: Dict2) -> list:
        return []

# a few other Dx classes
