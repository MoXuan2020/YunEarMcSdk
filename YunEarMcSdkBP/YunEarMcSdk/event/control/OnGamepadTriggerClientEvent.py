# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnGamepadTriggerClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnGamepadTriggerClientEvent, self).__init__(callback)
        self.key = None
        self.magnitude = None

    def CreateFromArgs(self, args):
        self.key = args.get("key")
        self.magnitude = args.get("magnitude")
