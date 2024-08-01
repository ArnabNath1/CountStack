import streamlit as st
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_file):
    img = Image.open(image_file)
    return img

def count_sheets(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Edge detection using Canny
    edges = cv2.Canny(blurred_image, 50, 150)

    # Line detection using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

    # Draw detected lines on the original image
    line_image = np.copy(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Count the number of detected lines
    num_lines = len(lines) if lines is not None else 0
    return num_lines, line_image, edges

st.title("Sheet Stack Counter")

image_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    image = load_image(image_file)
    image = np.array(image)

    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Count Sheets'):
        num_sheets, line_image, edges = count_sheets(image)

        st.write(f"Number of sheets detected: {num_sheets}")
        st.image(line_image, caption='Detected Lines', use_column_width=True)
        st.image(edges, caption='Edges', use_column_width=True)