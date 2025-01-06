#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os
from datetime import datetime
import base64

# App configuration
class CFG:
    model_id = "stabilityai/stable-diffusion-2"  # Hugging Face model ID
    device = "cuda" if torch.cuda.is_available() else "cpu"
    image_size = (400, 400)  # Resize generated images
    image_gen_steps = 50
    guidance_scale = 9
    history_dir = "./generated_images"  # Directory to save images

# Load the model (cached for efficiency)
@st.cache_resource
def load_model():
    model = StableDiffusionPipeline.from_pretrained(
        CFG.model_id, 
        torch_dtype=torch.float16,
        revision="fp16", 
        use_auth_token="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"  # Replace with your Hugging Face token
    ).to(CFG.device)
    return model

# Set background image (optional)
def set_background(image_path):
    with open(image_path, "rb") as file:
        data = file.read()
    b64_image = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{b64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Uncomment to add a background image
# set_background("background.jpg")

# Initialize
st.title("Text-to-Image Generator")
st.subheader("Generate stunning images from text prompts")

# Load the model
model = load_model()

# Ensure history directory exists
os.makedirs(CFG.history_dir, exist_ok=True)

# Prompt input
prompt = st.text_input("Enter your prompt:", placeholder="e.g., A futuristic cityscape at sunset")

if st.button("Generate Image"):
    if prompt.strip() == "":
        st.error("Please enter a valid prompt!")
    else:
        with st.spinner("Generating image..."):
            # Generate the image
            generated_image = model(
                prompt, 
                num_inference_steps=CFG.image_gen_steps,
                guidance_scale=CFG.guidance_scale
            ).images[0]

            # Resize the image
            generated_image = generated_image.resize(CFG.image_size)

            # Save the image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(CFG.history_dir, f"{timestamp}.png")
            generated_image.save(file_path)

            # Display the generated image
            st.image(generated_image, caption=f"Prompt: {prompt}", use_column_width=True)

            st.success(f"Image saved to: {file_path}")

# Display previously generated images
if st.checkbox("Show Generated Images History"):
    st.subheader("Generated Images")
    images = os.listdir(CFG.history_dir)
    if images:
        for img_file in sorted(images, reverse=True):
            img_path = os.path.join(CFG.history_dir, img_file)
            st.image(Image.open(img_path), caption=img_file, use_column_width=True)
    else:
        st.write("No images generated yet.")

