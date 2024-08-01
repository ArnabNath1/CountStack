# CountStack
This Streamlit application counts the number of sheets in a stack from an uploaded image using computer vision techniques.

# Features
Upload an image of a sheet stack.
Count the number of sheets in the stack.
Display the original image, detected lines, and edges.

# Requirements
```
Python 3.6 or higher
streamlit
opencv-python-headless
pillow
numpy
tensorflow
matplotlib
```

# Installation
Clone the repository:

``` https://github.com/ArnabNath1/CountStack.git ```
``` cd CountStack ```

# Create and activate a virtual environment:

``` conda create -p venvs python==3.11 -y ```
``` conda activate venvs/ ```

# Install the required packages:
Put the packages you need to install mentioned above in the requirements.txt file.
Install the packages using the command:
``` pip install -r requirements.txt ```

# Usage
Run the Streamlit app:

``` streamlit run app.py ```

# Interact with the app:

1. Open your browser and go to http://localhost:8501.
2. Upload an image of a stack using the file uploader.
3. Click the "Count Sheets" button to count the number of sheets detected.

# File Structure

1. requirements.txt: Contains all the dependencies to be downloaded.
2. app.py: Main script to run the Streamlit app.
4. README.md: This file.