# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayMusicClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayMusicClientEvent, self).__init__(callback)
        self.name_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.name_ = args["name"]
        self.cancel_ = args["cancel"]
