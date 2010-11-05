from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender

from raptus.multilanguagefields import widgets
from raptus.multilanguageplone.extender import fields
from raptus.multilanguageplone.extender.base import DefaultExtender

from Products.ATContentTypes.configuration import zconf
from Products.Archetypes.Field import TextField, LinesField, StringField
from Products.Archetypes.atapi import AnnotationStorage

from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen import PloneFormGenMessageFactory as _


class BaseFormFieldExtender(DefaultExtender):
    
    adapts(BaseFormField)
    
    textField = fields.TextField('fgDefault',
        searchable=0,
        required=0,
        storage=AnnotationStorage(migrate=True),
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
        storage=AnnotationStorage(migrate=True),
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
        storage=AnnotationStorage(migrate=True),
        widget=widgets.StringWidget(label=_(u'label_fgdefault_text', default=u'Default'),
        description=_(u'help_fgdefault_text', default=u"""
            The value the field should contain when the form is first displayed.
            Note that this may be overridden dynamically.
        """),
        ),
    )
    
    fgVocabulary = fields.LinesField('fgVocabulary',
        searchable=0,
        required=0,
        accessor='fgTVocabulary',
        storage=AnnotationStorage(migrate=True),
        widget=widgets.LinesWidget(
            label=_(u'label_fgvocabulary_text',
            default=u'Options'),
            description=_(u'help_fgvocabulary_text', default=u"""
                Use one line per option.
                Note that this may be overridden dynamically.
                [Note, you may optionally use a "value|label" format.]
            """),
        ),
    )
    
    # Todo --> attache theses fields
    fields.TextField('fgDefault',
        searchable=0,
        required=0,
        validators = ('isTidyHtmlWithCleanup',),
        default_content_type = 'text/html',
        default_output_type = 'text/x-html-safe',
        allowable_content_types = zconf.ATDocument.allowed_content_types,
        widget=widgets.RichWidget(label=_(u'label_fgtextdefault_text', default=u'Default'),
            description=_(u'help_fgtextdefault_text', default=u"""
                The text the field should contain when the form is first displayed.
                Note that this may be overridden dynamically.
            """),
        allow_file_upload = False,
        ),
    )

    fields.TextField('fgDefault',
        searchable=0,
        required=0,
        widget=widgets.TextAreaWidget(label=_(u'label_fgtextdefault_text', default=u'Default'),
            description=_(u'help_fgtextdefault_text', default=u"""
                The text the field should contain when the form is first displayed.
                Note that this may be overridden dynamically.
            """),
        ),
    )

    def getFields(self):
        defaultFields = DefaultExtender.fields + []#make a copy
        fgDefault = self.context.schema.get('fgDefault')
        
        if isinstance(fgDefault,TextField):
            defaultFields.append(self.textField)
        if isinstance(fgDefault,LinesField):
            defaultFields.append(self.linesField)
        if isinstance(fgDefault,StringField):
            defaultFields.append(self.stringField)
            
        if self.context.schema.get('fgVocabulary'):
            defaultFields.append(self.fgVocabulary)

        return defaultFields