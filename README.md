### Intro
This project's goal was to verify the claim made in Corridor Digital's video about AI images. My understanding of their claim is that AI images are generated from noise and thus their colors will average out to near grey. Whereas real images will not normally average out to grey. 
 
Original Video: https://www.youtube.com/watch?v=NsM7nqvDNJI

Short Version: https://www.youtube.com/shorts/rr1ZH7hi35Q

### Algorithm for Calculating Average Pixel Value and Confidence

1. **Calculate the Average Pixel Value**:

   \[
   \text{avg\_pixel\_value} = \frac{1}{N} \sum_{i=1}^{N} \text{img\_array}[i]
   \]

   Where \( N \) is the total number of pixels in the image.

2. **Convert the Average Pixel Value to a Percentage (0-100)**:

   \[
   \text{avg\_percentage} = \left( \frac{\text{avg\_pixel\_value}}{255} \right) \times 100
   \]

3. **Calculate Confidence**:

   \[
   \text{confidence} = \max \left( 0, 100 - 2 \times \left| \text{avg\_percentage} - 50 \right| \right)
   \]

This algorithm computes the average pixel value, scales it to a percentage, and calculates a confidence score based on its proximity to 50%.


### Results

The algorithm makes a real/ai classification based on the confidence level from above. Here are the results from a few notable confidence levels.

--------------------------------------------------------------
With a confidence threshold of 70%

![image](https://github.com/user-attachments/assets/1095b387-2cea-4745-807b-ef9ecf3e45ef)

--------------------------------------------------------------
--------------------------------------------------------------
With a confidence threshold of 90%

![image](https://github.com/user-attachments/assets/51bc97d7-a904-4c22-81a5-d491edc00a52)

--------------------------------------------------------------
--------------------------------------------------------------
With a confidence threshold of 80%

![image](https://github.com/user-attachments/assets/414e019c-d593-4222-a381-9fefc6cc0e3b)


--------------------------------------------------------------
--------------------------------------------------------------

With a confidence threshold of 82,5%

![image](https://github.com/user-attachments/assets/6adb69a7-e15f-4c3b-90af-b589657c526e)


--------------------------------------------------------------

### Cnclusion

I don't think that my interpretation of Corridor Digital's claims are sufficient to detect AI images. Of course the greyscale test is only a partial tell when determining AI images, it seems to do no better than a coin flip in its best case scenario. AI images may very well start from a noise that averages out to grey between the lights and darks. However, this changes depending on what kind of images is generated. Of course some image prompts result in an images with more darks than lights and visa versa. For example an image of a black gorilla couch will have more dark pixels than light pixels due to there being all that black in the couch itself. (see screenshot)

![image](https://github.com/user-attachments/assets/14b6bb8f-761e-446e-9621-4e38b0bcc47d)

Perhaps there is a way to account for the overall brightness of the image, or a better way to determine a saturation level, But given that many real photos are edited with color filters to make them more appealing, the difference between AI generated and edited real photo is likely quite small based on these metrics. 

### Potential Areas for Improvement

1. **Brightness and Contrast Adjustments:**  
   To account for the overall brightness and contrast of an image, a more sophisticated analysis might involve normalizing the brightness levels before performing the greyscale test. This could help mitigate the effects of inherently light or dark images (whether real or AI).

2. **Saturation and Color Analysis:**  
   Investigating the saturation levels or color distribution could provide more insight. Since AI-generated images often contain unusually vibrant or flat colors, analyzing the variance in color saturation might help refine the distinction between AI and real images.

3. **Texture and Detail Analysis:**  
   AI images often struggle with fine textures or irregular details (e.g., human hands or complex objects), which could be another potential avenue for distinguishing them from real photos. Integrating texture analysis techniques, such as edge detection or frequency domain analysis, could provide additional clues.

4. **Contextual Awareness:**  
   Understanding the context in which the image was generated could also aid in improving the algorithm. Real-world photos have subtle imperfections or inconsistencies in lighting and shadows, while AI-generated images tend to follow patterns and symmetries.

5. **Training on Larger Datasets:**  
   Training machine learning models on large datasets of both AI-generated and real images may improve classification performance. This would allow the model to learn subtle cues that the current algorithm might miss, especially when dealing with edge cases like heavily edited or filtered real images.

### Conclusion Revisited

In summary, while the current method offers an interesting perspective on distinguishing AI images, it's clear that relying solely on average pixel values and confidence levels is not enough. The similarities between real and AI-generated images, particularly after post-processing, make it difficult to draw reliable conclusions using this technique alone. However, by expanding the approach to include brightness normalization, color analysis, texture detection, and perhaps leveraging machine learning, a more robust solution could be developed. Though, perhaps I have misunderstandings about Corridor Digital's claims.
