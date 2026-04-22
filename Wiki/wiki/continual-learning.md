# Continual Learning

**Summary**: Continual learning is a machine learning paradigm where models keep adapting to new data or tasks over time while trying to preserve prior knowledge. In this wiki, it is distinct from MLOps-style continuous training pipelines. 

**Sources**: `raw/Continual Learning in Machine Learning.md`

**Last updated**: 2026-04-19

---

The source defines continual learning as an approach where models continue to grow and adapt over time instead of freezing their knowledge after a single training phase (source: Continual Learning in Machine Learning.md). It frames this as necessary because many real-world environments are dynamic and cannot be handled well by models trained once on static data (source: Continual Learning in Machine Learning.md).

## Central Challenge

The main problem highlighted by the source is [[catastrophic-forgetting]], where models lose performance on previously learned tasks when trained on new ones (source: Continual Learning in Machine Learning.md). The article presents this as the defining technical challenge that continual learning methods try to solve (source: Continual Learning in Machine Learning.md).

## Common Techniques

The source lists incremental learning, memory mechanisms, replay, transfer learning, and regularization as common components of continual learning systems (source: Continual Learning in Machine Learning.md). It specifically names Elastic Weight Consolidation and Synaptic Intelligence as regularization methods used to protect previously important parameters (source: Continual Learning in Machine Learning.md).

## Main Variants

The article distinguishes between task-based continual learning, [[class-incremental-learning]], and domain-incremental learning (source: Continual Learning in Machine Learning.md). These variants differ in how the incoming learning problem changes over time, whether by task identity, label space, or data distribution (source: Continual Learning in Machine Learning.md).

## Distinction From Continuous Training

The wiki should distinguish continual learning from [[continuous-training]] (inference: this is a wiki modeling decision based on both sources). The continual learning source describes a model-level learning paradigm, while the MLOps source describes automated retraining workflows triggered by new data or degraded performance (source: Continual Learning in Machine Learning.md; source: The Ultimate MLOps Roadmap for 2026 A Complete Guide to Becoming an MLOps Engineer.md).

## Related pages

- [[continual-learning-in-machine-learning]]
- [[catastrophic-forgetting]]
- [[class-incremental-learning]]
- [[continuous-training]]

