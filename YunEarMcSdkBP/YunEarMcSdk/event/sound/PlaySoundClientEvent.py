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
        self.name_ = args["name"]
        self.pos_ = args["pos"]
        self.volume_ = args["volume"]
        self.pitch_ = args["pitch"]
        self.cancel_ = args["cancel"]
