import pytest
import sys

sys.path.append("example_server/")
pytest.main(args=['-x', 'tests'])