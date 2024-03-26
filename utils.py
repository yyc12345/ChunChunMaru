import common, drawer
import typing

def border_ore_block(ctx: common.McContext, name: str, color: str, deepslate_color: str | None = None) -> None:
    if deepslate_color is None:
        deepslate_color = color

    drawer.border_block_texture(ctx, name, color)
    drawer.border_block_texture(ctx, 'deepslate_' + name, deepslate_color)
