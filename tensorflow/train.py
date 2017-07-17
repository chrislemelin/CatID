from sys import argv
import argparse
import os
import subprocess
import urllib


RETRAIN_REMOTE = "https://raw.githubusercontent.com/tensorflow/tensorflow/r1.2/tensorflow/examples/image_retraining/retrain.py"
RETRAIN_LOCAL = "common/retrain.py"

IMAGE_DIR_DEFAULT= "../trainingData/googleSearchScraper/data"
OUTPUT_GRAPH_DEFAULT= "output/network.pb"
OUTPUT_LABELS_DEFAULT= "output/labels.txt"


"""
Downloads (if necessary) and executes retrain.py.
"""
def retrain(image_dir, output_graph, output_labels):
    t
    ry:
        os.makedirs('output')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Download retrain.py if needed
    if not os.path.isfile(RETRAIN_LOCAL):
        os.makedirs("common")
        urllib.urlretrieve(RETRAIN_REMOTE, RETRAIN_LOCAL)


    subprocess.call([
        "python",
        os.path.join(".", RETRAIN_LOCAL),
        "--image_dir=" + image_dir,
        "--output_graph=" + output_graph,
        "--output_labels=" + output_labels,
    ])

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--image_dir", help="training image directory",
        type=str, default=IMAGE_DIR_DEFAULT)
    parser.add_argument("--output_graph", help="output graph location",
        type=str, default=OUTPUT_GRAPH_DEFAULT)
    parser.add_argument("--output_labels", help="output label location",
        type=str, default=OUTPUT_LABELS_DEFAULT)
    args = parser.parse_args()

    retrain(args.image_dir, args.output_graph, args.output_labels)

if __name__ == "__main__":
    main()
