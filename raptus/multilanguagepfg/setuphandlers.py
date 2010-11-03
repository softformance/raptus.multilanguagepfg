from raptus.multilanguagepfg import extender

from Products.CMFCore.utils import getToolByName

extenders = []

indexes = ('SearchableText', 'Subject', 'Title', 'Description', 'sortable_title',)

def reindex(portal):
    catalog = getToolByName(portal, 'portal_catalog')
    for index in indexes:
        catalog.reindexIndex(index, portal.REQUEST)

def install(context):

    if context.readDataFile('raptus.multilanguagepfg_install.txt') is None:
        return
    
    portal = context.getSite()
    quickinstaller = getToolByName(portal, 'portal_quickinstaller')

    sm = portal.getSiteManager()
    for extender in extenders:
        sm.registerAdapter(modifier, name='MultilanguagePFG%s' % extender.__name__)
        
    reindex(portal)
    
def uninstall(context):
    if context.readDataFile('raptus.multilanguagepfg_install.txt') is None and \
       context.readDataFile('raptus.multilanguagepfg_uninstall.txt') is None:
        return
    
    portal = context.getSite()
    sm = portal.getSiteManager()
    for extender in extenders:
        sm.unregisterAdapter(extender, name='MultilanguagePFG%s' % extener.__name__)
        
    reindex(portal)
    