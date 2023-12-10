# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadKeyPressClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadKeyPressClientEvent, self).__init__(callback)
        self.screenName = None
        self.key = None
        self.isDown = None

    def CreateFromArgs(self, args):
        self.screenName = args.get("screenName")
        self.key = args.get("key")
        self.isDown = args.get("isDown")
