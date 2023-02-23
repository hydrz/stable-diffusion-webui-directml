from huggingface_hub import hf_hub_download

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="andite/anything-v4.0",
    filename="anything-v4.5.safetensors",
)
