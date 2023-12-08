# -*- coding: utf-8 -*-

from YunEarMcSdk.event.world.AddEntityClientEvent import AddEntityClientEvent
from YunEarMcSdk.event.world.AddEntityServerEvent import AddEntityServerEvent
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk


@YunEarMcSdk
class YunEarMcSdkTest(object):

    @AddEntityServerEvent
    def AddEntityServerEvent(self, event):
        # type: (AddEntityServerEvent) -> None
        print event.entity.isEntityOnGround()

    @AddEntityClientEvent
    def AddEntityClientEvent(self, event):
        # type: (AddEntityClientEvent) -> None
        print event.entity.isEntityOnGround()
