from framework.dependency_management.dependency_resolver import ServiceLocator


DESCRIPTION = "Cross Site Flashing Plugin to assist manual testing"


def run(PluginInfo):
    resource = ServiceLocator.get_component("resource").GetResources('ExternalCrossSiteFlashing')
    Content = ServiceLocator.get_component("plugin_helper").ResourceLinkList('Online Resources', resource)
    return Content
