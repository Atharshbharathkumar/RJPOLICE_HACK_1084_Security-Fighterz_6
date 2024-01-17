from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("conect.pt")  # Load the YOLOv8s model

results_generator = model.predict(source=0, show=True, stream=False)

people_count = 0  # Variable to keep track of the number of people
color_tracker = {}  # Dictionary to track colors of each person

def get_average_color(image, box):
    # Extract the region of interest (ROI) for the given bounding box
    roi = image[box[1]:box[3], box[0]:box[2]]

    # Calculate the average color in the ROI
    average_color = np.mean(roi, axis=(0, 1))

    return average_color

for results in results_generator:
    boxes = results.boxes  # Get the bounding boxes for all detections
    class_ids = results.class_ids  # Get the class IDs for each bounding box
    probs = results.probs  # Get the probabilities for each class
    frame = results.render()[0]  # Get the rendered frame for visualization

    for i, box in enumerate(boxes):
        # Filter for person detections only
        if model.names[class_ids[i]] == "person":
            # Process the person detection (optional)
            # You can do additional processing on the person_boxes and person_probs here,
            # such as filtering by probability threshold, drawing boxes on frames, etc.

            # Count the number of people in the current frame
            people_count += 1

            # Get the average color of the person's clothing
            average_color = get_average_color(frame, box)

            # Convert the average color to a tuple of integers
            average_color = tuple(map(int, average_color))

            # Print the average color (BGR format)
            print(f"Person {people_count} Color (BGR): {average_color}")

            # Update the color tracker with the person's ID and average color
            color_tracker[people_count] = average_color

    # Display the current frame with person detections (optional)
    model.show()

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Print the total number of people detected
print(f"Total People Count: {people_count}")

# Print the colors associated with each person
print("Color Tracker:")
for person_id, color in color_tracker.items():
    print(f"Person {person_id} Color (BGR): {color}")

# Release resources
cv2.destroyAllWindows()
