from flask import Flask, make_response
from io import BytesIO
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/generate_image/<int:width>/<int:height>/<string:color>/<string:format>')
def generate_image(width, height, color, format):
    # Check if color is valid
    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}
    if color not in colors:
        return 'Invalid color', 400
    
    # Create a NumPy array of the specified size and fill it with the specified color
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    img_array[:, :] = colors[color]
    
    # Create a Pillow image from the NumPy array
    img = Image.fromarray(img_array)
    
    # Return the image as a response with the appropriate MIME type
    if format == 'jpeg':
        bytes_io = BytesIO()
        img.convert('RGB').save(bytes_io, 'JPEG')
        response = make_response(bytes_io.getvalue())
        response.headers.set('Content-Type', 'image/jpeg')
    elif format == 'png':
        bytes_io = BytesIO()
        img.save(bytes_io, 'PNG')
        response = make_response(bytes_io.getvalue())
        response.headers.set('Content-Type', 'image/png')
    elif format == 'gif':
        bytes_io = BytesIO()
        img.save(bytes_io, 'GIF')
        response = make_response(bytes_io.getvalue())
        response.headers.set('Content-Type', 'image/gif')
    else:
        return 'Invalid format', 400
    
    return response


if __name__ == '__main__':
    app.run(debug=True)
