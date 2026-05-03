import warnings
import numpy as np
from sklearn.utils.validation import column_or_1d
import pytest

def test_data_conversion_warning():
    y_column_vector = np.array([[1], [2], [3]])
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        column_or_1d(y_column_vector, warn=True)
        assert len(w) > 0
        assert issubclass(w[-1].category, UserWarning)

def test_ravel_shape():
    y_column_vector = np.array([[1], [2], [3]])
    y_raveled = y_column_vector.ravel()
    assert y_raveled.shape == (3,)
    assert np.array_equal(y_raveled, np.array([1, 2, 3]))