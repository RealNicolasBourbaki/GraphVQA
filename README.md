# Based on [GraphVQA](https://github.com/codexxxl/GraphVQA)

with mostly following changes:
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