import drawer, modifier, common
import typing

_OVERWORLD_WOOD_TYPE: tuple[str, ...] = (
    'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry'
)
_NETHER_WOOD_TYPE: tuple[str, ...] = (
    'crimson', 'warped'
)

def _iterate_copper_type() -> typing.Iterator[str]:
    for waxed in ('', 'waxed_'):
        for oxidezed_level in ('', 'exposed_', 'weathered_', 'oxidized_'):
            yield waxed + oxidezed_level + 'copper'

def proc_ore(ctx: common.McContext) -> None:
    # overworld
    modifier.overworld_ore(ctx, 'coal_ore', '#2e2e2e')
    modifier.overworld_ore(ctx, 'copper_ore', '#a65947')
    modifier.overworld_ore(ctx, 'diamond_ore', '#1ed0d6')
    modifier.overworld_ore(ctx, 'emerald_ore', '#17c544')
    modifier.overworld_ore(ctx, 'gold_ore', '#fcee4b')
    modifier.overworld_ore(ctx, 'iron_ore', '#d8af93')
    modifier.overworld_ore(ctx, 'lapis_ore', '#446fdc')
    modifier.overworld_ore(ctx, 'redstone_ore', '#ff0000')
    # nether
    drawer.border_block_texture(ctx, 'nether_gold_ore', '#fcee4b')
    drawer.border_block_texture(ctx, 'nether_quartz_ore', '#d4caba')
    # nether ancient debris need colorful border
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_side')
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_top')
    # raw ore block
    drawer.border_block_texture(ctx, 'raw_copper_block', '#a65947')
    drawer.border_block_texture(ctx, 'raw_gold_block', '#fcee4b')
    drawer.border_block_texture(ctx, 'raw_iron_block', '#d8af93')

def proc_redstone(ctx: common.McContext) -> None:
    # door showcase
    # todo: add copper door when updating to 1.20.3
    for door_type in _OVERWORLD_WOOD_TYPE + _NETHER_WOOD_TYPE + ('bamboo', 'iron'):
        modifier.redstone_door(ctx, door_type + '_door')

