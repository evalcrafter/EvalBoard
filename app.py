import gradio as gr
import os

css = """
<style>
body, html {
    margin: 0;
    padding: 0;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #121212; /* Dark background for the body */
    color: #e0e0e0; /* Light grey text for better readability */
    height: 100%;
    width: 100%;
}


.gallery-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    padding: 2rem;
    box-sizing: border-box;
}

.video-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
    padding: 1rem;
    width: 100%;
    max-width: 1200px;
}

.video-item {
    padding-top: 0;
    margin-bottom: 1rem;
}

.video-item video {
    width: 100%;
    display: block;
    border-radius: 8px;
}

.video-caption {
    color: #121212; /* Maintain white text for captions */
    padding: 0.5rem;
    border-radius: 4px;
    margin-top: 0.5rem;
    font-size: 0.9rem;
    display: block;
    width: auto;
}

.nav-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1rem;
}

.button {
    background-color: #333333; /* Dark grey button background */
    color: #ffffff; /* White text on buttons for visibility */
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.3rem;
    cursor: pointer;
    transition: background 0.2s ease-in-out;
}

.gr-button {
    background-color: #e5e7eb !important;
}

.button:hover {
    background-color: #4f4f4f; /* Lighter grey on hover for visibility */
}

.slider {
    background-color: #333333; /* Slider background */
    border-radius: 0.3rem;
    margin: 1rem 0;
}

.slider input[type="range"] {
    width: 100%;
}

a, a:visited {
    color: #76a9ff; /* Blue accent color for links for visibility */
    text-decoration: none;
}

a:hover {
    color: #a4c2ff; /* Lighter blue on hover for visibility */
}

input[type="text"], select, textarea {
    background-color: #333333; /* Dark grey input background for contrast */
    color: #e0e0e0; /* White text for inputs */
    border: 1px solid #343434; /* Subtle border color */
    border-radius: 0.3rem;
    padding: 0.5rem;
}

input[type="text"]:focus, select:focus, textarea:focus {
    outline: none;
    border-color: #76a9ff; /* Blue border color for focus */
}

/* Additional global styles can go here */

</style>
"""

js = """
<script>
function addMotionBackgrounds() {
    // Select all video containers
    var containers = document.querySelectorAll('.video-container');
    
    containers.forEach(container => {
        // Create a div for the background
        var background = document.createElement('div');
        background.className = 'video-background';
        
        // Append the background div to the container
        container.appendChild(background);
    });
}
// Call the function to add motion backgrounds
window.onload = addMotionBackgrounds;
</script>
"""


def video_to_base64(video_path):
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode('utf-8')

def showcase(page_num):
    videos_per_page = 1
    start_index = (page_num - 1) * videos_per_page
    end_index = start_index + videos_per_page
    video_html = "<div class='gallery-container'>"

    for i in range(start_index, end_index):
        video_name = f"{i:04d}.mp4"
        caption_name = f"{i:04d}.txt"
        video_html += "<div class='video-container'>"

        for category in [ 'VideoCrafter2','Pika','VideoCrafter1','VideoCrafter0.9','Pika1.0', 'Gen2-09.2023','Gen2-12.2023','HotShot','Lavie-Base','Lavie-Interpolation','ModelScope','MoonValley','Show1', 'ZeroScope']:
            video_url = f"http://localhost:8000/{category}/{video_name}"
            caption_path = os.path.join('prompts', caption_name)
            if os.path.exists(os.path.join('static', category, video_name)):
                caption_text = ""
                if os.path.exists(caption_path):
                    with open(caption_path, 'r') as file:
                        caption_text = file.read().strip()

                video_html += f"""
                <div class='video-item'>
                    <video controls>
                        <source src="{video_url}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    <p class='video-caption'>{category}: {caption_text}</p>
                </div>
                """

        video_html += "</div>"
    video_html += "</div>"
    return video_html


# Description and Acknowledgements    

description_html = """
<div style="text-align: center; margin-bottom: 20px;">
    <h2>EvalCrafter Text-to-Video (ECTV) Gallery 🎥📊</h2>
    <p>
    <a href="https://huggingface.co/datasets/RaphaelLiu/EvalCrafter_T2V_Dataset">Dataset</a> ·
    <a href="https://github.com/EvalCrafter/EvalCrafter">Code</a> · 
    <a href="http://evalcrafter.github.io">Project Page</a> · 
    <a href="https://huggingface.co/spaces/AILab-CVC/EvalCrafter">Leaderboard</a> · 
    <a href="https://arxiv.org/abs/2310.11440">Paper@ArXiv</a> · 
    <a href="https://github.com/evalcrafter/EvalCrafter/blob/master/prompt700.txt">Prompt list</a></p>
    <p>Welcome to the ECTV Gallery! This repository contains around 10000 videos generated by various methods using the Prompt list. These videos have been evaluated using the innovative EvalCrafter framework, which assesses generative models across visual, content, and motion qualities using 17 objective metrics and subjective user opinions.</p>
    <!-- Add more details and acknowledgements as needed -->
</div>
"""


def navigate(direction, current_page):
    if direction == "Beginning":
        return 1
    elif direction == "Previous":
        return max(1, current_page - 1)
    elif direction == "Next":
        return min(total_pages, current_page + 1)
    elif direction == "End":
        return total_pages
    else:
        # For direct navigation through the slider
        return current_page

def navigate_to_page(page_num, page_slider):
    # Directly navigate to the selected page from the slider
    page_num.value = page_slider
    return page_num, showcase(page_num)


# Define the total number of pages.
total_videos = 700
videos_per_page = 1
total_pages = (total_videos + videos_per_page - 1) // videos_per_page

with gr.Blocks(css=css)  as app:
    gr.Markdown(description_html)
    gr.Markdown(js)
    page_num = gr.State(value=1)

    with gr.Row():
        beginning_button = gr.Button("Beginning")
        previous_button = gr.Button("Previous")
        next_button = gr.Button("Next")
        end_button = gr.Button("End")
    page_slider = gr.Slider(minimum=1, maximum=total_pages, step=1, value=1, label="Go to page")
    output_html = gr.HTML()
    


    def update_output(direction):
        # new_page_num = navigate(direction, page_num.value)
        if isinstance(direction, int):
            new_page_num = direction
        else:
            new_page_num = navigate(direction, page_num.value)
        page_num.value = new_page_num
        content = showcase(new_page_num)
        return new_page_num, content
    
    def initialization(start):
        page_num.value = int(start)
        return page_num.value, showcase(page_num.value)

    app.load(fn=lambda: initialization('1'), inputs=None, outputs=[page_slider, output_html])
    

    beginning_button.click(fn=lambda: update_output("Beginning"), inputs=None, outputs=[page_slider, output_html])
    previous_button.click(fn=lambda: update_output("Previous"), inputs=None, outputs=[page_slider, output_html])
    next_button.click(fn=lambda: update_output("Next"), inputs=None, outputs=[page_slider, output_html])
    end_button.click(fn=lambda: update_output("End"), inputs=None, outputs=[page_slider, output_html])
    page_slider.change(fn=lambda x: update_output(x), inputs=page_slider, outputs=[page_slider, output_html])

    # Initialize the display for the first page
    output_html.update(value=showcase(page_num.value))

app.launch(share=True) 