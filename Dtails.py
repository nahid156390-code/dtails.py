import time
import sys
import os

def mehdi_pro_scanner():
    os.system('clear')
    print("="*45)
    print("   MEHDI BHAI REAL-DATA EXTRACTOR (V2)   ")
    print("="*45)
    
    area = input("[?] Enter Target Area: ")
    print(f"\n[*] Connecting to {area} Network Nodes...")
    
    # Rotating Animation (Gol Ghoomne Wala Design)
    symbols = ['|', '/', '-', '\\']
    for _ in range(30):
        for sym in symbols:
            sys.stdout.write(f'\r[+] Accessing Data Center... {sym}')
            sys.stdout.flush()
            time.sleep(0.1)
    
    print("\n\n[!] Error: Access Denied by Server Firewalls.")
    print("[!] Tip: Asli data ke liye victim ka phone control karna parhta hai.")
