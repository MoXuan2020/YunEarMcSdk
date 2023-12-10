# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerBlockUseEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerBlockUseEvent, self).__init__(callback)
        self.playerId_ = None
        self.blockName_ = None
        self.aux_ = None
        self.cancel_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.face_ = None
        self.itemDict_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.blockName_ = args.get("blockName")
        self.aux_ = args.get("aux")
        self.cancel_ = args.get("cancel")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.face_ = args.get("face")
        self.itemDict_ = args.get("itemDict")
        self.dimensionId_ = args.get("dimensionId")
