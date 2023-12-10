# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadControllerLayoutChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadControllerLayoutChangeClientEvent, self).__init__(callback)
        self.action = None
        self.newKey = None
        self.oldKey = None

    def CreateFromArgs(self, args):
        self.action = args.get("action")
        self.newKey = args.get("newKey")
        self.oldKey = args.get("oldKey")
