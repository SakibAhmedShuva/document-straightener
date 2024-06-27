import cv2
import numpy as np

def load_image(path):
    return cv2.imread(path)

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    return edges

def get_rotation_angle(edges):
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    angles = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            angle = np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi
            angles.append(angle)
    median_angle = np.median(angles)
    return median_angle

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Calculate the new bounding dimensions of the image
    abs_cos = abs(np.cos(np.radians(angle)))
    abs_sin = abs(np.sin(np.radians(angle)))
    bound_w = int(h * abs_sin + w * abs_cos)
    bound_h = int(h * abs_cos + w * abs_sin)

    # Adjust the rotation matrix to take into account the translation
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    M[0, 2] += (bound_w / 2) - center[0]
    M[1, 2] += (bound_h / 2) - center[1]

    # Perform the actual rotation and return the image
    rotated = cv2.warpAffine(image, M, (bound_w, bound_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def straighten_document(image_path, output_path):
    image = load_image(image_path)
    edges = preprocess_image(image)
    angle = get_rotation_angle(edges)
    rotated_image = rotate_image(image, angle)
    cv2.imwrite(output_path, rotated_image)
    print(f"Document straightened and saved to {output_path}")