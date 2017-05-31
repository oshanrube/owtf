"""
PASSIVE Plugin for Testing for Cross site flashing (OWASP-DV-004)
"""

from framework.dependency_management.dependency_resolver import ServiceLocator


DESCRIPTION = "Google Hacking for Cross Site Flashing"


def run(PluginInfo):
    resource = ServiceLocator.get_component("resource").GetResources('PassiveCrossSiteFlashingLnk')
    Content = ServiceLocator.get_component("plugin_helper").ResourceLinkList('Online Resources', resource)
    return Content
