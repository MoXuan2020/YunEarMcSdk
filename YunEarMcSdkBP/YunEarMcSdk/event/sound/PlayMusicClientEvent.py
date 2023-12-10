# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayMusicClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayMusicClientEvent, self).__init__(callback)
        self.name = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.name = args.get("name")
        self.cancel = args.get("cancel")
