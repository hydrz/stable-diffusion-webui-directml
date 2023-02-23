from huggingface_hub import hf_hub_download

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="prompthero/openjourney-v2",
    filename="openjourney-v2-unpruned.ckpt",
)
