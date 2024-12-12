# Open the file with the audacity markers
input_file = "markers.txt"  # Replace with the name of your input file
output_file = "output.js"  # Replace with the desired output file name

# Read the input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Initialize variables
last_time = 0.0  # To store the last marker time
output_lines = []  # To store the generated JavaScript lines

for line in lines:
    parts = line.strip().split("\t")
    if len(parts) == 3:  # Ensure the line has the expected format
        start_time, end_time, name = parts
        try:
            current_time = float(start_time)
            time_difference = int((current_time - last_time) * 1000)  # Convert to milliseconds
            js_line = f"await new Promise(resolve => setTimeout(resolve, {time_difference}));\n//{name}"
            output_lines.append(js_line)
            last_time = current_time  # Update the last time
        except ValueError:
            print(f"Error processing line: {line}")

# Write the output to a file
with open(output_file, "w") as file:
    file.write("\n".join(output_lines))

print(f"JavaScript statements written to {output_file}")
