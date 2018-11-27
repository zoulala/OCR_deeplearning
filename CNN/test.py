import os
import tensorflow as tf
from CNN.model import Model,Config
from CNN.read_util import get_next_batch,char_set


def main(_):

    model_path = os.path.join('models', Config.file_name)
    if os.path.exists(model_path) is False:
        os.makedirs(model_path)

    # 加载上一次保存的模型
    model = Model(Config)
    checkpoint_path = tf.train.latest_checkpoint(model_path)
    if checkpoint_path:
        model.load(checkpoint_path)

    print('start to test...')
    batch_x_test, batch_y_test = get_next_batch(1)
    max_idx_p = model.test(batch_x_test)
    chars = [char_set[idx] for idx in max_idx_p[0]]
    print('predict text:',"".join(chars))


if __name__ == '__main__':
    tf.app.run()
