
# Error Analysis

## Case 1 – Ambiguous Reflection
Input: I sat quietly thinking about many things.
Problem: No clear emotional signal.
Improvement: Use contextual embeddings.

## Case 2 – Very Short Input
Input: ok
Problem: Insufficient text information.
Improvement: Add rule-based detection.

## Case 3 – Conflicting Signals
Input: I feel stressed but the ocean sound helped me relax.
Problem: Mixed emotional cues.
Improvement: Multi-label emotion classification.

## Case 4 – Figurative Language
Input: My mind feels like a storm.
Problem: Model struggles with metaphor.
Improvement: Use transformer embeddings.

## Case 5 – Neutral Reflection
Input: I spent some time sitting on a bench.
Problem: Emotion unclear.
Improvement: Add neutral class.

## Case 6 – Missing Context
Input: I feel tired.
Problem: Metadata needed.
Improvement: Improve feature engineering.

## Case 7 – Label Noise
Some dataset labels inconsistent.
Improvement: Dataset cleaning.

## Case 8 – Sarcasm
Input: Another perfect day of stress.
Problem: Model misinterprets sarcasm.
Improvement: sentiment context detection.

## Case 9 – Long Reflection
Long text dilutes signals.
Improvement: sentence embeddings.

## Case 10 – Mixed Emotions
Input: I feel excited but nervous.
Improvement: multi-label prediction.
