"""
Shared MongoDB query-fragment helpers.
"""
import re


def case_insensitive_exact(value: str) -> dict:
    """Query fragment for an exact, case-insensitive string match."""
    return {"$regex": f"^{re.escape(value)}$", "$options": "i"}


def case_insensitive_contains(value: str) -> dict:
    """Query fragment for a case-insensitive substring match."""
    return {"$regex": re.escape(value), "$options": "i"}


def _singular(word: str) -> str:
    """Crude English singular: 'shirts' -> 'shirt', 'dresses' -> 'dress'; 'dress' stays."""
    lower = word.lower()
    if lower.endswith(("sses", "xes", "ches", "shes")):
        return word[:-2]
    if lower.endswith("s") and not lower.endswith("ss"):
        return word[:-1]
    return word


def keyword_contains(keyword: str) -> dict:
    """
    Substring match for a product-name keyword that also finds singular names,
    so 'polo shirts' matches 'Striped Polo Shirt'. Each stem is a prefix of its
    word, so anything the original keyword matched still matches.
    """
    # ponytail: suffix rules, not a stemmer; use a $text index or Atlas Search if irregular plurals matter.
    return case_insensitive_contains(" ".join(_singular(w) for w in keyword.split()))


def price_range_filter(min_price: int = None, max_price: int = None) -> dict:
    """Query fragment for a price range; empty dict if neither bound is given."""
    price_query = {}
    if min_price is not None:
        price_query["$gte"] = min_price
    if max_price is not None:
        price_query["$lte"] = max_price
    return price_query
