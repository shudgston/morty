"""
Main CLI entry point.
"""
import argparse
from morty.calculators import MortgageCalculator
from morty import formatters


def main():
    """Main program entry point"""
    args = get_arguments()
    morty = MortgageCalculator(args.principal, args.term, args.interest, args.extra)
    formatter = get_formatter(args.format)

    formatter_obj = formatter(
        [payment for payment in morty.get_payments()],
        get_headers())

    formatter_obj.write()


def get_arguments():
    """Parse and return the arguments object"""
    parser = build_parser()
    return parser.parse_args()


def get_formatter(format):
    """Return a formatter class"""
    if format == 'csv':
        return formatters.CSVFormatter
    if format == 'table':
        return formatters.TableFormatter
    raise RuntimeError('Invalid formatter option: {}'.format(format))


def get_headers():
    """Create the standard headers list"""
    return ['Payment #', 'Payment', 'Principal', 'Interest', 'Total Interest', 'Balance']


def build_parser():
    """Construct an argparse parser object."""
    parser = argparse.ArgumentParser(description='Calculate mortgage payments')
    parser.add_argument(
        '-p',
        '--principal',
        required=True,
        type=int,
        help='principal amount')

    parser.add_argument(
        '-t',
        '--term',
        required=True,
        type=int,
        help='loan term in years')

    parser.add_argument(
        '-i',
        '--interest',
        required=True,
        type=float,
        help='fixed interest rate (ex 6.875)')

    parser.add_argument(
        '-e',
        '--extra',
        default=0,
        type=int,
        help='extra principal to apply to each payment')

    parser.add_argument(
        '-F',
        '--format',
        default='table',
        type=str,
        help='format output (csv or table)')
    return parser


if __name__ == '__main__':
    main()
