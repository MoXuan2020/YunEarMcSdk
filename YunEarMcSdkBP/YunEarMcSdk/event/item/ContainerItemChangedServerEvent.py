# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ContainerItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ContainerItemChangedServerEvent, self).__init__(callback)
        self.pos = None
        self.containerType = None
        self.slot = None
        self.dimensionId = None
        self.oldItemDict = None
        self.newItemDict = None

    def CreateFromArgs(self, args):
        self.pos = args.get("pos")
        self.containerType = args.get("containerType")
        self.slot = args.get("slot")
        self.dimensionId = args.get("dimensionId")
        self.oldItemDict = args.get("oldItemDict")
        self.newItemDict = args.get("newItemDict")
