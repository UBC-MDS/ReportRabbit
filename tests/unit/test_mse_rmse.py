"""
A test module that tests the get_mse_rmse() and its helper functions,
get_mse() and get_rmse().
Note: these tests are written with the assistance of LLMs.
"""

from reportrabbit.mse_rmse import get_mse, get_rmse, get_mse_rmse
import pytest
import numpy as np


def test_get_mse_basic():
    """Test: Basic functionality of get_mse."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    out = get_mse(y_true, y_pred)
    expected_out = 0.0
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_get_rmse_basic():
    """Test: Basic functionality of get_rmse."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    out = get_rmse(y_true, y_pred)
    expected_out = 0.0
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_get_mse_rmse_basic():
    """Test: Basic functionality of get_mse_rmse."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    out = get_mse_rmse(y_true, y_pred)
    expected_out = {"mse": 0.0, "rmse": 0.0}
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_get_mse_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ for get_mse."""
    with pytest.raises(ValueError):
        get_mse([1, 2], [1, 2, 3])


def test_get_rmse_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ for get_rmse."""
    with pytest.raises(ValueError):
        get_rmse([1, 2], [1, 2, 3])


def test_get_mse_rmse_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ for get_mse_rmse."""
    with pytest.raises(ValueError):
        get_mse_rmse([1, 2], [1, 2, 3])


def test_get_mse_empty_list():
    """Test: Edge case - Empty inputs for get_mse."""
    with pytest.raises(ValueError):
        get_mse([], [])


def test_get_rmse_empty_list():
    """Test: Edge case - Empty inputs for get_rmse."""
    with pytest.raises(ValueError):
        get_rmse([], [])


def test_get_mse_rmse_empty_list():
    """Test: Edge case - Empty inputs for get_mse_rmse."""
    with pytest.raises(ValueError):
        get_mse_rmse([], [])


def test_get_mse_non_numeric():
    """Test: Ensure ValueError is raised for non-numeric input for get_mse."""
    with pytest.raises(ValueError):
        get_mse([1, 2, "a"], [1, 2, 3])


def test_get_rmse_non_numeric():
    """Test: Ensure ValueError is raised for non-numeric input for get_rmse."""
    with pytest.raises(ValueError):
        get_rmse([1, 2, "a"], [1, 2, 3])


def test_get_mse_rmse_non_numeric():
    """Test: Ensure ValueError is raised for non-numeric input for get_mse_rmse."""
    with pytest.raises(ValueError):
        get_mse_rmse([1, 2, "a"], [1, 2, 3])


def test_get_mse_rmse_with_weights():
    """Test: Functionality of get_mse_rmse with sample weights."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 4]
    sample_weight = [1, 1, 2]
    out = get_mse_rmse(y_true, y_pred, sample_weight=sample_weight)
    expected_out = {"mse": 0.75, "rmse": np.sqrt(0.75)}
    assert np.isclose(
        out["mse"], expected_out["mse"]
    ), f"Expected MSE {expected_out['mse']} but got {out['mse']}"
    assert np.isclose(
        out["rmse"], expected_out["rmse"]
    ), f"Expected RMSE {expected_out['rmse']} but got {out['rmse']}"


def test_get_mse_rmse_numpy_arrays():
    """Test: Functionality of get_mse_rmse with NumPy array inputs."""
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.5, 2.5, 3.5])
    out = get_mse_rmse(y_true, y_pred)
    expected_out = {"mse": 0.25, "rmse": 0.5}
    assert np.isclose(
        out["mse"], expected_out["mse"]
    ), f"Expected MSE {expected_out['mse']} but got {out['mse']}"
    assert np.isclose(
        out["rmse"], expected_out["rmse"]
    ), f"Expected RMSE {expected_out['rmse']} but got {out['rmse']}"


def test_get_mse_rmse_negative_and_float_values():
    """Test: Handles negative and floating-point values correctly."""
    y_true = [-1.0, 0.5, 2.0]
    y_pred = [-0.5, -0.5, 1.0]
    out = get_mse_rmse(y_true, y_pred)
    expected_out = {"mse": 0.75, "rmse": np.sqrt(0.75)}
    assert np.isclose(
        out["mse"], expected_out["mse"]
    ), f"Expected MSE {expected_out['mse']} but got {out['mse']}"
    assert np.isclose(
        out["rmse"], expected_out["rmse"]
    ), f"Expected RMSE {expected_out['rmse']} but got {out['rmse']}"
