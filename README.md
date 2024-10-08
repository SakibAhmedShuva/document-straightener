# Document Straightener

A Python script for straightening scanned document images using OpenCV. The script detects the skew angle of the document and corrects it.

## Features

- Loads an image from a file.
- Auto Preprocesses the image by converting it to grayscale, applying Gaussian blur, and detecting edges.
- Calculates the rotation angle using the Hough Line Transform.
- Auto rotates the image to correct the skew.
- Save the straightened image to a specified path.

## Screenshots:
**Input:**

![input](https://github.com/SakibAhmedShuva/tiny-document-straightener/assets/126283947/83303005-dcc6-47c5-b963-5fbabfabfa94)

**Output:**

![output](https://github.com/SakibAhmedShuva/tiny-document-straightener/assets/126283947/7160cfe8-dca5-4692-93fc-21f733e5d976)

## I have Used:
- Python 3.12.4
- numpy==2.0.0
- opencv_python==4.10.0.82
- opencv_python_headless==4.10.0.82

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/SakibAhmedShuva/tiny-document-straightener
   
2. Open the folder

   ```sh
   cd tiny-document-straightener

2. Install the required packages:

    ```sh
    pip install -r requirements.txt

3. Run the script
   
    ```sh
    straighten_document('input_filename.jpg', 'output_filename.jpg')

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
