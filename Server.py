import json
import os


def info_servers():
    file_naam = "servers.json"

    if os.path.exists(file_naam):
        try:
            with open(file_naam, "r") as file:
                servers = json.load(file)
        except FileNotFoundError:
            servers = []
    else:
        servers = []

    return servers


def opslaan_server(servers):
    try:
        with open("servers.json", "w") as file:
            json.dump(servers, file)
    except FileNotFoundError:
        print("Fout: servers.json kon niet worden gevonden of geopend.")


def toevoeg_server(server_naam):
    servers = info_servers()
    servers.append(server_naam)
    opslaan_server(servers)
    print(f"{server_naam} toegevoegd aan de lijst.")


def verwijder_server(server_naam):
    servers = info_servers()
    if server_naam in servers:
        servers.remove(server_naam)
        opslaan_server(servers)
        print(f"{server_naam} verwijderd uit de lijst.")
    else:
        print(f"{server_naam} niet gevonden in de lijst.")


def lijst_servers():
    servers = info_servers()
    print("Lijst van servers: ")
    for server in servers:
        print(server)
