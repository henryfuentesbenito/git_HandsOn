#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# Create the command line argument parser with a description
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# Required input argument: the sequence
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
# Optional argument: a motif to search within the sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If the user passed no arguments, show help and exit with code 1
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Actually parse the CLI arguments
args = parser.parse_args()

# Normalize the sequence to uppercase to make classification and search case-insensitive
args.seq = args.seq.upper() 

# Validate that the sequence only contains A, C, G, T, or U
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
# If invalid characters are present, it’s neither DNA nor RNA
else:
    print ('The sequence is not DNA nor RNA')

# --- Motif search (only if -m/--motif was provided) ---
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND (motif v2)")
    else:
        print("NOT FOUND (motif)")
