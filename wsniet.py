#!/usr/bin/env python3

import subprocess
import speedtest
import re
from colorama import Fore, Style, init
from tqdm import tqdm
import time
import os

# Initialize colorama for cross-platform color support
init(autoreset=True)

def welcome_message():
    """
    Display a stylish welcome message.
    """
    print(Fore.CYAN + Style.BRIGHT + r"""
  __          _______  _   _ _____ ______ _______ 
  \ \        / / ____|| \ | |_   _|  ____|__   __| 
   \ \  /\  / / (___  |  \| | | | | |__     | |   
    \ \/  \/ / \___ \ | . ` | | | |  __|    | |   
     \  /\  /  ____) || |\  |_| |_| |____   | |   
      \/  \/  |_____/ |_| \_|_____|______|  |_|   
""")
    print(Fore.GREEN + "Welcome to the Wi-Fi Speed Test Tool (WSNIET)!")
    print(Fore.YELLOW + "Powered by Python\n")

def get_wifi_details():
    """
    Get Wi-Fi details such as link speed and signal quality using netsh (Windows).
    """
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
        wifi_details = {}
        
        # Parse the output for Link Speed (Wi-Fi speed) and Signal Level
        bitrate_match = re.search(r"Link Speed\s*:\s*(\d+ \S+)", output)
        signal_match = re.search(r"Signal\s*:\s*(\d+)", output)
        
        if bitrate_match:
            wifi_details['bit_rate'] = bitrate_match.group(1)
        else:
            wifi_details['bit_rate'] = "Unknown"
        
        if signal_match:
            wifi_details['signal_level'] = f"{signal_match.group(1)}%"
        else:
            wifi_details['signal_level'] = "Unknown"
        
        return wifi_details
    except Exception as e:
        return {"error": f"Error getting Wi-Fi details: {e}"}

def get_speedtest_results():
    """
    Get download speed, upload speed, and ping using speedtest-cli.
    """
    try:
        st = speedtest.Speedtest()
        
        # Simulating a progress bar during server finding
        for _ in tqdm(range(100), desc="Finding best server"):
            time.sleep(0.02)
        st.get_best_server()
        
        # Simulating a progress bar during download/upload test
        for _ in tqdm(range(100), desc="Testing download speed"):
            time.sleep(0.02)
        download_speed = st.download() / 1e6  # Convert to Mbps
        
        for _ in tqdm(range(100), desc="Testing upload speed"):
            time.sleep(0.02)
        upload_speed = st.upload() / 1e6  # Convert to Mbps
        
        ping = st.results.ping  # Latency in ms
        
        return {
            'download_speed': round(download_speed, 2),
            'upload_speed': round(upload_speed, 2),
            'ping': round(ping, 2)
        }
    except Exception as e:
        return {"error": f"Error running speed test: {e}"}

def display_results(wifi_details, speed_results):
    """
    Display results in a clean format.
    """
    print("\n" + Fore.CYAN + "="*30)
    print(Fore.YELLOW + "=== Wi-Fi Details ===")
    if "error" in wifi_details:
        print(Fore.RED + wifi_details["error"])
    else:
        print(Fore.GREEN + f"Wi-Fi Bit Rate: {wifi_details.get('bit_rate', 'N/A')}")
        print(Fore.GREEN + f"Signal Level: {wifi_details.get('signal_level', 'N/A')}")

    print(Fore.CYAN + "="*30)
    print(Fore.YELLOW + "=== Internet Speed Test ===")
    if "error" in speed_results:
        print(Fore.RED + speed_results["error"])
    else:
        print(Fore.GREEN + f"Download Speed: {speed_results.get('download_speed', 0)} Mbps")
        print(Fore.GREEN + f"Upload Speed: {speed_results.get('upload_speed', 0)} Mbps")
        print(Fore.GREEN + f"Ping (Jitter): {speed_results.get('ping', 0)} ms")
    print(Fore.CYAN + "="*30)

def check_and_install():
    """
    Ensure the script is executable and moved to /usr/local/bin as 'wsniet'.
    This is specific to Windows and won't affect other systems.
    """
    script_path = os.path.realpath(__file__)
    script_name = "wsniet"

    # Ensure the script is executable
    try:
        subprocess.run(["chmod", "+x", script_path], check=True)
        print(Fore.GREEN + f"Tool is ready to run: {script_name}")
    except Exception as e:
        print(Fore.RED + f"Error during setup: {e}")

if __name__ == "__main__":
    check_and_install()  # Check if the script is set up
    welcome_message()  # Display welcome message
    
    wifi_details = get_wifi_details()  # Get Wi-Fi details
    speed_results = get_speedtest_results()  # Run speed test
    
    display_results(wifi_details, speed_results)  # Display the results
