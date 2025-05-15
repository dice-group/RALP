# RALP*: Learning Chain Of Thoughts Prompts for Predicting Entities, Relations, and even Literals on Knowledge Graphs

***RALP** stands for Retrieval Augmented Link Prediction.
For the ease of referencing, different models that we have implemented 
here are put under the name 'RALP framework' or for short, just 'RALP'.

## Link Prediction Results via Static RALP
```
python -m models.static_ralp --enrich_train --dataset_dir KGs/Countries-S3 --out "countries_s3_results.json" && cat countries_s3_results.json
```

```
cp -r KGs/Countries-S3 KGs/Enriched_Countries-S3
cat KGs/Enriched_Countries-S3/missing_triples.txt >> KGs/Enriched_Countries-S3/train.txt
bash rag_standard_exp.sh --dataset_dir KGs/Enriched_Countries-S3
```

#### Latex Table 
```
python dicee/analyse_experiments.py --dir Experiments --features "model" "testMRR" "testH@1" "testH@3" "testH@10"
```

do not forget to delete Experiments:

```
rm -rf Experiments
```

## Numerical link prediction

To generate predictions for numerical literals:

```aiignore
python -m LLP.py --kg_path KGs/LitWD1K --base_url http://some_llm_endpoint.com --temperature 0.1 --seed 42 --llm_model model_name
```

