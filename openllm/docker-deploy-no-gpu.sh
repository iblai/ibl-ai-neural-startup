# pass model name as first argument.
docker run -d -p 3000:3000 ghcr.io/bentoml/openllm start $1 --backend pt