"""Self-check for keyword_contains. Run: python -m app.utils.test_mongo"""
import re

from .mongo import keyword_contains


def matches(keyword: str, name: str) -> bool:
    fragment = keyword_contains(keyword)
    return re.search(fragment["$regex"], name, re.IGNORECASE) is not None


def test_keyword_contains():
    assert matches("shirts", "Striped Polo Shirt")
    assert matches("polo shirts", "Striped Polo Shirt")
    assert matches("dresses", "Floral Summer Dress")
    assert matches("dress", "Floral Summer Dress")
    assert matches("jeans", "Slim Fit Blue Jeans")
    assert matches("watches", "Smart Watch")
    assert matches("hoodies", "Modern Men Hoodie")
    assert not matches("shoes", "Cargo Shorts")
    assert keyword_contains("a.b") == {"$regex": r"a\.b", "$options": "i"}  # still regex-escaped


if __name__ == "__main__":
    test_keyword_contains()
    print("keyword_contains OK")
