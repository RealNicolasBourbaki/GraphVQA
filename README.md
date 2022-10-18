# Based on [GraphVQA](https://github.com/codexxxl/GraphVQA)


This is a report for seminar Advanced Machine
Learning at University of Stuttgart. We aim
at GraphVQA task and adopted the original
GraphVQA framework. Based on which we
substituted the Seq2Seq module with a GNN
based module to parse questions in this task.
We further experimented our updated system
with multiple variations, including using different graph construction schemes (dependency
graphs and AMR graphs), using pretrained
model BERT for better node representations,
or using positional features and bidirectional
edges in GNN. Our final results outperformed
the original ones.


* ```gqa_dataset_entry.py```: 
	1. Added graph construction and new qa vocab construction (under class ```GQATorchDataset```: ```def _get_features``` and ```def build_question_graph_edges_vocab```)
	2. Reconstructed ```class GQATorchDataset_collate_fn``` to include tree information

* ```pipeline_model_gat.py```:
	1. Added class ```GNNQuestionEncoder```
	2. Added class ```BertQuestionEncoder```
	3. Reconstructed ```class PipelineModel``` to include new encoders

* ```edge_vocab.py```: 
	-Collect edge vocabs

* ```graph_construction/```:
	- Code that used to construct trees based on the questions

* ```mainExplain_gat.py```:
	- Reconstructed to fit with the new data structure and new encoders.
