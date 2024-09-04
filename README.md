# Demo_Project
Demo project

The screenshots are uploaded in the screeshots folder.

Note:
- Install Node.js to get npm

# Project Setup Instructions

This guide will help you set up and run the project, including both the backend and frontend components.

## Prerequisites
- Python 3.10
- Node.js and npm
- Git Bash (for Windows users)

## 1. Create and Activate a Virtual Environment

1. **Create the virtual environment:**

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment:**
   - On Windows:
   
     ```bash
     venv\Scripts\activate
     ```
  
## 2. Setup and Run the Backend

1. **Move to the backend directory:**

    ```bash
    cd backend
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure that the virtual environment is activated.**

4. **Open a new Git Bash terminal:**
   - Navigate to the backend directory:
   
     ```bash
     cd backend
     ```

5. **Set the environment variables:**
   - On Windows:
   
     ```bash
     set FLASK_APP=app
     set FLASK_ENV=development
     ```
   
6. **Run the Flask application:**

    ```bash
    flask run
    ```

## 3. Open new Git Bash terminal and run the Frontend

1. **Move to the frontend directory:**

    ```bash
    cd ../frontend
    ```

2. **Install the required npm packages:**

    ```bash
    npm install
    ```

3. **Install the `markdown-to-jsx` package:**

    ```bash
    npm install markdown-to-jsx
    ```
This to avoid symbols like '*' that gets parsed during inferencing from LLM model

4. **Start the React frontend application:**

    ```bash
    npm start
    ```

## 4. Access the Application

- **Backend:** The Flask server should be running on `http://127.0.0.1:5000`.
- **Frontend:** The React application should be accessible via `http://localhost:3000`.

## Troubleshooting

- Ensure all environment variables are correctly set.
- Make sure the correct Python version and Node.js version are installed.
- If you encounter any issues, ensure your virtual environment is activated, and all dependencies are installed properly.



## Prompting Strategies

The following prompting strategies have been employed to guide the multimodal LLM in describing features based on screenshots:

### Prompt Template

```text
First, identify features in these screenshots and provide a brief description. Understand what each specific tab and section does according to a user who can use that feature. Guide them on how they can use it. If more than one image is uploaded, proceed with this explanation one by one and then address the user-provided context.

Note: Do not output "User given context" and "Output" strictly.

Examples for your understanding:

Example 1:
- User given context: Explain to me how can I find my bookings?
- Output: The bookings tab is located to the right of the home tab in the bottom section. Please find your bookings there and for more information, select the help tab.

Example 2:
- User given context: How can I change my personal information?
- Output: Find the My Account tab in the bottom section. This can help you in changing your personal information. Provide me with the screenshot of the My Account tab so that I can assist further.

User given context: {context}
```


## Explanation

To guide the multimodal LLM in describing features from screenshots, we use the following prompting strategy:

1. **Feature Identification**: The model is asked to identify and describe features in the provided screenshots.

2. **User Guidance**: It explains how each feature can be used from a user's perspective.

3. **Handling Multiple Images**: For multiple images, the model processes each one sequentially and then addresses any additional user-provided context.

4. **Contextual Relevance**: The prompt incorporates user-provided context to tailor the explanation to specific questions or needs.


Link of Project Demo:
https://www.loom.com/share/9d9d948a02a741c087444a2f6d30018f


