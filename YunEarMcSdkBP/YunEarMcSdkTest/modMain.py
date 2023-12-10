# -*- coding: utf-8 -*-

from YunEarMcSdk.event.world.AddEntityServerEvent import AddEntityServerEvent
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk


@YunEarMcSdk
class YunEarMcSdkTest(object):

    @AddEntityServerEvent
    def AddEntityServerEvent(self, event):
        print event
