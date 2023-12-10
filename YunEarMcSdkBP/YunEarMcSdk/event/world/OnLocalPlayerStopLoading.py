# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnLocalPlayerStopLoading(ClientEvent):

    def __init__(self, callback):
        super(OnLocalPlayerStopLoading, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
