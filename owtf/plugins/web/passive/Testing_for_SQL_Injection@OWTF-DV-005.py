"""
PASSIVE Plugin for Testing for SQL Injection (OWASP-DV-005)
https://www.owasp.org/index.php/Testing_for_SQL_Injection_%28OWASP-DV-005%29
"""

from framework.dependency_management.dependency_resolver import ServiceLocator


DESCRIPTION = "Google Hacking for SQLi"


def run(PluginInfo):
    resource = ServiceLocator.get_component("resource").GetResources('PassiveSQLInjectionLnk')
    Content = ServiceLocator.get_component("plugin_helper").ResourceLinkList('Online Resources', resource)
    return Content
