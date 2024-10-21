from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image
from ai_image_finder import analyze_image 


def test_image_folder(folder_path, label, actual_label, predictions, expected_labels):
    """
    Test all images in the folder, output the confidence score, 
    and add the result to predictions and expected_labels.
    """
    # Loop through all files in the directory
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Open image
                img = Image.open(file_path)
                
                # Analyze the image and get the confidence result
                result = analyze_image(img)
                
                # Check if the result contains "AI" or "Real"
                predicted_label = "AI Image" if "AI Generated" in result else "Real Image"
                
                # Output the result with filename
                print(f"{label} - {filename}: {result}")
                
                # Store predictions and actual labels
                predictions.append(predicted_label)
                expected_labels.append(actual_label)
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")


def run_tests():
    """Run the tests for both AI-generated and Real images, and plot confusion matrix."""
    # Paths to the test folders
    ai_folder = "archive/test/FAKE"
    real_folder = "archive/test/REAL"
    
    predictions = []
    expected_labels = []
    
    # Testing AI-generated images
    print("Testing AI-generated images:")
    test_image_folder(ai_folder, "AI Image", "AI Image", predictions, expected_labels)
    
    # Testing Real images
    print("\nTesting Real images:")
    test_image_folder(real_folder, "Real Image", "Real Image", predictions, expected_labels)
    
    # Generate the confusion matrix
    cm = confusion_matrix(expected_labels, predictions, labels=["AI Image", "Real Image"])
    plot_confusion_matrix(cm, ["AI Image", "Real Image"])


def plot_confusion_matrix(cm, labels):
    """Plot the confusion matrix using seaborn."""
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

# Run the test
run_tests()

