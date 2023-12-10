# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlaySoundClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlaySoundClientEvent, self).__init__(callback)
        self.name = None
        self.pos = None
        self.volume = None
        self.pitch = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.name = args.get("name")
        self.pos = args.get("pos")
        self.volume = args.get("volume")
        self.pitch = args.get("pitch")
        self.cancel = args.get("cancel")
