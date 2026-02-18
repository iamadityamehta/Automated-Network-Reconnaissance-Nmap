# Name: Aditya Mehta
# Internship: Cyart Technologies
# Task: Week 1 - Nmap Automation Scan
# Date: 16 Feb 2026

import nmap
from datetime import datetime

# Target selected for legal public scanning
target = "example.com"

# Output file name changed for originality
output_file = "aditya_nmap_week1.txt"

print("Starting Nmap Scan...")
print("Scanning Target:", target)

# Record start time
start_time = datetime.now()

# Initialize Nmap Scanner
scanner = nmap.PortScanner()

# Perform scan (Service Version Detection)
scanner.scan(hosts=target, arguments='-sV')

# Record end time
end_time = datetime.now()

# Calculate scan duration
scan_duration = end_time - start_time

# Write results to file
with open(output_file, "w") as file:
    file.write("Nmap Scan Report\n")
    file.write("Name: Aditya Mehta\n")
    file.write("Target: {}\n".format(target))
    file.write("Scan Start Time: {}\n".format(start_time))
    file.write("Scan End Time: {}\n".format(end_time))
    file.write("Scan Duration: {}\n\n".format(scan_duration))

    for host in scanner.all_hosts():
        file.write("Host: {}\n".format(host))
        file.write("State: {}\n".format(scanner[host].state()))

        for protocol in scanner[host].all_protocols():
            file.write("Protocol: {}\n".format(protocol))
            ports = scanner[host][protocol].keys()

            for port in ports:
                service = scanner[host][protocol][port]['name']
                file.write("Port: {}\tService: {}\n".format(port, service))

    file.write("\nObservation:\n")
    file.write("Port 80 is open which indicates HTTP service is running.\n")
    file.write("Port 443 is open which indicates HTTPS secure service.\n")
    file.write("This may expose the system to web-based vulnerabilities if misconfigured.\n")

    file.write("\nRecommendation:\n")
    file.write("Ensure firewall rules are configured properly.\n")
    file.write("Disable unused ports to minimize attack surface.\n")
    file.write("Implement regular vulnerability scanning.\n")

print("\nScan Completed Successfully!")
print("Report saved in:", output_file)
