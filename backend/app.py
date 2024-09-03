from flask import Flask, request, jsonify
#from services.image_processing import process_images
#from services.prompt_engineer import generate_prompt
from Gemini import process_multimodal_input
import logging
from utils.logger import setup_logger
from PIL import Image
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS  # Import CORS

# Intialiazige flask app

app = Flask(__name__)

# Set up CORS
CORS(app)

#Setup logging
logger = setup_logger()

UPLOAD_FOLDER = 'uploaded_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# APi route for feature description
@app.route('/describe', methods=['POST'])

def describe_features():
    """Extract images and optional text content from the request"""
    try:
        # Check if the request contains files
        if 'images' not in request.files:
            logger.error("No images found in the request.")
            return jsonify({"error": "No images found in the request."}), 400
        
        images = request.files.getlist("images")
        context = request.form.get("context", "")
        print('Done!')

        # Validate image files
        if not images:
            logger.error("No image files uploaded.")
            return jsonify({"error": "No image files uploaded."}), 400
        
        image_paths = []
        for image in images:
            if image and image.filename:
                # Secure the filename and save the image
                filename = secure_filename(image.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                image.save(file_path)

                # Open image with PIL for processing
                try:
                    img = Image.open(file_path)
                    img.save(file_path)  
                    image_paths.append(file_path)
                    print(image_paths)
                except Exception as img_error:
                    logger.error(f"Image processing error: {img_error}")
                    return jsonify({"error": "Image processing error."}), 500
            else:
                logger.error("Invalid image file.")
                return jsonify({"error": "Invalid image file."}), 400




        #Call the multimodal LLM integration
    
        llm_response_text = process_multimodal_input(image_paths, context)

        # Return the LLM response
        llm_response = {"description": llm_response_text}
        return jsonify(llm_response), 200
    
    except Exception as e:
        logger.error(f" Error in describe featres : {e}")
        return jsonify({"error": "An error occurred during processing"}), 500

if __name__ == '__main__':
    app.run(debug=True)
    
        