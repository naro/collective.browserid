from zope.component.interfaces import IObjectEvent


class IBrowserIDUserAuhenticatedEvent(IObjectEvent):
    """ User has been authenticated using BrowserID """