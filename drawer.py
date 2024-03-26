import common
import PIL, PIL.Image, PIL.ImageDraw
import typing

def border_block_texture(ctx: common.McContext, name: str, color: str) -> None:
    # read image
    img: PIL.Image.Image = ctx.read_texture(name)
    # create sketchpad and draw
    sketchpad = PIL.ImageDraw.Draw(img)
    # draw rectangle
    sketchpad.rectangle(
        (0, 0, 15, 15), 
        fill=None, 
        outline=common.resolve_hex_color(color), 
        width=1
    )
    # save result
    ctx.write_texture(name, img)

