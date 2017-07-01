import pytest
import sys

sys.path.append("src/")
pytest.main(args=['-x', 'tests'])