# RISC-V Assembler

A toy assembler for the RV32I ISA.

## Purpose

The purpose of this assembler is to become familiar with the instruction set, machine code, and writing assembly. It probably shouldn't be used for anything important.

## Installation and Use

Set up the Python environment using `conda`.

```
conda env create -f environment.yml
conda activate riscv_asm
poetry install
```

Running the assembler:

```
python -m riscv_asm path_to_assembly_file.s
```
