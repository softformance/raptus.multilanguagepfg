from raptus.multilanguagepfg import LOG

from Products.PloneFormGen.content.form import FormFolder

_getFieldObjects_old = FormFolder._getFieldObjects
def _getFieldObjects(self, objTypes=None, includeFSMarkers=False):
    fields = _getFieldObjects_old(self, objTypes, includeFSMarkers)

    for field in fields:
        field.setTitle(field.Title())
        field.setDescription(field.Description())
        if hasattr(field,'setFgDefault'):
            field.setFgDefault(field.getFgDefault())
    
    return fields
FormFolder._getFieldObjects = _getFieldObjects
LOG.info("Products.PloneFormGen.content.form.FormFolder._getFieldObjects patched")