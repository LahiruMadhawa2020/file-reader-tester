from utility_file_reader import reader_utility
import pytest
import logging
import sys


LOGGER = logging.getLogger(__name__)


@pytest.mark.reader
@pytest.mark.run(order=1)
def test_reader():
    reader01 = reader_utility.reader_without_configuration_file('csv', 'input_files/csv/csv_s1.csv', ',', 'yes', 'na', 'na', 'na', 'no', 'na')
    print(reader01)
    reader_02 = reader_utility.reader_from_configuration_file('ini', 'configuration_files/file_reader_config/csv_reader_config.ini', 'source_01')
    print(reader_02)


