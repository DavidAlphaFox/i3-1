import subprocess

def get_keyboard_layout():
    # Run the xkb-switch command and capture its output:
    output = subprocess.check_output(["xkb-switch", "-p"])
    
    # Convert the output to a string and return it:
    return output.decode("utf-8").strip()

def bumblebee_status():
    # Get the current keyboard layout:
    layout = get_keyboard_layout()
    
    # Return the layout as part of the Bumblebee status string:
    return [{
        "name": "keyboard_layout",
        "full_text": f" {layout}",
    }]
