#!/usr/local/bin/python3
import sys

def main():
    out_string = sys.argv[1] # string to output
    write_files = sys.argv[2:] # variable amount of files to write to
    sys.stdout.write(out_string)
    for file in write_files:
        with open(file, 'w') as fh:
            fh.write(out_string)

if __name__ == '__main__':
    main()
