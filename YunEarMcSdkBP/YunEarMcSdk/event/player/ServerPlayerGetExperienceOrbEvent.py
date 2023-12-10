# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerGetExperienceOrbEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerGetExperienceOrbEvent, self).__init__(callback)
        self.playerId_ = None
        self.experienceValue_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.experienceValue_ = args.get("experienceValue")
        self.cancel_ = args.get("cancel")
