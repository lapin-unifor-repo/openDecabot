# ┌────────────────────────────────────────────┐
# │ ESP IDE  : FREE MicroPython WEB IDE        │
# │ AUTHOR   : Milan Spacek (2019–2026)        │
# │ WEB      : https://espide.eu               │
# │ LICENSE  : AGPL-3.0                        │
# │                                            │
# │ CODE IS OPEN — IMPROVEMENTS MUST STAY OPEN │
# │ Please contribute your improvements back   │
# └────────────────────────────────────────────┘

import time

# Program autostart
def autostart():
    try:
        os.stat('idecode')
    except OSError:
        return

    try:
        with open('idecode', 'r') as f:
            start_data = f.read(16)
        if "#autostart*" in start_data:
            print("Program autostart in 2s")
            time.sleep(2)
            print("Startuji...")
            try:
                run_code()
            except Exception as e:
                print("Runtime error:")
                sys.print_exception(e)
    except Exception as e:
        print("Error reading file 'idecode':")
        sys.print_exception(e)

autostart()


