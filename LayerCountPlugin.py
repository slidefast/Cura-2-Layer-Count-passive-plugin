import os
import sys
import os.path
import json
import re
import collections

from UM.Message import Message
from UM.Logger import Logger

from UM.Application import Application
from UM.Preferences import Preferences
from UM.Extension import Extension
from UM.PluginRegistry import PluginRegistry


from UM.Mesh.MeshWriter import MeshWriter
from UM.FileHandler.WriteFileJob import WriteFileJob
from cura.Settings.ExtruderManager import ExtruderManager
from UM.Settings.ContainerStack import ContainerStack
from UM.Settings.InstanceContainer import InstanceContainer
from UM.Settings.DefinitionContainer import DefinitionContainer
from UM.Settings.ContainerRegistry import ContainerRegistry
from UM.OutputDevice.OutputDevicePlugin import OutputDevicePlugin
from UM.OutputDevice.OutputDevice import OutputDevice
from UM.OutputDevice import OutputDeviceError


from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")


class LayerCountExtension(OutputDevicePlugin):
    def __init__(self):
        super().__init__()
		
	         
    @property	
    def start(self,stream, nodes,MeshWriter,OutputMode,TextMode):

			
        count = "-"
        for index, layer in enumerate(data):
            new_layer = ""
            lines = layer.split("\n")
            for line in lines:
                if line:
                    new_layer += line + "\n"
                    if line.startswith(";LAYER_COUNT:"):
                        count = line[13:].rstrip()
                    if line.startswith(";LAYER:"):
                        this_layer = int(line[7:].rstrip()) + 1
                        new_layer += "M117 Layer {0}/{1}...\n".format(this_layer, count)
            data[index] = new_layer
        return data

   

    