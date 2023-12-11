# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod

from YunEarMcSdk.config import Config
from YunEarMcSdk.event.ClientEvent import ClientEvent
from YunEarMcSdk.event.ServerEvent import ServerEvent


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
            self.server = serverApi.GetSystem(
                self.modCls.__module__,
                self.modCls.__name__
            )
            if self.server is None:
                self.server = serverApi.RegisterSystem(
                    self.modCls.__module__,
                    self.modCls.__name__,
                    Config.SdkServerClsPath
                )
                for attr in self.modCls.__dict__:
                    event = self.modCls.__dict__[attr]
                    if isinstance(event, ServerEvent):
                        event.BindMod(self.mod)
                        self.server.ListenForEvent(
                            serverApi.GetEngineNamespace(),
                            serverApi.GetEngineSystemName(),
                            event.__class__.__name__,
                            self.mod,
                            event.callback
                        )
            self.client = clientApi.RegisterSystem(
                self.modCls.__module__,
                self.modCls.__name__,
                Config.SdkClientClsPath
            )
            for attr in self.modCls.__dict__:
                event = self.modCls.__dict__[attr]
                if isinstance(event, ClientEvent):
                    event.BindMod(self.mod)
                    self.client.ListenForEvent(
                        clientApi.GetEngineNamespace(),
                        clientApi.GetEngineSystemName(),
                        event.__class__.__name__,
                        self.mod,
                        event.callback
                    )
