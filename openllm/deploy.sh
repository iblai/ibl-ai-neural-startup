

# apt update; apt upgrade -y

apt install -y python3 python3-pip

pip3 install "openllm[vllm]"

openllm start $1  --backend vllm
