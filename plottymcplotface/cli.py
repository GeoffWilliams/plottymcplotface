import logging
import argparse
import pkg_resources
import sys
import plottymcplotface.chart

logger = logging.getLogger(__name__)


def setup_logging(level, logger_name=__name__):
    _logger = logging.getLogger(logger_name)
    _logger.setLevel(level)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(
        "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    )
    _logger.addHandler(console_handler)

    _logger.debug("====[debug mode enabled]====")

def version():
    return pkg_resources.require("plottymcplotface")[0].version

def create_chart(filename):
    logger.info(f"created {filename}")
    plottymcplotface.chart.save(filename)


def main():
    parser = argparse.ArgumentParser(description="""
        Describe plottymcplotface here...
    """)

    parser.add_argument('--debug',
                        default=False,
                        action='store_true',
                        help='Enable debugging output')
    parser.add_argument('--version',
                        default=False,
                        action='store_true',
                        help='Print the sysdef version and exit')
    parser.add_argument('--output-file',
                        default=False,
                        help='file to save chart to')
    args = parser.parse_args()
    setup_logging(logging.DEBUG if args.debug else logging.INFO)
    exit_status = 1
    try:
        if args.version:
            print(version())
            exit_status = 0
        elif args.output_file:
            create_chart(args.output_file)
            exit_status = 0
        else:
            parser.print_usage()
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.error(str(exc_value))
        if args.debug:
            logger.exception(e)

    sys.exit(exit_status)
