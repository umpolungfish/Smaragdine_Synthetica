"""Smaragdine Synthetica — CLI entry point."""

import sys
import argparse
from .navigator import lookup, list_versicles, analyse_operation


def main():
    parser = argparse.ArgumentParser(description='Smaragdine Synthetica — retrosynthetic alchemical compiler')
    sub = parser.add_subparsers(dest='command')

    p_lookup = sub.add_parser('lookup', help='Look up a versicle')
    p_lookup.add_argument('versicle', type=int, help='Versicle number (1-15)')

    p_list = sub.add_parser('list', help='List all versicles')

    p_analyse = sub.add_parser('analyse', help='Analyse a versicle operation')
    p_analyse.add_argument('versicle', type=int, help='Versicle number (1-15)')

    args = parser.parse_args()

    if args.command == 'lookup':
        result = lookup(args.versicle)
        print(f"Versicle {result['versicle']}: {result['operation']}")
        print(f"  Tuple: {result['tuple']}")
        print(f"  Label: {result['label']}")

    elif args.command == 'list':
        versicles = list_versicles()
        for v in versicles:
            print(f"V{v['versicle']:02d}: {v['operation']:20s}  {''.join(v['tuple'])}")

    elif args.command == 'analyse':
        analysis = analyse_operation(args.versicle)
        print(f"Operation: {analysis['operation']}")
        print("  Interpretation:")
        for k, v in analysis['interpretation'].items():
            print(f"    {k}: {v}")
        if analysis['bottlenecks']:
            print("  Bottlenecks:", '; '.join(analysis['bottlenecks']))

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
