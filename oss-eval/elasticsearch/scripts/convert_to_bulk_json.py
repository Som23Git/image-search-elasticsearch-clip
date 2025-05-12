import json

input_file = "../collection/collection.10k.tsv"
output_file = "../record/es_bulk_msmarco_10k.jsonl"

with open(input_file, "r", encoding="utf8") as infile, open(output_file, "w", encoding="utf8") as outfile:
    for line in infile:
        parts = line.strip().split("\t")
        if len(parts) != 2:
            continue
        docid, passage = parts
        action = {"index": {"_index": "msmarco", "_id": docid}}
        doc = {"passage": passage}
        outfile.write(json.dumps(action) + "\n")
        outfile.write(json.dumps(doc) + "\n")
