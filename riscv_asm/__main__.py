import logging
import os
import sys

logger = logging.getLogger("riscv_asm")

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logger.error("Please provide the file to convert via command line argument.")
        sys.exit()

    input_file_location = sys.argv[1]

    output_file_name = os.path.basename(input_file_location).split(".")[0] + ".o"
    output_file_location = f"./{output_file_name}"

    with open(input_file_location, "r", encoding="utf-8") as input_file:
        with open(output_file_location, "wb") as obj_file:
            for index, string in enumerate(input_file):
                obj_file.write(bytes([ord(s) for s in string]))
