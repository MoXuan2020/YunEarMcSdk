# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ContainerItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ContainerItemChangedServerEvent, self).__init__(callback)
        self.pos_ = None
        self.containerType_ = None
        self.slot_ = None
        self.dimensionId_ = None
        self.oldItemDict_ = None
        self.newItemDict_ = None

    def CreateFromArgs(self, args):
        self.pos_ = args.get("pos")
        self.containerType_ = args.get("containerType")
        self.slot_ = args.get("slot")
        self.dimensionId_ = args.get("dimensionId")
        self.oldItemDict_ = args.get("oldItemDict")
        self.newItemDict_ = args.get("newItemDict")
