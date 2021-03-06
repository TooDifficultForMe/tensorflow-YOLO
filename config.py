import os

LEARNING_RATE = 0.00001
#DECAY_STEPS = 5000 * 30
#DECAY_RATE = 0.1
#STAIRCASE = False

EPSILON = 1e-8

BATCH_SIZE = 16
MAX_ITER = 25000
SUMMARY_ITER = 100
PRINT_ITER = 1000
SAVE_ITER = 2000

DATA_PATH = './data'

PASCAL_PATH = os.path.join(DATA_PATH, 'pascal_voc')

CACHE_PATH = os.path.join(PASCAL_PATH, 'cache')

OUTPUT_DIR = os.path.join(PASCAL_PATH, 'output')

SAVE_DIR = './saved_model'

WEIGHTS_DIR = os.path.join(DATA_PATH, 'weights')

WEIGHTS_FILE = 'yolo.ckpt'

CLASSES = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
			'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
			'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
			'train', 'tvmonitor']

IMAGE_SIZE = 448

CELL_SIZE = 7

FLIPPED = False