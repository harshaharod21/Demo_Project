
import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.logger import setup_logger
from flask import Flask, request, jsonify


# Initialize logger
logger = setup_logger()

# Configuring the API Key for Google Generative AI (Make sure this is set in your environment variables)
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    raise ValueError("Google API Key not found. Please set the 'GOOGLE_API_KEY' environment variable.")

# Configuring the Google Generative AI API
genai.configure(api_key=GOOGLE_API_KEY)

def upload_image(image_path, display_name):
    """
    Uploads an image to Google Generative AI and returns the file reference.
    
    :param image_path: The path to the image file to upload.
    :param display_name: A display name for the uploaded image.
    :return: The uploaded file reference.
    """
    try:
        sample_file = genai.upload_file(path=image_path, display_name=display_name)
        logger.info(f"Uploaded file: {display_name}")
        return sample_file
    except Exception as e:
        logger.error(f"Error uploading file {display_name}: {e}")
        raise

def generate_response_from_images(images, prompt):
    """
    Generates a response using the Gemini model based on the uploaded images and prompt.
    
    :param images: List of image file references.
    :param prompt: The text prompt to guide the generation.
    :return: The generated response text.
    """
    
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        response = model.generate_content([prompt] + images)
        logger.info("Generated response from Gemini model.")
        return response.text
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise

def process_multimodal_input(images, context=""):
    """
    Handles the process of uploading images and generating a response from the LLM.
    
    :param images: List of image paths to upload.
    :param context: Optional context to include in the prompt.
    :return: The generated response.
    """
    try:
        uploaded_images = [upload_image(image, f"Uploaded Image {i+1}") for i, image in enumerate(images)]
        print("Done uploading images")
        prompt = f"""First identify features in these screenshots and provide a brief description.
         Understand what each specific tab and section does according to a user who can use that feature.Guide them on how they can use it.
         If more than one images are uploaded proceed with this explanation given above one by one and then address the user given context.
        These examples are for your understanding how to approach according to what is given in User given context in the bottom :
          Note: Dont output "User given context" and "Output" strictly
          
          Example 1:
          user given context: Explain to me how can I find my bookings ?
          Output : The bookings tab is located to the right of home tab in the bottom section. Please find your bookings there and more information select help tab.

          Example 2:
          User given context: How can I change my personal information?
          Output: Find the My Account tab in the bottom section.This can help you in changing you personal information.Provide me with the screenshot of My Account tab so that I can assist further.

          User given context: {context}"""
        response = generate_response_from_images(uploaded_images, prompt)
        return response
    except Exception as e:
        logger.error(f"Error processing multimodal input: {e}")
        return jsonify({"error": "An error occurred during uploading images"}), 500

        raise

