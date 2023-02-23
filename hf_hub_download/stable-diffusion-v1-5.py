from huggingface_hub import hf_hub_download

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="runwayml/stable-diffusion-v1-5",
    filename="v1-5-pruned.safetensors",
)
