'''
The module focus on texture drawing (modification)
'''

import common
import PIL, PIL.Image, PIL.ImageDraw, PIL.ImageFont
import typing, math

def _check_range(v, vmin, vmax) -> bool:
    return v <= vmax and v >= vmin and vmax >= vmin

def _check_size(img: PIL.Image.Image, expected_size: tuple[int, int]) -> None:
    (x, y) = img.size
    if not (x == expected_size[0] and y == expected_size[1]):
        raise Exception('assert minecraft texture size failed')

def _check_animation_size(img: PIL.Image.Image, unit_size: tuple[int, int]) -> int:
    (x, y) = img.size
    # check width
    if x != unit_size[0]:
        raise Exception('assert minecraft texture size failed')
    # check height and return frame count
    frame_count: int = y // unit_size[1]
    if frame_count < 1 or y % unit_size[1] != 0:
        raise Exception('assert minecraft texture size failed')
    return frame_count

def border(ctx: common.ImgContext, color: str) -> None:
    """
    Add border for given image. The most simple and widely used drawer in this module.
    
    This function can accept animation texture.
    """
    # get image
    img: PIL.Image.Image = ctx.get_image()
    # if this image have animation, its height must be multiple times of 16.
    # we check width and compute animation frames count
    count: int = _check_animation_size(img, (16, 16))
    # create sketchpad and draw
    sketchpad = PIL.ImageDraw.Draw(img)
    # draw rectangle for each frames
    for i in range(count):
        sketchpad.rectangle(
            (0, i * 16, 15, i * 16 + 15),
            fill=None,
            outline=common.resolve_hex_color(color),
            width=1
        )

def shiny_border(ctx: common.ImgContext, ref_ctx: common.ImgContext) -> None:
    """
    Add a shiny animated border for block. Usually used by ancient debris.
    """
    # check reference image size
    ref_img: PIL.Image.Image = ref_ctx.get_image()
    _check_size(ref_img, (16, 16))
    # create a new image and paste example double
    # get image and resize to new size
    img: PIL.Image.Image = ctx.get_image()
    img.resize((16, 16 * 2))
    # paste ref image
    img.paste(ref_img, (0, 0))
    img.paste(ref_img, (0, 16))
    # create sketchpad and write boundary
    sketchpad = PIL.ImageDraw.Draw(img)
    sketchpad.rectangle(
        (0, 0, 15, 15),
        fill=None,
        outline=common.resolve_hex_color('#18ff00'),
        width=1
    )
    sketchpad.rectangle(
        (0, 16, 15, 31),
        fill=None,
        outline=common.resolve_hex_color('#00ffc6'),
        width=1
    )

    # change animation data forcely
    ctx.set_image_meta({"animation": {"frametime": 5, "interpolate": True}})

def snowflake_overlay(ctx: common.ImgContext) -> None:
    """
    Add a snowflake pattern at the center of block. Usually used by powder snow.
    """
    # read image and check size
    img: PIL.Image.Image = ctx.get_image()
    _check_size(img, (16, 16))
    # create sketchpad and draw snowflake
    sketchpad = PIL.ImageDraw.Draw(img)
    parts: int = 4
    radius: float = 4
    for i in range(parts):
        degree: float = math.radians(180.0 / parts * i)
        x1: float = math.cos(degree) * radius
        y1: float = math.sin(degree) * radius
        sketchpad.line(
            ((round(8 + x1), round(8 - y1)), (round(8 - x1), round(8 + y1))),
            fill=common.resolve_hex_color('#beddef'),
            width=1,
            joint=None
        )

def grass_border(ctx: common.ImgContext, 
                 left_height: int, right_height: int,
                 top_color: str | None, bottom_color: str | None,
                 is_dirt_path: bool) -> None:
    """
    Add border for grass block side like texture. Its border is consisted by 2 individual parts and need to be filled by different color.

    If color is None, it means that corresponding border do not need to be drawn.

    If it is dirt path, a extra offset will be added because the top of dirt path texture is blank.
    """
    # read image and check size
    img: PIL.Image.Image = ctx.get_image()
    _check_size(img, (16, 16))
    # create sketchpad and draw
    sketchpad = PIL.ImageDraw.Draw(img)
    top_offset: int = 1 if is_dirt_path else 0
    # draw border
    if top_color is not None:
        sketchpad.line(
            ((0, left_height), (0, top_offset), (15, top_offset), (15, right_height)),
            fill=common.resolve_hex_color(top_color),
            width=1,
            joint=None
        )
    if bottom_color is not None:
        sketchpad.line(
            ((0, left_height + 1), (0, 15), (15, 15), (15, right_height + 1)),
            fill=common.resolve_hex_color(bottom_color),
            width=1,
            joint=None
        )

def door_border(top_ctx: common.ImgContext, bottom_ctx: common.ImgContext) -> None:
    img: PIL.Image.Image

    # proc top and bottom respectively
    # create sketchpad and draw left and right ring first
    # top
    img = top_ctx.get_image()
    _check_size(img, (16, 16))
    sketchpad = PIL.ImageDraw.Draw(img)
    sketchpad.line(
        ((1, 14), (1, 1), (14, 1), (14, 14)),
        fill=common.resolve_hex_color('#df0906'),
        width=1,
        joint=None
    )
    # bottom
    img = bottom_ctx.get_image()
    _check_size(img, (16, 16))
    sketchpad = PIL.ImageDraw.Draw(img)
    sketchpad.line(
        ((1, 1), (1, 14), (14, 14), (14, 1)),
        fill=common.resolve_hex_color('#df0906'),
        width=1,
        joint=None
    )

g_FontName: str = 'Minecraft.ttf'
def leaves_level(ctx: common.ImgContext, level: int) -> None:
    # get image and check size
    img: PIL.Image.Image = ctx.get_image()
    _check_size(img, (32, 32))
    # check level range
    _check_range(level, 1, 7)

    # create font
    font = PIL.ImageFont.truetype(g_FontName, 14)
    # draw text at center
    sketchpad: PIL.ImageDraw.ImageDraw = PIL.ImageDraw.Draw(img)
    sketchpad.text(
        (17, 13),
        text=str(level),
        fill=common.resolve_hex_color('#ffffff'),
        font=font,
        anchor='mm',
        stroke_width=1,
        stroke_fill=common.resolve_hex_color('#475e2f')
    )

def leaves_persistent(ctx: common.ImgContext, is_persistent: bool) -> None:
    # get image and check size
    img: PIL.Image.Image = ctx.get_image()
    _check_size(img, (32, 32))
    # draw rectangle
    sketchpad = PIL.ImageDraw.Draw(img)
    sketchpad.rectangle(
        (8, 21, 23, 23),
        fill=common.resolve_hex_color('#1e90ff' if is_persistent else '#ffffff'),
        outline=common.resolve_hex_color('#475e2f'),
        width=1
    )

def redstone_dust_level(ctx: common.McContext) -> None:
    pass
