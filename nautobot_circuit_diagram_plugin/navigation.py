"""Navigation Items to add to Nautobot for diagram."""
from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab
from nautobot.extras.plugins import PluginMenuItem

menu_items = (
    NavMenuTab(
        name="Circuits",
        groups=(
            NavMenuGroup(
                name="Circuits",
                weight=150,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_circuit_diagram_plugin:world-map-view",
                        name="Diagram",
                        permissions=["circuits.view_circuits"],
                    ),
                ),
            ),
        ),
    ),
)
