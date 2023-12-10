# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StartDestroyBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StartDestroyBlockServerEvent, self).__init__(callback)
        self.pos = None
        self.blockName = None
        self.auxValue = None
        self.playerId = None
        self.dimensionId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.pos = args.get("pos")
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")
        self.playerId = args.get("playerId")
        self.dimensionId = args.get("dimensionId")
        self.cancel = args.get("cancel")
