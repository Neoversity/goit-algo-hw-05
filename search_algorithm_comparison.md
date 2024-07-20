# Comparison of Substring Search Algorithms

| Article  | Substring Type | Algorithm    | Time (seconds) |
|----------|----------------|--------------|----------------|
| article1 | existing | boyer_moore | 0.000580 |
| article1 | existing | kmp | 0.003186 |
| article1 | existing | rabin_karp | 0.004894 |
| article1 | non_existing | boyer_moore | 0.000399 |
| article1 | non_existing | kmp | 0.003527 |
| article1 | non_existing | rabin_karp | 0.003937 |
| article2 | existing | boyer_moore | 0.000919 |
| article2 | existing | kmp | 0.005870 |
| article2 | existing | rabin_karp | 0.006311 |
| article2 | non_existing | boyer_moore | 0.000872 |
| article2 | non_existing | kmp | 0.004731 |
| article2 | non_existing | rabin_karp | 0.006719 |

## Conclusions
Based on the measured times, we can conclude the following:
- For article1 with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000580 seconds.
- For article1 with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000399 seconds.
- For article2 with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000919 seconds.
- For article2 with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000872 seconds.

Overall, the fastest algorithm is boyer_moore with a time of 0.000399 seconds.
