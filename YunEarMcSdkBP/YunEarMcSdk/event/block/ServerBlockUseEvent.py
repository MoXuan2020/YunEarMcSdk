# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerBlockUseEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerBlockUseEvent, self).__init__(callback)
        self.playerId = None
        self.blockName = None
        self.aux = None
        self.cancel = None
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.itemDict = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.blockName = args.get("blockName")
        self.aux = args.get("aux")
        self.cancel = args.get("cancel")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.face = args.get("face")
        self.itemDict = args.get("itemDict")
        self.dimensionId = args.get("dimensionId")
