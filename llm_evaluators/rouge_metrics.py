from rouge import Rouge

from llm_evaluators.base import RougeEvaluator


class RougeMetrics(RougeEvaluator):

    def evaluate(self):
        rouge = Rouge()
        scores = rouge.get_scores(hyps=self.ground_truth, refs=self.predicted)

        all_metrics = scores[0]

        return all_metrics

    def __call__(self, *args, **kwargs):
        metrics = self.evaluate()

        return metrics
