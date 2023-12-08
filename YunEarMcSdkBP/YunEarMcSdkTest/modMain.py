# -*- coding: utf-8 -*-

from YunEarMcSdk.event.world.AddEntityServerEvent import AddEntityServerEvent
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk


@YunEarMcSdk
class YunEarMcSdkTest(object):

    @AddEntityServerEvent
    def AddEntityServerEvent(self, event):
        # type: (AddEntityServerEvent) -> None
        pos = event.entity.GetPos()
        event.entity.SetPos((pos[0], pos[1] + 5, pos[2]))
