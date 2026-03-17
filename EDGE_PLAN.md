
# Edge Deployment Plan

## Goal
Allow emotion detection to run locally on mobile devices without cloud APIs.

## Benefits
- Privacy
- Offline capability
- Low latency

## Model Size
TF‑IDF vectorizer: ~5MB
XGBoost model: ~15MB
Total: ~20MB

## On‑Device Pipeline
User Input
→ Feature Processing
→ ML Model
→ Decision Engine
→ Recommendation

## Latency
Estimated inference: 20–50 ms on mobile CPU.

## Optimizations
- Reduce TF‑IDF vocabulary
- Tree pruning for XGBoost
- Quantization (8‑bit models)

## Privacy
User reflections remain on device.

## Tradeoffs
Advantages:
- Offline use
- Faster response
- Better privacy

Disadvantages:
- Smaller model capacity
- Harder model updates
