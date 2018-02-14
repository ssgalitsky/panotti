
import json
# preprocess_data -s -m --dur=4.0 -r=44100
# train_network.py --epochs=10 --val=0
settings_json = json.dumps([
    {'type': 'title',
     'title': 'Sorting Hat Settings'},
    {'type': 'string',
     'title': 'Server',
     'desc': 'Hostname or IP address of GPU compute server',
     'section': 'example',
     'key': 'server'},
    {'type': 'string',
     'title': 'Username',
     'desc': 'Username on GPU server',
     'section': 'example',
     'key': 'username'},
    {'type': 'path',
     'title': 'SSH keys',
     'desc': 'Path to ssh keys',
     'section': 'example',
     'key': 'sshKeyPath'},
    {'type': 'bool',
     'title': 'Mono',
     'desc': 'Force audio to mono',
     'section': 'example',
     'key': 'mono'},
    {'type': 'bool',
     'title': 'sequential',
     'desc': 'Sequential order of audio clips (False = Shuffle)',
     'section': 'example',
     'key': 'sequential'},
    {'type': 'numeric',
     'title': 'Duration',
     'desc': 'Length in seconds of audio clips (truncated/padded if too long/short)',
     'section': 'example',
     'key': 'duration'},
    {'type': 'numeric',
     'title': 'Sample rate',
     'desc': 'Sample rate to re-sample all audio clips to',
     'section': 'example',
     'key': 'sampleRate'},
    {'type': 'options',
     'title': 'Starting weights',
     'desc': "Initial neural network weights for training (Default = whatever's on the hard drive)",
     'section': 'example',
     'key': 'weightsOption',
     'options': ['Default', 'Random', "Upload (doesn't work yet)"]},
    {'type': 'numeric',
     'title': 'Epochs',
     'desc': 'Number of machine learning iterations to run.',
     'section': 'example',
     'key': 'epochs'},
    {'type': 'numeric',
     'title': 'Validation split',
     'desc': 'Fraction of training data to "split off" for validation',
     'section': 'example',
     'key': 'val_split'},
     ])
