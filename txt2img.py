from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import gradio as gr
from translate import Translator

def txt2img(device, model_file, prompt, steps):
    pipe1 = StableDiffusionPipeline.from_single_file(model_file).to(device)
    pipe1.scheduler = DPMSolverMultistepScheduler.from_config(
        pipe1.scheduler.config, timestep_spacing="trailing", use_karras_sigmas=True
    )
    img = pipe1(Translator('en','ja').translate(prompt), num_inference_steps=steps).images[0]
    gr.Info("生成が完了しました。")
    return img