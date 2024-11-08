# Text to Matrix Image Generator

This project converts a given text string into a visual matrix representation, normalizes the values row by row, and creates an enlarged, grayscale image of the matrix.

## Overview

The script performs the following steps:
1. **Text to Matrix Conversion**: Converts each character in the input text to its ASCII value (mapped to a range from 0 to 255) and arranges it into a square matrix.
2. **Row Normalization**: Normalizes the values in each row separately, scaling them to a range from 0 to 255.
3. **Matrix Enlargement**: Enlarges the matrix by creating pixel blocks, making the generated pattern more visually apparent.
4. **Image Creation**: Converts the enlarged matrix to an image and saves it in grayscale.

## Installation

Make sure you have the necessary libraries:
```bash
pip install numpy pillow
```

## Usage

Edit the `input_text` variable in the script to your desired input text. Then, run the script:
```python
python your_script_name.py
```

This will generate an image named `normalized_peak_matrix_image.png`.

## Functions

### 1. `text_to_matrix(text)`
Converts the input text into a matrix where each character's ASCII value is mapped to a range of 0-255.

- **Parameters**: `text` (str) - The input text to be converted.
- **Returns**: A 2D numpy array representing the mapped ASCII values.

### 2. `normalize_rows(matrix)`
Normalizes each row of the matrix separately, scaling values to 0-255.

- **Parameters**: `matrix` (2D numpy array) - The matrix to normalize.
- **Returns**: A normalized 2D numpy array of type `uint8`.

### 3. `enlarge_matrix(matrix, block_size=10)`
Expands the matrix by creating larger blocks of each matrix cell, enhancing the visual effect.

- **Parameters**: 
  - `matrix` (2D numpy array) - The matrix to enlarge.
  - `block_size` (int) - The size of each enlarged block.
- **Returns**: An enlarged 2D numpy array of type `uint8`.

## Example

```python
input_text = "Adventure, a journey unfolds. Mountain, of rivers flow..."
matrix = text_to_matrix(input_text)
normalized_matrix = normalize_rows(matrix)
image_matrix = enlarge_matrix(normalized_matrix)
```
