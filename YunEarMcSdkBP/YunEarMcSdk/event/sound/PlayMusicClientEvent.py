# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayMusicClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayMusicClientEvent, self).__init__(callback)
        self.name_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.name_ = args.get("name")
        self.cancel_ = args.get("cancel")
