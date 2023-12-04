# -*- coding: utf-8 -*-

from mod.common.mod import Mod

from YunEarMcSdk.config import Config


@Mod.Binding(Config.SdkName, Config.SdkVersion)
class YunEarMcSdk(object):

    def __init__(self, modCls=None):
        self.modCls = modCls
        self.mod = None
        self.server = None
        self.client = None

    def __call__(self):
        if self.mod is None:
            self.mod = self.modCls()
            import mod.server.extraServerApi as serverApi
            self.server = serverApi.RegisterSystem(
                Config.SdkName,
                Config.SdkServerName,
                Config.SdkServerClsPath
            )
            import mod.client.extraClientApi as clientApi
            self.client = clientApi.RegisterSystem(
                Config.SdkName,
                Config.SdkClientName,
                Config.SdkClientClsPath
            )
            for attr in self.modCls.__dict__:
                from YunEarMcSdk.event.ServerEvent import ServerEvent
                if isinstance(self.modCls.__dict__[attr], ServerEvent):
                    self.modCls.__dict__[attr].InitMod(self.mod)
                    self.server.ListenForEvent(
                        serverApi.GetEngineNamespace(),
                        serverApi.GetEngineSystemName(),
                        self.modCls.__dict__[attr].__class__.__name__,
                        self.mod,
                        self.modCls.__dict__[attr].callback
                    )
                from YunEarMcSdk.event.ClientEvent import ClientEvent
                if isinstance(self.modCls.__dict__[attr], ClientEvent):
                    self.modCls.__dict__[attr].InitMod(self.mod)
                    self.client.ListenForEvent(
                        clientApi.GetEngineNamespace(),
                        clientApi.GetEngineSystemName(),
                        self.modCls.__dict__[attr].__class__.__name__,
                        self.mod,
                        self.modCls.__dict__[attr].callback
                    )
