import subprocess

# Set the font and font weight variables:
font = "monospace"
font_weight = "bold"

while True:
    # Run the Bash script and capture its output:
    output = subprocess.check_output(["bash", "-c", "font=${font:-monospace} font_weight=${font_weight:-bold} while : do xkb-switch -p | awk -v font=\"$font\" -v font_weight=\"$font_weight\" '{print \"<span font_family=\\\"\"font\"\\\"  font_weight=\\\"\"font_weight\"\\\">\"toupper($0)\"</span>\"}' || sleep 1 xkb-switch -w done"])

    # Convert the output to a string and print it:
    output_str = output.decode("utf-8")
    print(output_str)
