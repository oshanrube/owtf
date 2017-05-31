from framework.utils import OWTFLogger
from framework.dependency_management.dependency_resolver import ServiceLocator


DESCRIPTION = "robots.txt analysis through third party sites"


def run(PluginInfo):
    plugin_helper = ServiceLocator.get_component("plugin_helper")
    resource = ServiceLocator.get_component("resource")
    Content = plugin_helper.RequestLinkList('Passive Analysis Results', resource.GetResources('PassiveRobotsAnalysisHTTPRequests'), PluginInfo)
    Content += plugin_helper.ResourceLinkList('Online Resources', resource.GetResources('PassiveRobotsAnalysisLinks'))
    # Try to retrieve the robots.txt file from all defined resources
    Count = 0
    for Name, Resource in resource.GetResources('PassiveRobots'):
        URL = Resource  # Just for clarity
        # Preparing link chunks for disallowed entries
        LinkStart, LinkFinish = URL.split('/robots.txt')
        LinkStart = LinkStart.strip()
        LinkFinish = LinkFinish.strip()
        # Use the cache if possible for speed
        Transaction = ServiceLocator.get_component("requester").GetTransaction(True, URL)
        if Transaction is not None and Transaction.Found:
            Content += plugin_helper.ProcessRobots(PluginInfo, Transaction.GetRawResponseBody(), LinkStart, LinkFinish,
                                                   'robots%s.txt' % str(Count))
            Count += 1
        else:  # Not found or unknown request error
            Message = "Could not be retrieved using resource: %s" % Resource
            OWTFLogger.log(Message)
        Content += plugin_helper.TransactionTableForURLList(True, [URL])
    return Content
