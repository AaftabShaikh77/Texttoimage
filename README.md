Text-to-Image Generator
This repository contains a Text-to-Image Generator powered by the Stable Diffusion model. With this tool, you can generate stunning images from descriptive text prompts using a user-friendly Streamlit interface.

Features
🎨 Generate high-quality images from text prompts.
⚡ Powered by Stable Diffusion 2 for state-of-the-art results.
💾 Save generated images locally with automatic timestamping.
🖼️ View and manage your image generation history.
🌐 Easy-to-use web interface built with Streamlit.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/text-to-image-generator.git
cd text-to-image-generator
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Authenticate with Hugging Face:

Replace the use_auth_token value in the text2image.py file with your personal Hugging Face token. You can get one here.
Run the Streamlit app:

bash
Copy code
streamlit run text2image.py
Usage
Open the app in your browser at http://localhost:8501.
Enter a text prompt (e.g., "A futuristic cityscape at sunset").
Click Generate Image to create a unique image.
Optionally, view previously generated images by selecting Show Generated Images History.
Configuration
Model ID: Stable Diffusion 2 (stabilityai/stable-diffusion-2)
Image Size: 400 x 400 pixels (modifiable in the CFG class).
Device: Automatically detects GPU (cuda) or CPU.
Output Directory: Saved images are stored in the ./generated_images folder.
Requirements
Python 3.7 or higher
Hugging Face Diffusers library
Streamlit
Torch
PIL (Pillow)
Refer to the requirements.txt file for the full list of dependencies.
