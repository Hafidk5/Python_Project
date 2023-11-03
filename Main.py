import sys
from Server import (
    info_servers,
    opslaan_server,
    toevoeg_server,
    verwijder_server,
    lijst_servers,
)

from Server_check import server_check, generate_html_rapport


if __name__ == "__main__":
    mode = "check" if len(sys.argv) > 1 and sys.argv[1] == "check" else "management"

    if mode == "management":
        # Management modus
        servers = info_servers()

        while True:
            print("Beschikbare acties:")
            print("1. Voeg een server toe")
            print("2. Verwijder een server")
            print("3. Toon de lijst met servers")
            print("4. Sla de huidige serverlijst op en verlaat het programma")

            keuze = input("Selecteer een actie (1/2/3/4): ")

            if keuze == "1":
                nieuw_server = input("Voer de naam of IP van de server in: ")
                toevoeg_server(nieuw_server)
                print(f"{nieuw_server} is toegevoegd.")
            elif keuze == "2":
                target_server = input("Voer de naam of IP van de te verwijderen server in: ")
                verwijder_server(target_server)
                print(f"{target_server} is verwijderd.")
            elif keuze == "3":
                print("Huidige lijst met servers:")
                lijst_servers()
            elif keuze == "4":
                opslaan_server(servers, "servers.json")
                break
            else:
                print("Ongeldige keuze. Probeer opnieuw.")

    elif mode == "check":
        # Check modus
        servers = info_servers()
        if not servers:
            print(
                "Voeg servers toe in de management modus voordat je de checks uitvoert."
            )
        else:
            results = server_check(servers)
            generate_html_rapport(results)
            print("Serverchecks voltooid. Rapport gegenereerd als 'rapport.html'.")
