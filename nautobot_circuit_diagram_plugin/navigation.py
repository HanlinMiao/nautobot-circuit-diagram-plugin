"""Navigation Items to add to Nautobot for diagram."""
from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab
from nautobot.extras.plugins import PluginMenuItem

menu_items = (
    # PluginMenuItem(
    #     link='plugins:nautobot_circuit_diagram_plugin:world-map-view',  # A reverse compatible link to follow.
    #     link_text = 'global-diagram',  # Text to display to user.
    #     permissions = [],  # Optional: List of permissions required to display this link.
    #     # buttons = (  # Optional: Iterable of PluginMenuButton instances to display.
    #     #     PluginMenuButton(
    #     #         'plugins:diagram:model',  # A reverse compatible link to follow.
    #     #         'Sample Text',  # Text to display to user.
    #     #         'mdi mdi-help-circle',  # Button icon CSS Classes (Currently supports Material Design Icons.)
    #     #         ButtonColorChoices.BLUE,  # Optional: Color for the button.,
    #     #         permissions = []  # Optional: List of permissions required to display this button.
    #     #     )
    #     # )
    # ),

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
