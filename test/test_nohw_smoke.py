import pyorbbecsdk


def test_TC_CORE_001_import_module():
    """Verify python module can be imported in no-hardware CI."""
    assert pyorbbecsdk is not None


def test_TC_CORE_002_basic_symbols_exist():
    """Verify core symbols are available without opening a device."""
    assert hasattr(pyorbbecsdk, "Context")
    assert hasattr(pyorbbecsdk, "OBLogLevel")
    assert hasattr(pyorbbecsdk, "OBPropertyID")
