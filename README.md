# ibl-ai-neural-startup

This project presents different ways to run llms in production

> [!Note]
> Openllm with gpu support is the preferred means of running llms for high throughput.


## OpenLLM
OpenLLM exposes an intuitive api on top of backends like vllm, ctranslate, etc. It scales very well and has very good integration with langchain through langchain's `OpenLLM` llm class.

Three approaches to deploying with openllm are presented in the openllm directory.
1. deploy.sh: Run openllm directly on the host device. This checks to ensure that python3 and openllm packages are installed. You must always pass a model's repo_id from huggingface as input parameter.
2. docker-deploy-no-gpu.py: This runs opennl model in a non-gpu container. 
3. docker-deploy-gpu.py: This runs openllm in docker with gpu support. `nvidia-smi` driver must be configured from the aws instance.


## api
The api module presents a mini fastapi app that expoises endpoints for inference. This has only minimal features.

#### usage
You can either run the project directly
```shell
cd api
pip install -r requirements.txt
uvicorn app:app
```


Or run with docker using

```
cd api
docker build . -t api
docker run --rm -d --gpus all -p 3000:3000  api
```
You may run without gpus but at a performance penalty.e