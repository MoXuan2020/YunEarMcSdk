# -*- coding: utf-8 -*-

from YunEarMcSdk.event.world.AddEntityClientEvent import AddEntityClientEvent
from YunEarMcSdk.event.world.AddEntityServerEvent import AddEntityServerEvent
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk


@YunEarMcSdk
class YunEarMcSdkTest(object):

    @AddEntityServerEvent
    def AddEntityServerEvent(self, args):
        print self, args

    @AddEntityClientEvent
    def AddEntityClientEvent(self, args):
        print self, args
