from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender

from raptus.multilanguagefields import widgets
from raptus.multilanguageplone.extender import fields
from raptus.multilanguageplone.extender.base import DefaultExtender

from Products.ATContentTypes.configuration import zconf
from Products.Archetypes.Field import TextField, LinesField, StringField
from Products.Archetypes.atapi import AnnotationStorage

from Products.PloneFormGen.content.fields import FGSelectionField
from Products.PloneFormGen import PloneFormGenMessageFactory as _


