# Comparison of Substring Search Algorithms

| Article  | Substring Type | Algorithm    | Time (seconds) |
|----------|----------------|--------------|----------------|
| article1 | existing | boyer_moore | 0.000020 |
| article1 | existing | kmp | 0.000081 |
| article1 | existing | rabin_karp | 0.000070 |
| article1 | non_existing | boyer_moore | 0.000243 |
| article1 | non_existing | kmp | 0.004750 |
| article1 | non_existing | rabin_karp | 0.005544 |
| article2 | existing | boyer_moore | 0.000515 |
| article2 | existing | kmp | 0.001503 |
| article2 | existing | rabin_karp | 0.000906 |
| article2 | non_existing | boyer_moore | 0.000700 |
| article2 | non_existing | kmp | 0.006245 |
| article2 | non_existing | rabin_karp | 0.006549 |

## Conclusions
Based on the measured times, we can conclude the following:
- For article1 with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000020 seconds.
- For article1 with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000243 seconds.
- For article2 with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000515 seconds.
- For article2 with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000700 seconds.

Overall, the fastest algorithm is boyer_moore with a time of 0.000020 seconds.
