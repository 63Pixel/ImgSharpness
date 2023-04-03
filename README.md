# ImgSharness
A tool that calculates the sharpness of an image. The result will be exported in a text and csv file.

The results looks like:

Result of the quality check:

Sharpness: [ 393.04 ]
--> which is: Blurry

Explanation:
0 - 300: Very Blurry
301 - 399: Blurry
400 - 499: Okay
500 - 649: Sharp
650 - 749: Crispy
750 - above: Very Crispy 

The sharpness value is calculated using the standard deviation of the gradient magnitude calculated by Sobel filters. 
The sharpness is calculated as the average value of the gradient magnitude. A higher gradient magnitude means higher sharpness.
