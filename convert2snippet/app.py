import contextlib
import sys

def process_line(line) -> str:
    # Escape backslashes and dollar signs, and wrap the line in double quotes
    line = line.replace('\\', '\\\\').replace('$', '\\$').replace('"', '\\"')
    return f'"{line}",'

def main():
    lines = []

    # Check if a file is provided as a command line argument
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            lines = file.readlines()
    else:
        # Read from standard input
        print("Enter text (type END to finish):")
        with contextlib.suppress(EOFError):
            while True:
                line = input()
                if line == "END":
                    break 
                lines.append(line)
    # Process each line
    for line in lines:
        print(process_line(line.strip()))

if __name__ == "__main__":
    main()
