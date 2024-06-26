#!/usr/bin/env python

import argparse
import json
import sys

from postcodes.parsers.uk import PostCodeUK


def displays_header_text_output():
    print('Parsing postcode validations...')


def displays_postcode_text_output(postcode):
    # displays header
    print('\n---')
    status = 'VALID' if postcode.is_valid else 'INVALID'
    print(f'Postcode ({postcode.postcode}) format is: {status}')

    # displays errors reasons
    if not postcode.is_valid:
        print('  Errors:')
    for error_detail in postcode.errors.values():
        print(f'    -> {error_detail}')

    # displays postcode attributes
    print('  Attributes:')
    for attribute in postcode.attributes:
        attribute_detail = '(invalid format)' if attribute in postcode.errors.keys() else ''
        print(f'    -> {attribute}: {getattr(postcode, attribute)}{attribute_detail}')


def displays_results_text_output(valid_postcodes, invalid_postcodes):
    # displays header
    print('\n---')
    print('Results:')

    # displays valid postcodes
    if valid_postcodes:
        valid_postcodes_str = '(' + '), ('.join(valid_postcodes) + ')'
        print(f'  -> Valid postcodes: {valid_postcodes_str}')

    # displays invalid postcodes
    if invalid_postcodes:
        invalid_postcodes_str = '(' + '), ('.join(invalid_postcodes) + ')'
        print(f'  -> Invalid postcodes: {invalid_postcodes_str}')


def displays_results_json_output(all_postcodes):
    # displays combined jsons of many postcode validations
    print(json.dumps(all_postcodes, indent=4, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description='A command line to parses postcodes.')
    parser.add_argument('-p', '--postcodes', type=str, nargs='*', required=True,
                        help='The post code to analise.')
    parser.add_argument('-r', '--region-format', type=str, default='UK', choices=['UK'],
                        help='The region format.')
    parser.add_argument('-o', '--output-format', type=str, default='text', choices=['json', 'text'],
                        help='The region format.')
    args = parser.parse_args()

    # executes the format validations
    if args.output_format == 'text':
        displays_header_text_output()

    # parses format validations
    all_postcodes = {}
    valid_postcodes = []
    invalid_postcodes = []
    for raw_postcode in args.postcodes:
        # assign validations on variables
        postcode = PostCodeUK(raw_postcode)
        all_postcodes[raw_postcode] = postcode.to_dict()
        if postcode.is_valid:
            valid_postcodes.append(postcode.postcode)
        else:
            invalid_postcodes.append(postcode.postcode)

        # if output_format if json skips verbose prints on display
        if args.output_format == 'json':
            continue

        # if output_format if text show display with prints
        displays_postcode_text_output(postcode)

    # if output_format if text prints on display final results
    if args.output_format == 'text':
        displays_results_text_output(valid_postcodes, invalid_postcodes)

    # if output_format if json prints on display the group of dicts
    if args.output_format == 'json':
        displays_results_json_output(all_postcodes)

    # finish the program
    sys.exit(1 if invalid_postcodes else 0)


if __name__ == '__main__':
    main()
