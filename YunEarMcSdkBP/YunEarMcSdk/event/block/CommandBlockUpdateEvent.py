# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CommandBlockUpdateEvent(ServerEvent):

    def __init__(self, callback):
        super(CommandBlockUpdateEvent, self).__init__(callback)
        self.playerId = None
        self.playerUid = None
        self.command = None
        self.isBlock = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.victimId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.playerUid = args.get("playerUid")
        self.command = args.get("command")
        self.isBlock = args.get("isBlock")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.victimId = args.get("victimId")
        self.cancel = args.get("cancel")
