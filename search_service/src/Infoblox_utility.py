import logging
import csv
logger = logging.getLogger(__name__)

DATABASE_FILENAME = "database/catalog.csv"


def fetch_contact(input):
    with open('database/catalog.csv', newline='') as csvfile:
        contactsreader = csv.reader(csvfile)
        find_flag = False
        for row in contactsreader:
            row_lower = map(lambda x: x.lower(), (row[0], row[1]))
            if input.lower() in list(row_lower):
                find_flag = True
                logger.info(",".join(row))
        if not find_flag:
            logger.warning("No input found")


# Driver to verify the module classes and functions.
if __name__ == '__main__':
    import sys

    # Initialize the logger for this module if run as a standalone script.
    def init_logger():
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter(fmt))

        root_log = logging.getLogger()
        root_log.setLevel(logging.INFO)
        root_log.addHandler(handler)

    init_logger()
    if len(sys.argv) != 2:
        logger.error("Invalid input")
    else:
        logger.info("Fetching contact {} from address book".format(
            sys.argv[1]))
        fetch_contact(sys.argv[1])
