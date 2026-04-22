# Continuous Training

**Summary**: Continuous training is the automated retraining of machine learning models when new data arrives or model performance degrades. The source treats it as a core automation pattern in MLOps. 

**Sources**: `raw/The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md`

**Last updated**: 2026-04-19

---

The article describes automated model retraining as part of ML CI/CD and says pipelines can retrain models when new data arrives or performance dips (source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md). In its FAQ section, it defines Continuous Training as automatically retraining models when new data becomes available so they remain current and accurate (source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md).

## Relationship to Monitoring

The source connects retraining to production monitoring, especially when detecting model drift or performance degradation (source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md). In that sense, continuous training depends on strong observability, validated data flows, and reliable deployment pipelines (source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md).

## Distinction From Continual Learning

This page is about an MLOps workflow pattern rather than a model-learning paradigm (inference: this is a wiki modeling decision based on both sources). The wiki should distinguish [[continuous-training]] from [[continual-learning]]: continuous training refers to automated retraining pipelines in production systems, while continual learning refers to models that adapt over time while preserving prior knowledge (source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md; source: Continual Learning in Machine Learning.md).

## Related pages

- [[mlops]]
- [[ml-ci-cd]]
- [[model-drift]]
- [[experiment-tracking]]
- [[continual-learning]]
