# ![PyPalette](http://i.imgur.com/QWeYq0i.png) PyPalette

## What is PyPalette?
PyPalette is a collection of tools written in Python for extracting and manipulating colors and color palettes from images. It is currently dependency-free, but can be very easily utilized alongside other libraries such as [Pillow](https://github.com/python-pillow/Pillow).

## Where is PyPalette headed?
The current goal for PyPalette is not very defined. My plan is to incorporate as many different functionalities relating to colors and images as possible. There are so many things that can be done that I feel like going with the wind is the best way currently. Any suggestions are welcome and encouraged!

## What does PyPalette currently do?
1. **Color Space Conversions**
  - [cmyk2rgb](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L4-34)
  - [hex2rgb](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L37-52)
  - [hsl2rgb](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L55-101)
  - [hsv2rgb](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L104-153)
  - [rgb2cmyk](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L156-192)
  - [rgb2hex](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L195-218)
  - [rgb2hsl](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L221-272)
  - [rgb2hsv](https://github.com/adamgrieger/pypalette/blob/master/pypalette/conversions.py#L275-329)
2. **Image Color Analysis**
  - [average_color](https://github.com/adamgrieger/pypalette/blob/master/pypalette/pypalette.py#L5-26)
3. **Color Lists**
  - [CSS3 Color Names](https://github.com/adamgrieger/pypalette/blob/master/pypalette/color_lists.py#L1-157)
  - [Google Material Design Colors](https://github.com/adamgrieger/pypalette/blob/master/pypalette/color_lists.py#L159-438)
4. **Clustering**
  - [*k*-means with *k*-means++ seeding](https://github.com/adamgrieger/pypalette/blob/master/pypalette/kmeans.py#L20-165)

## What are some things on the TO-DO list?
- Clustering
    * More clustering options for choice of accuracy or performance?
- Palettes
    * Palette lists
        * :video_game: Retro video game console palettes
        * :art: Crayola crayon and colored pencil colors
        * :us: Country flags (w/ color percentages)
        * Signature Plastics' ABS and PBT plastic colors
        * Something, something colors (I'll make a color list of fruit indigenous to Jamaica if I am so inclined)
        * ColourLovers support (I believe they have an API)?
    * Palette class for percentage-based color palettes
- Image Processes/Analysis
    * Median color, grayscale, sepia, etc.
    * Dithering and noise
    * Image blending modes
    * "Daltonization" for the color-blind (may require LMS color space)?
- :free: :icecream:

## License
[The MIT License (MIT)](https://github.com/adamgrieger/pypalette/blob/master/LICENSE)
