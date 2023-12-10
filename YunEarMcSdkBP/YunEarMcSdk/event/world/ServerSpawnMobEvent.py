# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerSpawnMobEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerSpawnMobEvent, self).__init__(callback)
        self.entityId = None
        self.identifier = None
        self.type = None
        self.baby = None
        self.x = None
        self.y = None
        self.z = None
        self.dimensionId = None
        self.realIdentifier = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.identifier = args.get("identifier")
        self.type = args.get("type")
        self.baby = args.get("baby")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.dimensionId = args.get("dimensionId")
        self.realIdentifier = args.get("realIdentifier")
        self.cancel = args.get("cancel")
