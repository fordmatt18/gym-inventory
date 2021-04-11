from gym.envs.registration import register

register(
    id='inventory-v0',
    entry_point='inventory.envs:Inventory',
)