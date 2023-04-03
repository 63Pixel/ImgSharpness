import cv2
import numpy as np
import os
import csv

def estimate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sharpness = np.mean(magnitude)
    return sharpness

def write_sharpness_csv(image_path, sharpness, csv_writer):
    # Write the sharpness value to the CSV file
    basename = os.path.splitext(os.path.basename(image_path))[0]
    csv_writer.writerow([basename, sharpness])

def write_sharpness_text(image_path, sharpness):
    # Write the sharpness value and explanation to a text file
    basename = os.path.splitext(os.path.basename(image_path))[0]
    result_path = os.path.join(os.getcwd(), f"{basename}_sharpness.txt")
    with open(result_path, 'w') as f:
        explanation = ""
        if sharpness < 300:
            explanation = "Very Blurry"
        if sharpness >= 300 and sharpness < 400:
            explanation = "Blurry"
        elif sharpness >= 400 and sharpness < 500:
            explanation = "Okay"
        elif sharpness >= 500 and sharpness < 650:
            explanation = "Sharp"
        elif sharpness >= 650 and sharpness < 750:
            explanation = "Crispy"
        elif sharpness >= 750:
            explanation = "Very Crispy"
        f.write(f"Result of the quality check:\n\nSharpness: [ {sharpness:.2f} ]\n--> which is: {explanation}\n\nExplanation:\n0 - 300: Very Blurry\n301 - 399: Blurry\n400 - 499: Okay\n500 - 649: Sharp\n650 - 749: Crispy\n750 - above: Very Crispy \n\nThe sharpness value is calculated using the standard deviation of the gradient magnitude calculated by Sobel filters. The sharpness is calculated as the average value of the gradient magnitude. A higher gradient magnitude means higher sharpness.")


def write_sharpness_on_image(image_path, sharpness):
    # Load the image
    image = cv2.imread(image_path)

    # Add the sharpness value to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottom_left_corner = (70, 130)
    font_scale = 3
    font_color = (0, 255, 0) # green
    thickness = 3
    text = f"Sharpness: {sharpness:.2f}"
    cv2.putText(image, text, bottom_left_corner, font, font_scale, font_color, thickness)

    # Add the explanation text to the image
    explanation = ""
    if sharpness < 300:
        explanation = "Very Blurry"
    if sharpness >= 300 and sharpness < 400:
        explanation = "Blurry"
    elif sharpness >= 400 and sharpness < 500:
        explanation = "Okay"
    elif sharpness >= 500 and sharpness < 650:
        explanation = "Sharp"
    elif sharpness >= 650 and sharpness < 750:
        explanation = "Crispy"
    elif sharpness >= 750:
        explanation = "Very Crispy"
    bottom_left_corner = (1000, 130)
    text = f"({explanation})"
    cv2.putText(image, text, bottom_left_corner, font, font_scale, font_color, thickness)

    # Save the image with the sharpness value and explanation
    basename = os.path.splitext(os.path.basename(image_path))[0]
    result_path = os.path.join(os.getcwd(), f"{basename}_sharpness.jpg")
    cv2.imwrite(result_path, image)

# Process all image files in the current directory
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
csv_path = os.path.join(os.getcwd(), "sharpness.csv")
with open(csv_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Image', 'Sharpness'])

    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(image_extensions):
            image_path = os.path.join(os.getcwd(), file)
            sharpness = estimate_sharpness(cv2.imread(image_path))
            write_sharpness_csv(image_path, sharpness, csv_writer)
            write_sharpness_text(image_path, sharpness)
