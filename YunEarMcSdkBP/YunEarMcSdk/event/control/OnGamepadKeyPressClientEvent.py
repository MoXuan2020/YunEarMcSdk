# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadKeyPressClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadKeyPressClientEvent, self).__init__(callback)
        self.screenName_ = None
        self.key_ = None
        self.isDown_ = None

    def CreateFromArgs(self, args):
        self.screenName_ = args.get("screenName")
        self.key_ = args.get("key")
        self.isDown_ = args.get("isDown")
