# RALP*: Learning Chain Of Thoughts Prompts for Predicting Entities, Relations, and even Literals on Knowledge Graphs

***RALP** stands for Retrieval Augmented Link Prediction.
For the ease of referencing, different models that we have implemented 
here are put under the name 'RALP framework' or for short, just 'RALP'.

## Link Prediction Results via Static RALP

In the following command, please specify also the arguments to configure the LLM: `--base_url`, `--llm_model_name` and `--api_key`.
```aiignore
python -m models.static_ralp --enrich_train --dataset_dir KGs/Countries-S3 --out "countries_s3_results.json"  && cat countries_s3_results.json
```

```aiignore
cp -r KGs/Countries-S3 KGs/Enriched_Countries-S3
cat KGs/Enriched_Countries-S3/missing_triples.txt >> KGs/Enriched_Countries-S3/train.txt
bash rag_standard_exp.sh --dataset_dir KGs/Enriched_Countries-S3
```

#### Latex Table 

```aiignore
python dicee/analyse_experiments.py --dir Experiments --features "model" "testMRR" "testH@1" "testH@3" "testH@10"
```

do not forget to delete Experiments:

```aiignore
rm -rf Experiments
```

## Numerical link prediction

To generate predictions for numerical literals:

```aiignore
python -m LLP.py --kg_path KGs/LitWD1K --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name
```

## OWL Reasoning / Instance Retrieval

For manchester syntax and triples represented using full IRI:
```aiignore
python -m IRLLM.py --kg_path KGs/Father/father.owl --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name --output_csv_path IR_results_m.csv --expression_language manchester 
```

For manchester syntax and triples represented using IRI without namespace:

```aiignore
python -m IRLLM.py --kg_path KGs/Father/father.owl --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name --output_csv_path IR_results_m.csv --expression_language manchester --triple_without_namespace
```

For DL syntax and triples represented using full IRI:

```aiignore
python -m IRLLM.py --kg_path KGs/Father/father.owl --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name --output_csv_path IR_results_m.csv --expression_language dl
```

For DL syntax and triples represented using IRI without namespace:

```aiignore
python -m IRLLM.py --kg_path KGs/Father/father.owl --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name --output_csv_path IR_results_m.csv --expression_language dl --triple_without_namespace
```

Note: We tried to run this commands multiple time and sometime we get different results. We attribute this to the difference in 
few-shot examples that are generated and the LLM temperature.