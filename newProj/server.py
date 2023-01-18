from __future__ import annotations

from enum import Enum
from typing import Dict, List, Type


class IndicatorState(Enum):
    ON = 'on'
    OFF = 'off'
    BLINKING = 'blinking'


class Device: #according to factory template 
    DEVICE_TYPES: Dict[str, Type[Device]] = {}
    PREFIX_SN: str = NotImplementedError
    INDICATOR_COUNT: int = 3

    def __init__(self, serial_number: str, indicators: List[str]):
        self.serial_number: str = serial_number
        self.indicators: List[IndicatorState] = [IndicatorState(i) for i in indicators]

    def __init_subclass__(cls, **kwargs):
        cls.DEVICE_TYPES[cls.PREFIX_SN] = cls

    @property
    def status(self) -> str:
        raise NotImplementedError

    @property
    def is_all_off(self) -> bool:
        return all(i == IndicatorState.OFF for i in self.indicators)

    @property
    def is_all_on(self) -> bool:
        return all(i == IndicatorState.ON for i in self.indicators)

    def count_indicators_state(self, state: IndicatorState):
        return self.indicators.count(state)

    @classmethod
    def factory(cls, serial_number: str) -> Device:
        for key, clas in cls.DEVICE_TYPES.items():
            if serial_number.startswith(key):
                return clas
        return None


class Lamp24X(Device):
    PREFIX_SN = '24-X'

    @property
    def status(self):
        return "please upgrade your device"


class Lamp36X(Device):
    PREFIX_SN = '36-X'

    @property
    def status(self):
        if self.is_all_off:
            return "turn on the device"
        elif self.count_indicators_state(IndicatorState.BLINKING) == 2:
            return "Please wait"
        elif self.is_all_on:
            return "ALL is ok"
        else:
            return "unknown status"


class Lamp51B(Device):
    PREFIX_SN = "51-B"

    @property
    def status(self):
        if self.is_all_off:
            return "turn on the device"
        elif any(i == IndicatorState.BLINKING for i in self.indicators):
            return "Please wait"
        elif self.count_indicators_state(IndicatorState.ON) > 1:
            return "ALL is ok"
        else:
            return "unknown status"


def get_response_from_server(res_device):
    sn = res_device['serial_number']
    indicator1 = res_device.get('status_indicator1')
    indicator2 = res_device.get('status_indicator2')
    indicator3 = res_device.get('status_indicator3')
    
    indicators = [indicator1, indicator2, indicator3]
    if sn.isnumeric():
        return "Bad serial number"
    elif cls := Device.factory(sn):
        device = cls(sn, indicators)
        return device.status
    else:
        return "Unknown device"
