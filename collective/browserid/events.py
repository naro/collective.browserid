from zope.interface import implements
from zope.component.interfaces import ObjectEvent
from collective.browserid.interfaces import IBrowserIDUserAuhenticatedEvent


class BrowserIDUserAuhenticatedEvent(ObjectEvent):
    """ User has been authenticated using BrowserID """

    implements(IBrowserIDUserAuhenticatedEvent)