# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PerspChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PerspChangeClientEvent, self).__init__(callback)
        self._from = None
        self.to = None

    def CreateFromArgs(self, args):
        self._from = args.get("from")
        self.to = args.get("to")
