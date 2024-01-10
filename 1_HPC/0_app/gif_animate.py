# ref - https://github.com/tonybutzer/the_handbook/blob/64870d44be57e18eb7dce25dcb57eaa35c037b43/teigen-lightning-talks/1_Oct_2021/4_sioux_falls_animation_research_upside_down.ipynb

import glob
#from IPython.display import Image


from PIL import Image, ImageDraw, ImageFont

from os.path import basename



def make_gif_from_tif(frame_folder, output_gif_name):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.tif")]
    frame_one = frames[0]
    frame_one.save(output_gif_name, format="GIF", append_images=frames,
               save_all=True, duration=500, loop=0)


def make_gif_from_jpeg(frame_folder, output_gif_name):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpeg")]
    frame_one = frames[0]
    frame_one.save(output_gif_name, format="GIF", append_images=frames,
               save_all=True, duration=1500, loop=0)

def make_mpeg_from_jpeg(frame_folder, output_mpeg_name):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpeg")]
    frame_one = frames[0]
    # frame_one.save(output_mpeg_name, format="MPEG", append_images=frames,
               #save_all=True, duration=1500, loop=0)
    frame_one.save(output_mpeg_name, append_images=frames,
               save_all=True, duration=1500, loop=0)



def emboss_image(image_path, the_text):
    # Open an Image
    img = Image.open(image_path)
     
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
     
    # Add Text to an image
    I1.text((28, 36), the_text, fill=(255, 0, 0))
    y = 40
    for font_size in range(12, 40, 10):
        #font = ImageFont.load_default(size=font_size)
        font = ImageFont.truetype("DejaVuSans.ttf", size=font_size)
        I1.text((10, y), f"{the_text} ({font_size}", font=font)
        y += 35
     
    # Display edited image
    #img.show()

    # Save the edited image
    img.save(image_path)


def convert_tif_to_jpeg(image_list):
    src_dir = '/home/ec2-user/data/'
    dst_dir = src_dir + 'jpg/'
    for in_tif in image_list:
        #print(in_tif)
        a = basename(in_tif) 
        #print(a)
        b = a.replace('.tif','.jpg')
        src_file = src_dir + in_tif
        dst_file = dst_dir + b
        print('Convert ', src_file, 'to ', dst_file)
        img = Image.open(src_file)
        rgb_img = img.convert('RGB')
        rgb_img.save(dst_file)
