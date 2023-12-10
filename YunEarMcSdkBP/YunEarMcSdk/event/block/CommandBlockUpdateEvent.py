# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CommandBlockUpdateEvent(ServerEvent):

    def __init__(self, callback):
        super(CommandBlockUpdateEvent, self).__init__(callback)
        self.playerId_ = None
        self.playerUid_ = None
        self.command_ = None
        self.isBlock_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.victimId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.playerUid_ = args.get("playerUid")
        self.command_ = args.get("command")
        self.isBlock_ = args.get("isBlock")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.victimId_ = args.get("victimId")
        self.cancel_ = args.get("cancel")
