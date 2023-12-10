# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadControllerLayoutChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadControllerLayoutChangeClientEvent, self).__init__(callback)
        self.action_ = None
        self.newKey_ = None
        self.oldKey_ = None

    def CreateFromArgs(self, args):
        self.action_ = args.get("action")
        self.newKey_ = args.get("newKey")
        self.oldKey_ = args.get("oldKey")
