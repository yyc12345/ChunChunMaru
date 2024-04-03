import common
import PIL, PIL.Image, PIL.ImageDraw, PIL.ImageFont
import typing, math

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

def border_block_texture(ctx: common.McContext, name: str, color: str) -> None:
    # read image
    img: PIL.Image.Image = ctx.read_texture(name)
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
    # save result
    ctx.write_texture(name, img)

    # if count is not zero, we should copy its animation data
    if count > 1:
        meta: typing.Any = ctx.read_texture_meta(name)
        ctx.write_texture_meta(name, meta)

g_ColorfulBorderBlockTextureMeta: typing.Any = {"animation": {"frametime": 5, "interpolate": True}}
def colorful_border_block_texture(ctx: common.McContext, name: str) -> None:
    """
    Add a shiny animated border for block. Usually used by ancient debris.
    """
    # read image and check size
    example: PIL.Image.Image = ctx.read_texture(name)
    _check_size(example, (16, 16))
    # create a new image and paste example double
    img: PIL.Image.Image = PIL.Image.new(example.mode, (16, 32))
    img.paste(example, (0, 0))
    img.paste(example, (0, 16))
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
    # save it
    ctx.write_texture(name, img)

    # create animation meta file
    ctx.write_texture_meta(name, g_ColorfulBorderBlockTextureMeta)

def snowflake_overlay_block_texture(ctx: common.McContext, name: str) -> None:
    """
    Add a snowflake pattern at the center of block. Usually used by powder snow.
    """
    # read image and check size
    img: PIL.Image.Image = ctx.read_texture(name)
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

    # save it
    ctx.write_texture(name, img)

def border_door_block_texture(ctx: common.McContext, name: str) -> None:
    # proc top and bottom respectively
    for is_top in (True, False):
        # load images
        door_part: str = name + ('_top' if is_top else '_bottom')
        img: PIL.Image.Image = ctx.read_texture(door_part)
        _check_size(img, (16, 16))
        # decide drawing lines coord point first
        route: tuple[tuple[int, int], ...]
        if is_top:
            route = ((1, 14), (1, 1), (14, 1), (14, 14))
        else:
            route = ((1, 1), (1, 14), (14, 14), (14, 1))
        # create sketchpad and draw left and right ring first
        sketchpad = PIL.ImageDraw.Draw(img)
        sketchpad.line(
            route,
            fill=common.resolve_hex_color('#df0906'),
            width=1,
            joint=None
        )
        # save it as new file
        ctx.write_texture(door_part + '_open', img)

g_FontName: str = 'Minecraft.ttf'
def generate_leaves_level(ctx: common.McContext) -> None:
    # create font
    font = PIL.ImageFont.truetype(g_FontName, 14)

    # create 7 levels leaves
    for i in range(7):
        # adjust it to 1 based
        i += 1
        # create empty image and sketchpad
        img: PIL.Image.Image = PIL.Image.new('RGBA', (32, 32), common.resolve_hex_alpha_color('#00000000'))
        sketchpad: PIL.ImageDraw.ImageDraw = PIL.ImageDraw.Draw(img)
        # draw text at center
        sketchpad.text(
            (17, 13), 
            text=str(i),
            fill=common.resolve_hex_color('#ffffff'),
            font=font,
            anchor='mm',
            stroke_width=1,
            stroke_fill=common.resolve_hex_color('#475e2f')
        )
        # save it
        ctx.write_texture(f'leaves_level_{i}', img)

def generate_leaves_persistent(ctx: common.McContext) -> None:
    # create persistent marker
    for is_persistent in (True, False):
        # create empty image and sketchpad
        img: PIL.Image.Image = PIL.Image.new('RGBA', (32, 32), common.resolve_hex_alpha_color('#00000000'))
        sketchpad = PIL.ImageDraw.Draw(img)
        # draw rectangle
        sketchpad.rectangle(
            (8, 21, 23, 23),
            fill=common.resolve_hex_color('#1e90ff' if is_persistent else '#ffffff'),
            outline=common.resolve_hex_color('#475e2f'),
            width=1
        )
        # save it
        ctx.write_texture(f'leaves_persistent_{"on" if is_persistent else "off"}', img)

def generate_redstone_dust_level(ctx: common.McContext) -> None:
    pass
