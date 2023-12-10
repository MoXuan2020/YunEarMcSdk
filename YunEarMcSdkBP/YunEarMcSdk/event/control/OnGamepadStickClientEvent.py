# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadStickClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadStickClientEvent, self).__init__(callback)
        self.key_ = None
        self.x_ = None
        self.y_ = None

    def CreateFromArgs(self, args):
        self.key_ = args.get("key")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
