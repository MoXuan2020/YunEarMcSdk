# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadTriggerClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadTriggerClientEvent, self).__init__(callback)
        self.key_ = None
        self.magnitude_ = None

    def CreateFromArgs(self, args):
        self.key_ = args["key"]
        self.magnitude_ = args["magnitude"]
