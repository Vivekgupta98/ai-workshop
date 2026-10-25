# Running example: the item that gets reused

## The problem

You have `n` items. Each item has a weight and a value. Choose items whose total weight is at most the capacity and print the maximum total value.

**Each item may be selected at most once.**

Input:

```text
n capacity
weight_1 value_1
weight_2 value_2
...
```

## The plausible-looking buggy program

```python
n, capacity = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (capacity + 1)
for weight, value in items:
    for current in range(weight, capacity + 1):
        dp[current] = max(dp[current], dp[current - weight] + value)

print(dp[capacity])
```

The program is short, valid Python, and often returns a believable answer. That makes it a useful debugging case.

## The revealing test

```text
1 4
2 3
```

Only one item exists, so the correct output is `3`. The buggy program prints `6` because the upward loop reads values that the same item wrote earlier in the current iteration.

The invariant for 0/1 knapsack is that an item must not consume a state already updated by that item. Iterating capacity downward preserves that invariant:

```python
for current in range(capacity, weight - 1, -1):
```

## Where this example is used

- The specification is easy to understand.
- The code has no syntax or runtime error.
- The wrong answer needs a carefully chosen boundary case.
- The root cause is an algorithm invariant, not a typo.
- A test tool can prove that the old and corrected programs differ.
- The same bug works for direct calls, routing, retry loops, parallel review, checkpoints, and ReAct.

Days 0 to 4 use this program. Day 5 switches to three Codeforces wrong-answer cases so the agents can be compared across difficulty levels.
