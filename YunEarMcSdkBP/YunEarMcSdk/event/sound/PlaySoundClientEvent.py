# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlaySoundClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlaySoundClientEvent, self).__init__(callback)
        self.name_ = None
        self.pos_ = None
        self.volume_ = None
        self.pitch_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.name_ = args.get("name")
        self.pos_ = args.get("pos")
        self.volume_ = args.get("volume")
        self.pitch_ = args.get("pitch")
        self.cancel_ = args.get("cancel")
