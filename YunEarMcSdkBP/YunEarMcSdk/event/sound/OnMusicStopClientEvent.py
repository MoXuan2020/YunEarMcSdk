# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMusicStopClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMusicStopClientEvent, self).__init__(callback)
        self.musicName = None

    def CreateFromArgs(self, args):
        self.musicName = args.get("musicName")
