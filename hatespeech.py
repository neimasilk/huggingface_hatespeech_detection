from absl import app, flags, logging
import sh

import torch as th
import pytorch_lightning as pl

import nlp 
import transformers
from datasets import load_dataset

flags.DEFINE_integer('epochs', 10, 'number of epochs')
flags.DEFINE_float('lr', 0.001, 'learning rate')
flags.DEFINE_integer('batch_size',8,'Batch Size')
flags.DEFINE_float('momentum', 0.9, 'momentum')
flags.DEFINE_string('model', 'bert-base-multilingual-cased', 'model name')
flags.DEFINE_integer('seq_length',32,'seq length ')
flags.DEFINE_bool('debug',True,'debuggin mode')


FLAGS = flags.FLAGS

sh.rm('-rf', 'logs')
sh.mkdir('logs')

class HateSpeechClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = transformers.BertForSequenceClassification.from_pretrained(FLAGS.model)
    
    def prepare_data(self):
        tokenizer = transformers.AutoTokenizer.from_pretrained(FLAGS.model)

        def _tokenize(x):
            x['input_ids']= tokenizer.encode(
                x['text'],
                max_length=FLAGS.seq_length,
                pad_to_max_length=True,
            )
            return x
        def _prepare_ds(split):
            ds = load_dataset('imdb', split=f'{split}[:{FLAGS.batch_size if FLAGS.debug else "5%"}]')
            ds = ds.map(_tokenize)
            ds.set_format('torch', columns=['input_ids', 'label'])
            return ds
        self.train_ds = _prepare_ds('train')
        self.val_ds = _prepare_ds('test')
        self.test_ds = _prepare_ds('test')

 
    def forward(self, batch):
        import IPython; IPython.embed(); exit(1)


    def training_step(self, batch, batch_idx):
        import IPython; IPython.embed(); exit(1)
    
    def validation_step(self, batch, batch_idx):
        import IPython; IPython.embed(); exit(1)
    
    def validation_epoch_end(self, outputs):
        import IPython; IPython.embed(); exit(1)

    def train_dataloader(self):
        return th.utils.data.DataLoader(
            self.train_ds,
            batch_size=FLAGS.batch_size,
            drop_last=True,
            shuffle=True,
        )
    
    def val_dataloader(self):
        return th.utils.data.DataLoader(
            self.val_ds,
            batch_size=FLAGS.batch_size,
            drop_last=True,
            shuffle=True,
        )
    
    def test_dataloader(self):
            return th.utils.data.DataLoader(
                self.test_ds,
                batch_size=FLAGS.batch_size,
                drop_last=True,
                shuffle=True,
            )   

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
        fast_dev_run=FLAGS.debug,
    )
    trainer.fit(model)


if __name__ == '__main__':
    app.run(main)
