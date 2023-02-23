from huggingface_hub import hf_hub_download

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_canny.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_depth.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_hed.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_mlsd.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_normal.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_scribble.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_openpose.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="models/control_sd15_seg.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="annotator/ckpts/body_pose_model.pth",
)

hf_hub_download(
    cache_dir="./cache",
    resume_download=True,
    repo_id="lllyasviel/ControlNet",
    filename="annotator/ckpts/hand_pose_model.pth",
)
