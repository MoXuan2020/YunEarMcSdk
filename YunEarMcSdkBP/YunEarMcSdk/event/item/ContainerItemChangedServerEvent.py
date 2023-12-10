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
        self.pos_ = args["pos"]
        self.containerType_ = args["containerType"]
        self.slot_ = args["slot"]
        self.dimensionId_ = args["dimensionId"]
        self.oldItemDict_ = args["oldItemDict"]
        self.newItemDict_ = args["newItemDict"]
