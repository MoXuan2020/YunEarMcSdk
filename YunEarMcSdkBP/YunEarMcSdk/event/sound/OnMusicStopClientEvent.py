# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMusicStopClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMusicStopClientEvent, self).__init__(callback)
        self.musicName_ = None

    def CreateFromArgs(self, args):
        self.musicName_ = args["musicName"]
