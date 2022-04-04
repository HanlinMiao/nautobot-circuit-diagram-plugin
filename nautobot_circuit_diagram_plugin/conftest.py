from nautobot.dcim.models import Site

def create_site(name="foooobar"):
    """Creates a Site to be used with tests."""
    site, _ = Site.objects.get_or_create(name="Site 1", slug="site-1", latitude=40.7831, longitude=73.9712, physical_address="Manhattan NY, USA")
    return site