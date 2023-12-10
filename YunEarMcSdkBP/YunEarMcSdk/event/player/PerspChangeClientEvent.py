# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PerspChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PerspChangeClientEvent, self).__init__(callback)
        self.from_ = None
        self.to_ = None

    def CreateFromArgs(self, args):
        self.from_ = args.get("from")
        self.to_ = args.get("to")
