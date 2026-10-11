from diffusers import StableDiffusionImg2ImgPipeline, DPMSolverMultistepScheduler
import gradio as gr
from translate import Translator
from PIL import Image

def img2img(device: str, model_file: str, image: str, prompt: str, steps: int):
        pipe2 = StableDiffusionImg2ImgPipeline.from_single_file(model_file).to(device)
        pipe2.scheduler = DPMSolverMultistepScheduler.from_config(
            pipe2.scheduler.config, timestep_spacing="trailing", use_karras_sigmas=True
        )
        img0 = Image.open(image)
        img = pipe2(Translator('en','ja').translate(prompt), image=img0, num_inference_steps=steps).images[0]
        gr.Info("生成が完了しました。")
        return img