import cv2
from ultralytics import solutions

# Input video path
video_path = r"D:\pycharm\heatmap\videos and images\istockphoto-1423119278-640_adpp_is.mp4"

# Output video path
output_path = r"D:\pycharm\heatmap\res\output11_heatmap.mp4"

# Open input video
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Initialize heatmap object
heatmap = solutions.Heatmap(
    colormap=cv2.COLORMAP_PARULA,
    show=True,
    model=r"D:\pycharm\learning\yolo11m.pt",
    classes=[0]
)

# Process video frame by frame
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break

    # Generate heatmap
    im0 = heatmap.generate_heatmap(im0)

    # Write frame to output video
    out.write(im0)

    # Show frame (optional)
    cv2.imshow("Heatmap", im0)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()


