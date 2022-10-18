# Based on [GraphVQA](https://github.com/codexxxl/GraphVQA)


We aim
at GraphVQA task and adopted the original
[GraphVQA framework](https://github.com/codexxxl/GraphVQA). Based on which we
substituted the Seq2Seq module with a GNN
based module to parse questions in this task.
We further experimented our updated system
with multiple variations, including using different graph construction schemes (dependency
graphs and AMR graphs), using pretrained
model BERT for better node representations,
or using positional features and bidirectional
edges in GNN. Our final results outperformed
the original ones and achieved SOTA.

[The framework we adopted in this work. It contains 4 parts: 1. Question Parsing; 2. Scene Graph Encoding; 3. Graph Reasoning; 4. Answering. We used a Graph2Seq structure for the Question Parsing module.](https://github.com/RealNicolasBourbaki/GraphVQA/blob/master/pics/graphVQA_framework.png)

[The Graph2Seq sturcture we used](https://github.com/RealNicolasBourbaki/GraphVQA/blob/master/pics/g2s.JPG)

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
