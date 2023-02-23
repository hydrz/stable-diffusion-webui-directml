from huggingface_hub import hf_hub_download

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="stabilityai/stable-diffusion-2-1",
    filename="v2-1_768-ema-pruned.safetensors",
)
