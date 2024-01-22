from CNN import Net
from az_parallel2 import AlphaZeroParallel2
from ataxx import AtaxxBoard
from torch.optim import Adam
FILL_SIZE = 7
AFLEX_MODEL_PARAMS = {"size":FILL_SIZE, "action_size":FILL_SIZE**4, "num_resBlocks":20, "num_hidden":64}
AFLEX_TRAIN_PARAMS = {"n_iterations":10, "self_play_iterations":20, "mcts_iterations":50, "n_epochs":20, "batch_size":128, "n_self_play_parallel":4, "move_cap":FILL_SIZE**3}
def train():
    model = Net(**AFLEX_MODEL_PARAMS)
    board = AtaxxBoard(4)
    optimizer = Adam(model.parameters(), lr=0.01, weight_decay=0.0001)
    Alpha = AlphaZeroParallel2(model, optimizer, board, 'A', data_augmentation=True, **AFLEX_TRAIN_PARAMS, fill_size=FILL_SIZE)
    Alpha.Learn()

train()