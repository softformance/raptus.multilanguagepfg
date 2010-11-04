from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender

from raptus.multilanguagefields import widgets
from raptus.multilanguageplone.extender import fields
from raptus.multilanguageplone.extender.base import DefaultExtender

from Products.ATContentTypes.configuration import zconf
from Products.Archetypes.Field import TextField, LinesField, StringField

from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen import PloneFormGenMessageFactory as _


class BaseFormFieldExtender(DefaultExtender):
    
    adapts(BaseFormField)
    
    defaultFields = DefaultExtender.fields
    
    textField = fields.TextField('fgDefault',
        searchable=0,
        required=0,
        widget=widgets.TextAreaWidget(label=_(u'label_fgtextdefault_text', default=u'Default'),
            description=_(u'help_fgtextdefault_text', default=u"""
                The text the field should contain when the form is first displayed.
                Note that this may be overridden dynamically.
            """),
        ),
    )
    
    linesField = fields.LinesField('fgDefault',
        searchable=0,
        required=0,
        widget=widgets.LinesWidget(label=_(u'label_fglinesdefault_text', default=u'Default'),
            description=_(u'help_fglinesdefault_text', default=u"""
                The values the field should contain when the form is first displayed.
                Use one value per line.
                Note that this may be overridden dynamically.
            """),
        ),
    )
        
    stringField = fields.StringField('fgDefault',
        searchable=0,
        required=0,
        widget=widgets.StringWidget(label=_(u'label_fgdefault_text', default=u'Default'),
        description=_(u'help_fgdefault_text', default=u"""
            The value the field should contain when the form is first displayed.
            Note that this may be overridden dynamically.
        """),
        ),
    )

    
    def getFields(self):
        
        fgDefault = self.context.schema.get('fgDefault')
        
        if isinstance(fgDefault,TextField):
            self.defaultFields.append(self.textField)
        if isinstance(fgDefault,LinesField):
            self.defaultFields.append(self.linesField)
        if isinstance(fgDefault,StringField):
            self.defaultFields.append(self.stringField)
        return self.defaultFields