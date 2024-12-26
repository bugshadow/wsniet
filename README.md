# WSNIET (Wi-Fi Speed and Network Information Extraction Tool)

## Description
WSNIET is a powerful Python-based Wi-Fi speed testing tool that provides detailed information about your wireless connection and internet performance. The tool features a colorful command-line interface with real-time progress indicators and comprehensive network statistics.

## Features
- Beautiful ASCII art welcome banner
- Real-time Wi-Fi connection details
- Internet speed testing (Download/Upload speeds)
- Latency (ping) measurement
- Signal strength monitoring
- Progress bars for better user experience
- Color-coded output for better readability

## Prerequisites
- Python 3.x
- Windows OS (for Wi-Fi details feature)
- Administrative privileges (for network access)

## Installation

### Required Python packages
```bash
pip install -r requirements.txt
```

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/bugshadow/wsniet.git
```

2. Navigate to the directory:
```bash
cd wsniet
```

3. Make the script executable:
```bash
chmod +x wsniet.py
```

4. Install system-wide (optional):
```bash
sudo cp wsniet.py /usr/local/bin/wsniet
```

## Usage
You can run the tool in two ways:

1. Directly from the script:
```bash
python3 wsniet.py
```

2. If installed system-wide:
```bash
wsniet
```

## Output Example
```
  __          _______  _   _ _____ ______ _______ 
  \ \        / / ____|| \ | |_   _|  ____|__   __| 
   \ \  /\  / / (___  |  \| | | | | |__     | |   
    \ \/  \/ / \___ \ | . ` | | | |  __|    | |   
     \  /\  /  ____) || |\  |_| |_| |____   | |   
      \/  \/  |_____/ |_| \_|_____|______|  |_|   

==============================
=== Wi-Fi Details ===
Wi-Fi Bit Rate: 300 Mbps
Signal Level: 85%
==============================
=== Internet Speed Test ===
Download Speed: 50.25 Mbps
Upload Speed: 25.10 Mbps
Ping (Jitter): 15.5 ms
==============================
```

## Features Explained
- **Wi-Fi Details**: Shows your current connection speed and signal strength
- **Download Speed**: Measures your download bandwidth in Mbps
- **Upload Speed**: Measures your upload bandwidth in Mbps
- **Ping**: Measures the latency of your connection in milliseconds

## Limitations
- The Wi-Fi details feature is currently optimized for Windows systems
- Requires administrative privileges for network speed testing
- Speed test results may vary based on server location and network conditions

## Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


## Author
Omar Bouhaddach

## Acknowledgments
- Speedtest-cli library
- Colorama for cross-platform colored output
- TQDM for progress bars
