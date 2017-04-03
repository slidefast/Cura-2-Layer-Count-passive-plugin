from . import LayerCountPlugin

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "type": "extension",
        "plugin": {
            "name": catalog.i18nc("@label", "Layer Count"),
            "author": "Slidefast",
            "description": catalog.i18nc("@info:whatsthis", "3D Printer LCD Display Layer Count."),
            "version": "1.0",
            "api": 3
        }
    }

def register(app):
    return {"extension": LayerCountPlugin.LayerCountPlugin()}
