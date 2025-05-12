#!/bin/bash

# Determine the directory this script is in
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

DOC_FILE="$BASE_DIR/record/es_bulk_msmarco_10k.jsonl"
OUT_FILE="$BASE_DIR/record/indexing_stats.txt"
RESPONSE_FILE="$BASE_DIR/record/bulk_response.json"

# Exit if required file doesn't exist
if [[ ! -f "$DOC_FILE" ]]; then
  echo "❌ Document file not found: $DOC_FILE"
  exit 1
fi

DOC_COUNT=$(grep -c '"index"' "$DOC_FILE")

echo "📦 Starting bulk indexing of $DOC_COUNT documents..."

START=$(date +%s.%N)

curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk \
  --data-binary @"$DOC_FILE" -o "$RESPONSE_FILE"

END=$(date +%s.%N)
ELAPSED=$(echo "$END - $START" | bc)

echo "⏱️ Indexing completed in $ELAPSED seconds"

# Calculate docs/sec (rounded to integer)
DOCS_PER_SEC=$(echo "$DOC_COUNT / $ELAPSED" | bc)

# Count errors (requires jq)
if command -v jq &> /dev/null; then
  ERROR_COUNT=$(jq '[.items[] | select(.index.status != 201)] | length' "$RESPONSE_FILE")
else
  echo "⚠️ jq not found; skipping error count."
  ERROR_COUNT="N/A"
fi

# Write report
{
  echo "Indexing Performance Report"
  echo "==========================="
  echo "Documents Indexed: $DOC_COUNT"
  echo "Total Time: $ELAPSED seconds"
  echo "Docs/sec: $DOCS_PER_SEC"
  echo "Errors: $ERROR_COUNT"
  echo "Timestamp: $(date)"
} > "$OUT_FILE"

echo "✅ Report saved to $OUT_FILE"