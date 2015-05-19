# ![PyPalette](http://i.imgur.com/QWeYq0i.png) PyPalette

## What is the goal of PyPalette?
The current goal for PyPalette is not very defined. My plan is to incorporate as many different functionalities relating to colors and images as possible. There are so many things that can be done that I feel like going with the wind is the best way currently. Any suggestions are welcome and encouraged!

## What does PyPalette currently do?
1. **Color Space Conversions**
  - RGB <=> CMYK
  - RGB <=> Hex
  - RGB <=> HSL
  - RGB <=> HSV
2. **Image Color Analysis**
  - Average color

## What are some things on the TODO list?
- Add HSI conversions back in if they stop being more temperamental than a sugar-high four-year-old
- Clustering
    * Optimizing K-means if possible
    * Median-cut?
    * k-d trees?
- Documentation / Testing
    * Thoroughly document ALL THE THINGS
    * Make unit tests for ALL THE THINGS
- Palettes
    * Palette lists
        * Retro consoles
        * Crayon colors
        * Country flags
        * ABS and PBT plastic colors
        * Something, something colors (I'll make a color list of fruit indigenous to Jamaica if I am so inclined)
        * ColourLovers support?
    * Palette class for palette creation
- Image Processes/Analysis
    * Median color, grayscale, sepia, etc.
    * Dithering and noise
    * Image blending
    * "Daltonization" for the color-blind?

## License
    The MIT License (MIT)

    Copyright (c) 2015 Adam Grieger

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
