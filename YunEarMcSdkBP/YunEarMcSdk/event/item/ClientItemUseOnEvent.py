# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientItemUseOnEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientItemUseOnEvent, self).__init__(callback)
        self.entityId_ = None
        self.itemDict_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.blockName_ = None
        self.blockAuxValue_ = None
        self.face_ = None
        self.clickX_ = None
        self.clickY_ = None
        self.clickZ_ = None
        self.ret_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.itemDict_ = args["itemDict"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.blockName_ = args["blockName"]
        self.blockAuxValue_ = args["blockAuxValue"]
        self.face_ = args["face"]
        self.clickX_ = args["clickX"]
        self.clickY_ = args["clickY"]
        self.clickZ_ = args["clickZ"]
        self.ret_ = args["ret"]
