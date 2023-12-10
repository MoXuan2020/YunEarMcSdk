# -*- coding: utf-8 -*-

from YunEarMcSdk.event.entity.HealthChangeBeforeServerEvent import HealthChangeBeforeServerEvent
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk


@YunEarMcSdk
class YunEarMcSdkTest(object):

    @HealthChangeBeforeServerEvent
    def HealthChangeBeforeServerEvent(self, event):
        # type: (HealthChangeBeforeServerEvent) -> None
        if event.from_ > event.to_:
            event.cancel_ = True
