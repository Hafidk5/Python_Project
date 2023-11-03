import subprocess
import os
import json


def server_check(servers):
    resultaat = {}

    for server in servers:
        online = ping_server(server)
        resultaat[server] = "Online" if online else "Offline"

    opslaan_check(resultaat)

    return resultaat


def ping_server(server):
    try:
        if os.name == "nt":
            # Het is voor windows, indien je apple hebt moet je nt vervangen door posix
            subprocess.check_output(
                ["ping", "-n", "3", server], stderr=subprocess.STDOUT
            )
            return True
    except subprocess.CalledProcessError:
        return False


def opslaan_check(resultaat):
    with open("server_checks.json", "w") as check_file:
        json.dump(resultaat, check_file)


def generate_html_rapport(resultaat):
    with open("template.html", "r") as template_file:
        template = template_file.read()

    table_content = ""
    for server, status in resultaat.items():
        table_content += f"<tr class=\"{'online' if status == 'Online' else 'offline'}\">"
        table_content += f"<td>{server}</td>"
        table_content += f"<td>{status}</td>"
        table_content += "</tr>"

    rapport = template.replace("<!-- SERVER_ROWS -->", table_content)

    with open("rapport.html", "w") as rapport_file:
        rapport_file.write(rapport)

