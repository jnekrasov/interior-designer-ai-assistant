def get_formatted_image_generation_workflow(
    empty_room_image_url, 
    design_style_image_url, 
    design_prompt):
    return {
        "1": {
            "inputs": {
            "ckpt_name": "Realistic_Vision_V5.1.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
            "_meta": {
            "title": "Load Checkpoint"
            }
        },
        "2": {
            "inputs": {
            "seed": 42,
            "steps": 30,
            "cfg": 7,
            "sampler_name": "dpmpp_2m_sde",
            "scheduler": "karras",
            "denoise": 0.75,
            "model": [
                "24",
                0
            ],
            "positive": [
                "17",
                0
            ],
            "negative": [
                "17",
                1
            ],
            "latent_image": [
                "9",
                0
            ]
            },
            "class_type": "KSampler",
            "_meta": {
            "title": "KSampler"
            }
        },
        "3": {
            "inputs": {
            "text": design_prompt,
            "clip": [
                "1",
                1
            ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
            "title": "CLIP Text Encode (Prompt)"
            }
        },
        "4": {
            "inputs": {
            "text": "(normal quality), (low quality), (worst quality), paintings, sketches",
            "clip": [
                "1",
                1
            ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
            "title": "CLIP Text Encode (Prompt)"
            }
        },
        "5": {
            "inputs": {
            "image": empty_room_image_url,
            "upload": "image"
            },
            "class_type": "LoadImage",
            "_meta": {
            "title": "Load Image"
            }
        },
        "6": {
            "inputs": {
            "vae_name": "vae-ft-mse-840000-ema-pruned.safetensors"
            },
            "class_type": "VAELoader",
            "_meta": {
            "title": "Load VAE"
            }
        },
        "7": {
            "inputs": {
            "samples": [
                "2",
                0
            ],
            "vae": [
                "6",
                0
            ]
            },
            "class_type": "VAEDecode",
            "_meta": {
            "title": "VAE Decode"
            }
        },
        "8": {
            "inputs": {
            "images": [
                "7",
                0
            ]
            },
            "class_type": "PreviewImage",
            "_meta": {
            "title": "Preview Image"
            }
        },
        "9": {
            "inputs": {
            "pixels": [
                "5",
                0
            ],
            "vae": [
                "6",
                0
            ]
            },
            "class_type": "VAEEncode",
            "_meta": {
            "title": "VAE Encode"
            }
        },
        "15": {
            "inputs": {
            "control_net_name": "control_v11p_sd15_mlsd.pth"
            },
            "class_type": "ControlNetLoader",
            "_meta": {
            "title": "Load ControlNet Model"
            }
        },
        "16": {
            "inputs": {
            "preprocessor": "M-LSDPreprocessor",
            "resolution": 512,
            "image": [
                "5",
                0
            ]
            },
            "class_type": "AIO_Preprocessor",
            "_meta": {
            "title": "AIO Aux Preprocessor"
            }
        },
        "17": {
            "inputs": {
            "strength": 0.25,
            "start_percent": 0,
            "end_percent": 1,
            "positive": [
                "3",
                0
            ],
            "negative": [
                "4",
                0
            ],
            "control_net": [
                "15",
                0
            ],
            "image": [
                "16",
                0
            ]
            },
            "class_type": "ControlNetApplyAdvanced",
            "_meta": {
            "title": "Apply ControlNet (Advanced)"
            }
        },
        "21": {
            "inputs": {
            "images": [
                "16",
                0
            ]
            },
            "class_type": "PreviewImage",
            "_meta": {
            "title": "Preview Image"
            }
        },
        "22": {
            "inputs": {
            "preset": "PLUS (high strength)",
            "model": [
                "1",
                0
            ]
            },
            "class_type": "IPAdapterUnifiedLoader",
            "_meta": {
            "title": "IPAdapter Unified Loader"
            }
        },
        "23": {
            "inputs": {
            "clip_name": "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"
            },
            "class_type": "CLIPVisionLoader",
            "_meta": {
            "title": "Load CLIP Vision"
            }
        },
        "24": {
            "inputs": {
            "weight": 0.3,
            "weight_type": "style transfer",
            "combine_embeds": "concat",
            "start_at": 0,
            "end_at": 1,
            "embeds_scaling": "V only",
            "model": [
                "22",
                0
            ],
            "ipadapter": [
                "22",
                1
            ],
            "image": [
                "25",
                0
            ],
            "clip_vision": [
                "23",
                0
            ]
            },
            "class_type": "IPAdapterAdvanced",
            "_meta": {
            "title": "IPAdapter Advanced"
            }
        },
        "25": {
            "inputs": {
            "interpolation": "LANCZOS",
            "crop_position": "top",
            "sharpening": 0,
            "image": [
                "36",
                0
            ]
            },
            "class_type": "PrepImageForClipVision",
            "_meta": {
            "title": "Prep Image For ClipVision"
            }
        },
        "27": {
            "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "7",
                0
            ]
            },
            "class_type": "SaveImage",
            "_meta": {
            "title": "Save Image"
            }
        },
        "36": {
            "inputs": {
            "image": design_style_image_url,
            "upload": "image"
            },
            "class_type": "LoadImage",
            "_meta": {
            "title": "Load Image"
            }
        }
    }

import os
import requests
def download_and_persist_image(url, folder = 'output'):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    extension = os.path.splitext(url.split('/')[-1])[1]
    
    existing_files = os.listdir(folder)
    max_index = 0
    for file in existing_files:
        file_index = file.split('.')[0]
        try:
            index = int(file_index)
            if index > max_index:
                max_index = index
        except ValueError:
            continue
 
    new_filename = f"{max_index + 1:02d}{extension}"
    path = os.path.join(folder, new_filename)
 
    response = requests.get(url)
    response.raise_for_status()
 
    with open(path, 'wb') as f:
        f.write(response.content)
    
    print(f"Image saved as {path}")