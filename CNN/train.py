import os
import tensorflow as tf
from CNN.model import Model,Config
from CNN.read_util import get_next_batch


def main(_):

    model_path = os.path.join('models', Config.file_name)
    if os.path.exists(model_path) is False:
        os.makedirs(model_path)

    # 加载上一次保存的模型
    model = Model(Config)
    checkpoint_path = tf.train.latest_checkpoint(model_path)
    if checkpoint_path:
        model.load(checkpoint_path)

    print('start to training...')
    model.train(get_next_batch, model_path)


if __name__ == '__main__':
    tf.app.run()
