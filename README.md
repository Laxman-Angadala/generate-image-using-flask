# generate_image_using_flask


# Flask Image Generator

This is a simple Flask application that generates an image of a specified size and color in the format of your choice.

## Installation

1. Clone the repository:

git clone

https://github.com/Laxmantech/generate_image_using_flask


2. Install the required packages:

pip install -r requirements.txt


## Usage

1. Start the Flask server:

python app.py


2. Open your web browser and go to http://localhost:5000/generate_image/<width>/<height>/<color>/<format>

- Replace <width> with the desired width of the image (in pixels).
- Replace <height> with the desired height of the image (in pixels).
- Replace <color> with one of the following colors: red, green, blue.
- Replace <format> with one of the following formats: jpeg, png, gif.

Example usage: http://localhost:5000/generate_image/500/300/green/jpeg
