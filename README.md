# VideoBoard  <img height="25px" src="https://user-images.githubusercontent.com/4397546/64920384-ae1d0500-d7e9-11e9-8aed-308f81088e8c.png"> 


This framework contains a simple UI for image comaprsion between different methods.

![image](https://user-images.githubusercontent.com/4397546/64920210-3d74e900-d7e7-11e9-9033-010b497a8d7d.png)

Original: https://github.com/vinthony/ImageBoard

### Requirements

- Flask
- jinja2

### Usage

1. clone this repo by `git clone https://git.woa.com/shadowcun/VideoBoard`

2. link your CoLVDM result folder under the static folder:

```
ln -s /apdcephfs/xxx/colvdm/Saved_Text2Video ./static/colvdm
```

3. run `pip install flask natsort` to install the requirements.

4. run `python app.py` in the root dir of this project and open your favourite browser to `YOUR_DEVCLOUD_IP:5000`.

5. choose the folder in banner and choose the methods to compare.

6. Go and compare your videos!

### UI function

- [x] adjust video size.
- [x] only compare certain images (remember or only in current page).
- [x] Pagination


### Some hint

- currently, this project is only visualize the `sampled images` in `training!!` and the `text-prompt`. you need to mannually change it in `app.py`

- Any issues and PR are welcome!# EvalBoard
