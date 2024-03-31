import drawer, modifier, common
import typing

_OVERWORLD_WOOD_TYPE: tuple[str, ...] = (
    'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry', 'bamboo'
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

def proc_common(ctx: common.McContext) -> None:
    # border all wood block
    # log (+-stripped) (原木)
    # wood (+-stripped) (木头) use the same texture with log so no need to process it
    # planks (木板)
    def call_with_check(ctx: common.McContext, name: str, color_tuple: modifier.TreeBlockColors_t) -> None:
        """
        color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color)
        """
        # check name
        tree_type: modifier.TreeType
        if name in _OVERWORLD_WOOD_TYPE:
            if name == 'bamboo': tree_type = modifier.TreeType.Bamboo
            else: tree_type = modifier.TreeType.Overworld
        elif name in _NETHER_WOOD_TYPE: tree_type = modifier.TreeType.Nether
        else: raise Exception('invalid tree type')
        # call real function
        modifier.tree_block(ctx, name, color_tuple, tree_type)
    call_with_check(ctx, 'oak', ('#382b18', None, '#846a3a', None, '#67502c'))
    call_with_check(ctx, 'spruce', ('#553a1f', None, '#544525', None, '#553a1f'))
    call_with_check(ctx, 'birch', ('#aea6a4', None, '#9d8754', None, '#907e58'))
    call_with_check(ctx, 'jungle', ('#635820', None, '#977c45', None, '#68462f'))
    call_with_check(ctx, 'acacia', ('#5b554d', None, '#8f4c2a', None, '#7b4024'))
    call_with_check(ctx, 'dark_oak', ('#584428', '#53381a', '#32281a', None, '#291a0c'))
    call_with_check(ctx, 'mangrove', ('#3c2f23', '#3c2f23', '#632122', None, '#5d1c1e'))
    call_with_check(ctx, 'cherry', ('#1b0f16', None, '#c07974', None, '#cd8580'))
    call_with_check(ctx, 'bamboo', ('#5a6627', '#505c23', '#615526', '#615526', '#615526'))
    call_with_check(ctx, 'crimson', ('#7b0000', '#442131', '#6a2640', None, '#3f1e2d'))
    call_with_check(ctx, 'warped', ('#16615b', '#442131', '#2e8578', None, '#113835'))

    # tree leaves
    # prepare leaves first
    modifier.prepare_tree_leaves(ctx)
