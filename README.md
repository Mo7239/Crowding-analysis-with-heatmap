
# Heatmap Generation for Video

This Python project generates a heatmap for an input video using a pre-trained model and displays the results frame by frame. The heatmap is then saved as an output video. The heatmap generation is done using the `solutions.Heatmap` class, which utilizes the YOLO model to detect objects and visualize them with heatmap overlays.

## Features

- **Heatmap Visualization**: Generates and overlays heatmaps on each frame of the input video.
- **YOLO Object Detection**: Utilizes the YOLO model (`yolo11m.pt`) for real-time object detection.
- **Real-time Frame Processing**: Processes the video frame by frame and displays the heatmap in real-time.
- **Customizable Output**: Saves the processed video with heatmap visualizations as an `.mp4` file.
- **Interactive Display**: Displays each frame with the overlayed heatmap in a window. Press 'q' to exit.
- **Configurable Model and Classes**: You can specify your own YOLO model and detection classes for the heatmap.
- **Colormap Selection**: Uses `cv2.COLORMAP_PARULA`, but this can be adjusted to other colormaps as needed.

## Prerequisites

- Python 3.x
- OpenCV (`opencv-python` and `opencv-python-headless`)
- YOLO pre-trained model (`yolo11m.pt`)
- `solutions` module for heatmap generation

## Installation

1. Install required Python packages:

    ```bash
    pip install opencv-python opencv-python-headless
    ```

2. Ensure the pre-trained model (`yolo11m.pt`) is accessible at the provided path.

## Code Description

```python
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
```

## How to Run

1. Make sure the input video file is specified correctly by updating the `video_path` variable.
2. Ensure that the model file (`yolo11m.pt`) is available in the specified location.
3. Run the Python script:
   
    ```bash
    python heatmap_video.py
    ```

4. The script will read the video, generate a heatmap for each frame, and output a video with the heatmap overlay in the specified output path (`output11_heatmap.mp4`).

5. The script also displays the processed frames in a window titled "Heatmap". Press 'q' to stop the process and close the window.

## Output

- The output video is saved in `.mp4` format with heatmap visualizations.
- The output path is specified in the `output_path` variable.

## Notes

- The heatmap is generated using the YOLO model for object detection, and the model file should be compatible with the code.
- You can adjust the colormap and other settings in the `Heatmap` initialization as needed.
- To modify the classes for detection, change the `classes` argument in the `solutions.Heatmap` initialization.

## 📬 Contact  
For any inquiries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/mohamed-wasef-789743233/)
