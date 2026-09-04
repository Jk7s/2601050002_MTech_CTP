# Q1. E-Commerce Product Search — Solution

## (a) Where sequence, mapping, and set fit

| Data structure | Used for | Why |
|---|---|---|
| **Sequence (list)** | Storing the full collection of product records | Products need to be iterated over, kept in insertion order, and possibly paginated/displayed as a list |
| **Mapping (dict)** | Each product record itself (`{'id':..., 'category':..., 'price':..., 'tags':...}`) — or an index like `category → list of products` | Fast O(1) average-time lookup by key (e.g. product ID or category), instead of scanning every record |
| **Set** | The `tags` field of each product, and the "search tags" the user supplies | Tags have no duplicates and only membership/intersection matters — sets give O(1) average membership tests and fast intersection |

## (b) Rewriting the filter with comprehensions + set operations

**Naive (nested-loop) version** — what the team currently does:

```python
def find_products_nested(products, target_category, search_tags):
    results = []
    for product in products:
        if product['category'] == target_category:
            match = False
            for tag in product['tags']:
                for s_tag in search_tags:
                    if tag == s_tag:
                        match = True
            if match:
                results.append(product)
    return results
```

**Pythonic version** — comprehension + set intersection:

```python
def find_products(products, target_category, search_tags):
    search_tags = set(search_tags)  # ensure O(1) membership / fast intersection
    return [
        product for product in products
        if product['category'] == target_category
        and product['tags'] & search_tags        # set intersection
    ]
```

Example data:

```python
products = [
    {'id': 1, 'category': 'electronics', 'price': 299, 'tags': {'wireless', 'audio'}},
    {'id': 2, 'category': 'electronics', 'price': 899, 'tags': {'gaming', 'laptop'}},
    {'id': 3, 'category': 'furniture',   'price': 150, 'tags': {'wooden', 'chair'}},
]

matches = find_products(products, 'electronics', ['audio', 'bluetooth'])
# -> [{'id': 1, 'category': 'electronics', 'price': 299, 'tags': {'wireless','audio'}}]
```

`product['tags'] & search_tags` returns a non-empty set (truthy) if there's at least one common tag — that single expression replaces the entire inner double loop.

An even faster variant if filtering by category **repeatedly**, using a dict index:

```python
from collections import defaultdict

def build_category_index(products):
    index = defaultdict(list)
    for p in products:
        index[p['category']].append(p)
    return index

def find_products_indexed(index, target_category, search_tags):
    search_tags = set(search_tags)
    return [p for p in index[target_category] if p['tags'] & search_tags]
```

## (c) Why these structures are preferable to repeatedly searching lists

- **Lists force linear scanning.** Checking `category == target` or `tag in tag_list` means walking through elements one by one until a match is found (or the list ends) — there's no way to "jump" to the right entry.
- **Dicts and sets use hashing.** Instead of comparing against every element, a hash of the key/value is computed and used to jump almost directly to the right bucket — this is what makes lookup and membership testing so much faster.
- **Sets eliminate the nested loop entirely.** Matching "at least one common tag" between two tag lists normally requires comparing every tag against every other tag. A set intersection (`&`) does this comparison internally using hashing, so the programmer doesn't need an explicit nested loop at all.
- **A dict index avoids repeating the category scan.** If searches happen many times, scanning the full product list for the category on *every single query* is wasteful. Building a `category → products` dict once means each future query jumps straight to the relevant subset.

## Time Complexity

| Approach | Category filter | Tag matching (per product) | Overall (N products, n/m tags) |
|---|---|---|---|
| Nested loops (original) | O(N) scan | O(n·m) comparisons | **O(N · n · m)** |
| Comprehension + set intersection | O(N) scan | O(min(n, m)) average | **O(N · min(n, m))** |
| + dict category index | O(1) average lookup | O(min(n, m)) average | **O(k · min(n, m))**, where k = products in that category |

Where:
- **N** = total number of products
- **n, m** = number of tags per product / number of search tags
- **k** = number of products in the target category (k ≤ N)

The dict + set version scales much better because both dict lookups and set intersections run in **O(1) / O(min(n,m)) average case** (via hashing) rather than the O(N) and O(n·m) required by repeated linear searches.
