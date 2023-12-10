# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadStickClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadStickClientEvent, self).__init__(callback)
        self.key = None
        self.x = None
        self.y = None

    def CreateFromArgs(self, args):
        self.key = args.get("key")
        self.x = args.get("x")
        self.y = args.get("y")
