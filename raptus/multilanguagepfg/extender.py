from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender

from raptus.multilanguagefields import widgets
from Products.PloneFormGen.content.form import FormFolder


class FormFolderExtender(object):
    implements(ISchemaExtender)
    adapts(FormFolder)
    
    fields = [
              
              
              
              
              ]
    
    def __init__(self, context):
         self.context = context

    def getFields(self):
        return self.fields