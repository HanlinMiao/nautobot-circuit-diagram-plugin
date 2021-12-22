"""Views for diagram."""
import os
from django.shortcuts import render
from nautobot.dcim.models import Site
from nautobot.dcim.choices import SiteStatusChoices
from nautobot.circuits.models import CircuitTermination, Circuit
from nautobot.circuits.choices import CircuitStatusChoices
from django.conf import settings
from django.http import JsonResponse
import random
import decimal

def world_map_view(request):
    GOOGLE_MAP_API_KEY = os.environ["GOOGLE_MAP_API_KEY"]
    return render(request, "nautobot_circuit_diagram_plugin/organization_map.html", {"key": GOOGLE_MAP_API_KEY})

def load_site_coordinates(request):
    if request.method == 'GET':
        sites = Site.objects.exclude(latitude=None).exclude(longitude=None)
        response = []
        coordinates = []
        circuit_set = []
        for site in sites:
            data = {}
            data["name"] = site.name
            data["address"] = site.physical_address if site.physical_address else "N/A"
            data["lat"] = site.latitude
            data["lng"] = site.longitude
            data["status"] = SiteStatusChoices.MAP_CSS_CLASSES[site.get_status_display()]
            data["circuits"] = {}
            circuit_terms = CircuitTermination.objects.filter(site=site)
            circuits = Circuit.objects.filter(terminations__in=circuit_terms)
            for circuit in circuits:
                if str(circuit) not in circuit_set:
                    circuit_set.append(str(circuit))
                data["circuits"][str(circuit)] = {}
                data["circuits"][str(circuit)]["status"] = circuit.get_status_display()
                data["circuits"][str(circuit)]["status_color"] = CircuitStatusChoices.MAP_CSS_CLASSES[circuit.get_status_display()]
                data["circuits"][str(circuit)]["A"] = {}
                data["circuits"][str(circuit)]["Z"] = {}
                if not circuit.termination_a:
                    data["circuits"][str(circuit)]["A"] = None
                else:
                    lat = circuit._get_termination("A").site.latitude
                    lng = circuit._get_termination("A").site.longitude
                    if (lat, lng) not in coordinates:
                        data["circuits"][str(circuit)]["A"]["lat"] = lat
                        data["circuits"][str(circuit)]["A"]["lng"] = lng
                    else:
                        count = 0
                        while (lat, lng) in coordinates:
                            if count % 2 == 0:
                                lat += decimal.Decimal(str(random.uniform(-1, 1)))
                            else:
                                lng += decimal.Decimal(str(random.uniform(-1, 1)))
                            count += 1
                        data["circuits"][str(circuit)]["A"]["lat"] = lat
                        data["circuits"][str(circuit)]["A"]["lng"] = lng
                    coordinates.append((lat, lng))

                if not circuit.termination_z:
                    data["circuits"][str(circuit)]["Z"] = None
                else:
                    lat = circuit._get_termination("Z").site.latitude
                    lng = circuit._get_termination("Z").site.longitude
                    if (lat, lng) not in coordinates:
                        data["circuits"][str(circuit)]["Z"]["lat"] = lat
                        data["circuits"][str(circuit)]["Z"]["lng"] = lng
                    else:
                        count = 0
                        while (lat, lng) in coordinates:
                            if count % 2 == 0:
                                lat += decimal.Decimal(str(random.uniform(-1, 1)))
                            else:
                                lng += decimal.Decimal(str(random.uniform(-1, 1)))
                            count += 1
                        data["circuits"][str(circuit)]["Z"]["lat"] = lat
                        data["circuits"][str(circuit)]["Z"]["lng"] = lng
                    coordinates.append((lat, lng))
            response.append(data)
        response.append(circuit_set)

        return JsonResponse(response, safe=False)