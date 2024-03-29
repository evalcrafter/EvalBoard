# EvalBoard 🎥📊

EvalBoard is a web application built using Gradio that displays a gallery of videos generated by various methods. It allows users to navigate through the gallery, view videos, and read associated captions. 
![AI-Created Video Gallery](https://github.com/evalcrafter/EvalCrafter/blob/master/Gallery.gif)


## Installation

To run EvalBoard locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/evalcrafter/EvalBoard
   ```

2. Navigate to the project directory:

   ```
   cd EvalBoard
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Data Preparation

Before running the EvalBoard application, you need to prepare the video data by following these steps:

1. Create a directory named `static` in the project root if it doesn't already exist.

2. Inside the `static` directory, create subdirectories for each category of videos. The category names are specified in the `showcase` function in the `EvalBoard.py` file. You can also replace the current names with yours.

3. Place the video files in their respective category subdirectories. The videos should be named using a four-digit index followed by the `.mp4` extension. For example, the first video for the category `VideoCrafter2` should be named `0000.mp4`, the second video should be named `0001.mp4`, and so on. Default to have 700 videos.

4. Place the prompts files corresponding to video names in `prompts`, using the same name with `.txt` extension. You may delete the current files first.

## Usage

To start EvalBoard, execute the following command within the project directory:

```
python app.py
```

Once the application is running, open your web browser and visit `http://localhost:8000` to access EvalBoard.

Upon launching EvalBoard, you will see a gallery of videos with their associated captions. The application provides several ways to navigate through the gallery:

- **Beginning**: Clicking the "Beginning" button takes you to the first page.
- **Previous**: Clicking the "Previous" button takes you to the previous page.
- **Next**: Clicking the "Next" button takes you to the next page.
- **End**: Clicking the "End" button takes you to the last page.
- **Slider**: You can use the slider to directly navigate to a specific page.

As you navigate through the gallery, the videos and captions will dynamically update to reflect the current page. Simply click on a video to play it within the application.


## Citation
If you find this repository helpful, please consider citing it in your research:

   ```
   @article{liu2023evalcrafter,
  title={Evalcrafter: Benchmarking and evaluating large video generation models},
  author={Liu, Yaofang and Cun, Xiaodong and Liu, Xuebo and Wang, Xintao and Zhang, Yong and Chen, Haoxin and Liu, Yang and Zeng, Tieyong and Chan, Raymond and Shan, Ying},
  journal={arXiv preprint arXiv:2310.11440},
  year={2023}
   }
   ```
