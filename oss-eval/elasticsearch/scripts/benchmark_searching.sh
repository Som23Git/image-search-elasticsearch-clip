#!/bin/bash

OUT_DIR="../record" 
mkdir -p "$OUT_DIR"

echo "📊 Running ab benchmark (1000 req, 50 concurrency)..."
ab -n 1000 -c 50 -p payload.json -T application/json http://localhost:9200/msmarco/_search > "$OUT_DIR/ab_results.txt"

echo "📊 Running wrk benchmark (30s, 4 threads, 50 connections)..."
wrk -t4 -c50 -d30s -s es_search.lua http://localhost:9200/msmarco/_search > "$OUT_DIR/wrk_results.txt"

echo "✅ Benchmarks completed. Results saved in $OUT_DIR"