# Disable Floating IPs
from openstack_dashboard.dashboards.project.access_and_security import tabs
from openstack_dashboard.dashboards.project.instances import tables
import horizon

NO = lambda *x: False

tabs.FloatingIPsTab.allowed = NO
tabs.APIAccessTab.allowed = NO
tables.AssociateIP.allowed = NO
tables.SimpleAssociateIP.allowed = NO
tables.SimpleDisassociateIP.allowed = NO

project_dashboard = horizon.get_dashboard("project")

# Completely remove panel Network->Routers
routers_panel = project_dashboard.get_panel("routers")
project_dashboard.unregister(routers_panel.__class__)

# Completely remove panel Network->Networks
networks_panel = project_dashboard.get_panel("networks")
project_dashboard.unregister(networks_panel.__class__)    # Disable Floating IPs

# Completely remove panel Network->Network Topology
topology_panel = project_dashboard.get_panel("network_topology")
project_dashboard.unregister(topology_panel.__class__)

# Remove "Volume Consistency Groups" tab
from openstack_dashboard.dashboards.project.volumes import tabs
tabs.CGroupsTab.allowed = NO
