# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GridComponentSizeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GridComponentSizeChangedClientEvent, self).__init__(callback)
        self.path = None

    def CreateFromArgs(self, args):
        self.path = args.get("path")
