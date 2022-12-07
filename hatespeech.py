from absl import app, flags, logging
import sh

import torch as th
import pytorch_lightning as pl

import nlp 
import transformers
from datasets import load_dataset

flags.DEFINE_integer('epochs', 10, 'number of epochs')
flags.DEFINE_float('lr', 0.001, 'learning rate')
flags.DEFINE_float('momentum', 0.9, 'momentum')
flags.DEFINE_string('model', 'bert-base-multilingual-cased', 'model name')


FLAGS = flags.FLAGS

sh.rm('-rf', 'logs')
sh.mkdir('logs')

class HateSpeechClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()
    
    def prepare_data(self):
        train_ds = load_dataset('hate_speech_offensive', split='train')
        tokenizer = transformers.AutoTokenizer.from_pretrained(FLAGS.model)
        import IPython; IPython.embed(); exit(1)

    def forward(self, batch):
        pass

    def training_step(self, batch, batch_idx):
        pass

    def train_dataloader(self):
        pass

    def configure_optimizers(self):
        return th.optim.SGD(
            self.parameters(), 
            lr=FLAGS.lr, 
            momentum=FLAGS.momentum,
            )



def main(_):
    model = HateSpeechClassifier()
    trainer = pl.Trainer(
        default_root_dir='logs',
        gpus=(1 if th.cuda.is_available() else 0),
        max_epochs=FLAGS.epochs,
    )
    trainer.fit(model)


if __name__ == '__main__':
    app.run(main)
